
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

int A[10005];
int main(int argc, char** argv)
{
	int t; S("%d", &t );
	REP(tc, t )
	{
		int n,l,h;
		S("%d%d%d", &n, &l, &h );
		REP(i, n) S("%d", &A[i] );
		bool fl;
		int Ans =0;
		FOR(i, l, h+1 )
		{
			fl = true;
			REP(j, n )
			{
				if( A[j]%i == 0 || i%A[j] == 0 )
				{
				}
				else
				{
					fl = false;
					break;
				}
			}
			if( fl )
			{
				Ans = i;
				break;
			}
		}
		P("Case #%d: ", tc+1 );
		if( Ans )
		{
			P("%d\n", Ans );
		}
		else
		{
			puts("NO");
		}
	}
	return 0;
}
