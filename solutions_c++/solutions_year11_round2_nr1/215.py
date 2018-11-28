///Team Heisenbug
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <cassert>
#include <vector>
#include <fstream>
#include <stack>
#include <cstring>
#include<sys/time.h>
/*****************************************************************************************************
					macros and typedefs for shortening length
******************************************************************************************************/
///Fast IO
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define SZ(c) (c).size()
#define ps(n) printf("%s\n",n)
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

/*****************************************************************************************************
							Program starts here
******************************************************************************************************/
///macros for global constants
#define MAXN 101
int N;
char A[MAXN][MAXN];
double AWP[MAXN];
double AOWP[MAXN];
double AOOWP[MAXN];
bool VWP[MAXN];
bool VOWP[MAXN];
bool VOOWP[MAXN];


double WP(int idx)
{
	if(VWP[idx] == 1)
	return AWP[idx];
	
	VWP[idx] = 1;
	
	int win = 0;
	int total = 0;
	
	for(int i=0;i<N;i++)
	if(A[idx][i] != '.')
	{
		if(A[idx][i] == '1')
		win++;
		
		total++;
	}
	
	return AWP[idx] = (double)win/total;
}
double OWP(int idx)
{
	if(VOWP[idx] == 1)
	return AOWP[idx];
	
	VOWP[idx] = 1;
	
	//throw out games of idx
	double sum = 0;
	int teams = 0;
	
	for(int i=0;i<N;i++)
	{
		if(A[idx][i] == '.')
		continue;
		
		int win = 0;
		int total = 0;
		
		for(int j=0;j<N;j++)
		{
			if(j == idx)continue;
			
			if(A[i][j] != '.')
			{
				if(A[i][j] == '1')
				win++;
				
				total++;
			}
		}
		sum += (double)win/total;
		teams++;
	}
	return AOWP[idx] = sum/teams;
}
double OOWP(int idx)
{
	if(VOOWP[idx] == 1)
	return AOOWP[idx];
	
	VOOWP[idx] = 1;
	
	int teams = 0;
	double sum = 0;
	
	for(int i=0;i<N;i++)
	{
		if(A[idx][i] == '.')
		continue;
		
		sum += OWP(i);
		teams++;
	}
	
	return AOOWP[idx] = sum/teams;
}

int main()
{
	int T;
	scanf("%d",&T);
	
	FOR(cases,1,T+1)
	{
		scanf("%d",&N);
		REP(i,N)
		{
			VWP[i] = VOWP[i] = VOOWP[i] = 0;
		}
		
		REP(i,N)
		scanf("%s",A[i]);
		
		printf("Case #%d:\n",cases);
		REP(i,N)
		{
			double rpi = 0.25 * WP(i) + 0.5 * OWP(i) + 0.25 * OOWP(i);
			printf("%.9lf\n",rpi);
		}
	}
	return 0;
}
