//#include <algorithm>  
#include <iostream>  
//#include <sstream>  
#include <string>  
#include <vector>  
//#include <queue>  
//#include <set>  
//#include <map>  
//#include <cstdio>  
//#include <cstdlib>  
//#include <cctype>  
//#include <cmath>  
//#include <list>  
using namespace std;  

//a to b-1
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n)  
//a to b
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)
typedef long long ll;

#define IPSET 50

void algo(int testNum) 
{
	// read each test inputs..
	int rows, colms;
	cin >> rows >> colms;

	char pic[IPSET+10][IPSET+10];
	int numb = 0;
	bool impossi= false;
	for(int i = 0; i < rows; i++)
	{
		string rowstr;
		cin >> rowstr;
		for(int j=0; j <colms; j++)
		{			
			pic[i][j] = rowstr.at(j);
			if(!impossi && pic[i][j] == '#' )
			{
				numb++;
				j++;
				if( j < colms )
				{
					pic[i][j] = rowstr.at(j);
					if( pic[i][j] != '#' ) 
						impossi=true;
					else 
						numb++;
				}
				else
					impossi=true;
			}
		}	
	}
	if(!impossi && numb%4 != 0)  impossi = true;

	for(int i = 0; i < rows && !impossi; i++)
	{
		for(int j=0; j <colms && !impossi; j++)
		{
			if( pic[i][j] == '#')
			{	if( j+1 < colms && pic[i][j+1] =='#' &&
					i+1 < rows && pic[i+1][j]=='#' && pic[i+1][j+1]=='#' )
				{
					pic[i][j] = pic[i+1][j+1] = '/';
					pic[i][j+1] = pic[i+1][j]='\\';
				}
				else 
					impossi = true;
			}
		}	
	}

	cout << "Case #" << testNum << ":" << endl;	
	if( impossi ) 
		cout << "Impossible" << endl;
	else
	{
		for(int i = 0; i < rows ; i++)
		{	for(int j=0; j <colms; j++)
				cout << pic[i][j];
			cout << endl;
		}
	}
}

int main() {
	int test_num=0;
	cin >> test_num;
	
	FORE(i,1,test_num) algo(i);
	
	return 0;
}