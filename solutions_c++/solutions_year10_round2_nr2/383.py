
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

int X[100];
int V[100];
int B[100];

int main()
{
	int tc; S("%d", &tc);
	int n, k, b, t;
	int cv;
	int ctr;
	REP(tc1, tc )
	{
		S("%d%d%d%d", &n, &k, &b, &t );
		REP(i,n) S("%d", &X[i] );
		REP(i,n) S("%d", &V[i] );
		cv = INF;
		FORD(i , n-1, 0 )
		{
			cv = min( V[i], cv );
			B[i] = cv;
		}
		cv = INF;
		ctr = 0;
		FORD( i, n-1, 0 )
		{
			cv = min( V[i], cv );
			if( X[i] + t*cv >= b )  ctr++;
			else break;
		}
		P("Case #%d: ", tc1+1 );
		int Ans = 0;
		if( k-ctr > 0 )
		{
			int idx = n-1 - ctr;
			FORD( i, idx, 0 )
			{
				if( X[i] + t*V[i] >= b )
				{
					//if( B[i] < V[i] )
					//{
						/*FOR( x, i+1, n-ctr+1 )
						{
							//if( (B[x] >= V[i]) || ( B[x] != V[i]  && (X[i]-X[x])/(B[x]-V[i]) <= min( t, (int)ceil(b-X[x])/B[x] ) ) )
							{
								ctr++;
								B[x-1] = V[i];
								break;
							}
							Ans++;
						}*/
						Ans += n - ctr -1 -i;
						ctr++;
					//}
					//else ctr++;
				}
				if( k == ctr ) break;
			}
			if( k == ctr)
			P("%d\n", Ans );
			else P("IMPOSSIBLE\n");
		}
		else
		{
			P("0\n");
		}
	}
	return 0;
}
