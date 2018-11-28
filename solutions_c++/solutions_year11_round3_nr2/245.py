
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
#include <fstream>

using namespace std;

#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
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

//int d[][2]={{-1,0},{1,0},{0,-1},{0,1}};

LL A[1005];
LL f[1000004];
LL g[1000004];
LL timesave[1000004];
int main(int argc, char** argv)
{
	int tt; S("%d", &tt );
	LL L, n, C;
	LL t;
	REP(tc, tt )
	{
		cin >> L >> t >> n >> C;
		memset(f, 0, sizeof(f));
		memset(g, 0, sizeof(g));
		memset(timesave,0, sizeof(timesave) );
		REP(i, C ) cin >> A[i];
		REP(i, n ) f[i] = A[(i%C)];
		g[0] = f[0];
		FOR(i,1, n ) g[i] = g[i-1] + f[i];
		
		FORD(i, n-1, 0 )
		{
			if( g[i]*2>= t )
			{
				timesave[i] = min( f[i], g[i]-(t/2) );
			}
		}
		sort( timesave, timesave+n );
		LL Ans = g[n-1]*2;
		REP(i, L )
		{
			if( n-1-i >= 0 )
			{
				Ans -= timesave[n-1-i];
			}
		}
		/*if( L == 2 )
		{
			int ts1, ts2;
			REP(i, n ) FOR(j, i+1, n )
			{
				if( g[i]*2 >= t )
				{
					ts1 = min(f[i], g[i]-(t/2));
					if( g[i]*2-ts1 >= t )
					{
						ts2 = min( f[j], (2*g[i]-ts1 - t)/2 );
						Ans = min( Ans, g[n-1]*2-ts1-ts2);
						//cout << g[n-1]*2-ts1-ts2 << endl;
					}

				}
			}
		}*/
		P("Case #%d: ", tc+1 );
		cout << Ans << endl;
	}
   return 0;
}
