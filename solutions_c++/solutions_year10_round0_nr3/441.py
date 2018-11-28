
/***** Author : Kunal *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>

using namespace std;

#define F(a,b) for(int a=0;a<b;a++)
#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define S scanf
#define P printf

#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int, PII> PIII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

//int d[][2]={{-1.0},{1,0},{0,-1},{0,1}};

int g[1200];
LL Z[10000000];
int vis[1200];

int main()
{
	int t; S("%d", &t);
	int R, k, N;
	int step, idx, no;
	int ss;
	int rS, initSteps;
	LL rA;
	REP(tc, t )
	{
		S("%d%d%d", &R, &k, &N );
		REP(i, N ) S("%d", &g[i] );
		REP(i, N ) vis[i] = -1;
		idx = step = 0;
		Z[0] = 0;
		step = 1;
		do
		{
			no = 0;
			ss = idx;
			while( 1 )
			{
				if( no + g[idx] > k ) break;
				else
				{
					if( no == 0 )
					{
						if( vis[idx] != -1 )
						{
							rS = step - vis[idx];
							initSteps = vis[idx] - 1;
							rA = Z[step-1] - Z[vis[idx]-1];
							goto out;
						}
						else
						{
							vis[idx] = step;
						}
					}
					no += g[idx];
					idx++;
					if( idx >= N ) idx -= N;
					if( idx == ss ) break;
				}
			}
			Z[step] = Z[step -1 ] + no;
			step++;
			if( idx == 0 )
			{
				initSteps = 0;
				rS = step -1;
				rA = Z[step-1];
			}
		}while( idx != 0 );
out:
		step --;
		if( R <= initSteps )
		{
			P("Case #%d: %lld\n", tc+1, Z[initSteps] );
		}
		else
		{
			P("Case #%d: %lld\n", tc+1, rA*((R-initSteps)/rS) + Z[(R-initSteps)%rS + initSteps]  );
		}
	}
	return 0;
}
