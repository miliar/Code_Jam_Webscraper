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

int main(int argc, char** argv)
{
	int t; S("%d", &t );
	LL A[1000];
	REP(tc, t )
	{
		int n; S("%d", &n );
		REP(i, n ) S("%lld", &A[i] );
		LL sum = 0, sumx = 0;
		REP(i, n )
		{
			sum ^= A[i];
			sumx += A[i];
		}

		//LL tmp, mval = -1;
		//LL tmp2;
		/*REP(i, 1<<n )
		{
			tmp = tmp2 = 0;
			REP(j, n )
			{
				if( i&(1<<j) )
				{
					tmp ^= A[j];
					tmp2 += A[j];
				}
			}
			if( (sum^tmp) == tmp && min(tmp2, sumx-tmp2) != 0 )
			{
				mval = max( mval, max( tmp2, sumx - tmp2 ) );
			}
		}*/
		sort( A, A+n );
		P("Case #%d: ", tc+1 );
		if( sum != 0 )
		{
			//assert( sum != 0);
			P("NO\n");
		}
		else
		{
			//assert( sum == 0 );
			P("%lld\n", sumx - A[0] );
		}
	}
   return 0;
}
