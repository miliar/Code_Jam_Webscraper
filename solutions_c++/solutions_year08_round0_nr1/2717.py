#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include<fstream>
#include <cctype>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <map>
#include <stack>
#include <sstream>
#include<set>
#include<map>
#ifdef __GNUC__
#define longlong long long
#else
#define longlong __int64
#endif

using namespace std; 

typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 

int dp[101][1001] ; 
vector< string > engine;
vector< string > query ; 

int N , M ; 

int GetNumber( int index, int current )
{

	int i ; 
	if ( index >= M ) return 0 ; 

	if ( dp[index][current] != -1 )
		return dp[ index][ current] ;

	int& ret = dp[ index][ current] ; 
	ret = M ; 

	if ( engine[ current ] != query[ index] )
		return ret = GetNumber( index + 1 , current ) ; 

	for (i = 1 ; i < N ; i++ ) 
	{
		int t= ( current + i ) % N ; 
		ret = min( ret , 1 + GetNumber( index +1 , t ) ); 
	}
	return ret ; 
}



int  main()
{
	ifstream inp ;	ofstream out ;
	char tt[120] ; 
	inp.open("A-small.in");
	out.open("A-small.out");
	
	string t ; 
	int i , j ;
	int cases ; 
	inp >> cases ; 
	inp.getline( tt , 100) ; 
	

	for ( int icase = 1 ; cases-- ; icase++ ) 
	{
        engine.clear();
        query.clear();
        
        memset( dp , -1 , sizeof( dp )) ; 
		inp>>N ;
		inp.getline( tt , 100 ) ;
		for(i = 0 ; i < N ; i++ ) 
		{
			inp.getline( tt , 100 ) ;
			engine.push_back( string( tt )  ) ; 

		}
		inp>>M ; 
		inp.getline( tt , 100 ) ; 
		for(i = 0 ; i < M ; i++ ) 
		{
			inp.getline( tt , 100 ) ; 
			query.push_back(  string( tt )  ) ; 

		}
		int ret = GetNumber( 0 , 0 )  ;
		for (i = 1 ; i < N ; i++ ) 
    	{
    		ret = min( ret ,  GetNumber( 0 , i ) ); 
    	}
		out<<"Case #"<<icase<<": "<<ret<<"\n" ;
	}
	return 0;
}


