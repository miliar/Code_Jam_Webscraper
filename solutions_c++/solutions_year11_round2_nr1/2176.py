#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

//a to b-1
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n)  
//a to b
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)
typedef long long ll;

#define IPSET 100

void algo(int testNum) 
{
	// read each test inputs..
	int nTeams = 0;
	cin >> nTeams;

	int oppon[IPSET][IPSET]={2}; //2 not playd, 1-WIn, 0 -loss
	long double wp[IPSET]={0L};
	long double owp[IPSET]={0L};
	long double oowp[IPSET]={0L};
	int play[IPSET] = {0};
	int win[IPSET]={0};
	int loss[IPSET]={0};
	int opp[IPSET]={0};

	for(int i = 0; i < nTeams; i++)
	{
		for(int j = 0; j < nTeams; j++)
		{
			char ch;
			cin >> ch;
			if( ch == '.') 
			{
				oppon[i][j]	=2;
				continue;
			}

			if( ch == '1' ) 
			{
				oppon[i][j] = 1;
				play[i]++; win[i]++;opp[i]++;
			}
			else if( ch == '0' ) 
			{	
				oppon[i][j] = 0;
				play[i]++;opp[i]++;
			}
		}
		wp[i] = (win[i]*1.0)/play[i];
	}
	
	for(int i = 0; i < nTeams; i++)
	{	
		long double wpSum = 0.000000000000000L;
		int oppT = opp[i];
		for(int j = 0; j < nTeams; j++)
		{
			if(oppon[i][j] == 2)continue;

			int playExlOpp = play[j];
			int winExlOpp = win[j];

			if( playExlOpp != 0) playExlOpp--;
			if( oppon[j][i] == 1 && winExlOpp != 0) winExlOpp--;
			if(playExlOpp)
				wpSum += (winExlOpp*1.0)/playExlOpp ;
		}	
		owp[i] = wpSum / oppT;
	}

	for(int i = 0; i < nTeams; i++)
	{
		for(int j = 0; j < nTeams; j++)
		{
			if( oppon[i][j]==2) continue;
			oowp[i] += owp[j];
		}
		oowp[i]/=opp[i];
	}

	cout << "Case #" << testNum << ":" << endl;
	cout.precision( 12);
	for(int i = 0; i < nTeams; i++)
	{
		cout << (0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] ) << endl;
	}
	
}

int main() {
	int test_num=0;
	cin >> test_num;
	
	FORE(i,1,test_num) algo(i);
	
	return 0;
}