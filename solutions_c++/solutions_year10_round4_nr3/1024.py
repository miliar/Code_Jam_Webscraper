
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
#include <fstream>

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

int A[300][300][2];

int main()
{
	int t; S("%d", &t);
	int n;
	int off = 100;
	int x1,x2,y1,y2;
	int ctr = 0;
	int Ans;
	REP( tc, t )	
	{
		S("%d", &n );
		memset( A, 0, sizeof A );
		REP(i,n)
		{
			cin >> x1 >>y1 >> x2>> y2;
			x1+=off; x2+=off; y1+=off; y2+=off;
			FOR( a, x1, x2+1 ) FOR( b, y1, y2+1 ) A[a][b][0] = 1;
		}
		int tx = 0;
		REP(i, 251) REP(j,251) if( A[i][j][tx] == 1) ctr++;
		Ans = 0;
		while( ctr )
		{
			Ans++;
			//cout<< ctr << endl;
			//FOR(i,50, 251) FOR(j,50,251) A[i][j][tx^1] = 0;
			FOR(i,50, 251 )
			{
				FOR(j,50, 251 )
				{
					if( A[i-1][j][tx] == 1 && A[i][j-1][tx] == 1 && A[i][j][tx] == 0 )
					{
						A[i][j][tx^1] = 1;
						ctr++;
					}
					else if( A[i-1][j][tx] == 0 && A[i][j-1][tx] == 0 && A[i][j][tx] == 1 )
					{
						A[i][j][tx^1] = 0;
						ctr--;
					}
					else A[i][j][tx^1] = A[i][j][tx];
				}
			}
			tx^=1;
			if( Ans == 10000) exit(0);
		}
		P("Case #%d: ", tc+1 );
		P("%d\n", Ans);
	}
	return 0;
}
