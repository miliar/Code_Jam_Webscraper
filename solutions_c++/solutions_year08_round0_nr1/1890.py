#include <iostream>
#include <vector>
#include <stack>
#include <math.h>
#include <queue>
#include <algorithm>
#include <string>
#include <map>
#include <list>
#include <fstream>
using namespace std ;

#define INVALIDED 100000 

vector<string> engines ;
vector<string> querey  ;

int S = 0 , Q = 0 ;	

int DP[1002][101] ;

int DPProcess()
{
	for( int j = 0 ; j < S ;  ++ j )
	{
		if( querey[0] == engines[j])
		{
			DP[0][j] = 1 ;
		}
	}

	for( int i = 1 ; i < Q ; ++ i)
	{
		for( int j = 0 ; j < S ; ++ j)
		{
			int temp = 1000 ;
			for( int k = 0 ; k < S ; ++ k)
			{
				if( temp > DP[ i - 1][k] && k != j)
					temp = DP[ i - 1][k] ;
			}
			DP[i][j] = min( DP[i - 1][j]  , temp + 1 );
			if( querey[ i] == engines[j])
			{
				DP[i][j] = INVALIDED ;
			}
		}
	}

	int result = 1000 ;
	for( int j = 0 ; j < S ; ++ j)
	{
		if(result > DP[Q - 1][j])
		{
			result = DP[Q - 1][j] ;
		}
	}

	return result ;
}

int main()
{
	int N = 0 , round = 1;
	ofstream outfile ;
	outfile.open("c://output.txt") ;

	cin >> N ;
	while( N --)
	{
		cin >> S ;
		string temp ;
		getline( cin , temp);
		
		for( int i = 0 ; i < S ; ++ i)
		{
			getline( cin , temp);
			engines.push_back(temp)  ;
		}

		cin >> Q ;
		getline( cin , temp);
		for(int i = 0 ; i < Q ; ++ i)
		{
			getline( cin , temp);
			querey.push_back(temp)  ;
		}
		if( Q == 0)
		{
			outfile << "Case #"<< round ++ <<": " << 0 << endl ;
			continue ;
		}
		memset(DP , 0 , sizeof(DP));

		int result = DPProcess() ;

		outfile << "Case #"<< round ++ <<": " << result << endl ;
		engines.clear() ;
		querey.clear();
	}
}