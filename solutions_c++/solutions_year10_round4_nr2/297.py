#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)

#define ll long long
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}

int dp[15][3000][15];
int mat[20][3000];
#define INF 1000000000
int P;
int doit(int col, int row, int choosen)
{
//	printf("%i %i %i\n", col, row, choosen);
	if( row == 0 )
	{
		if( P-choosen > mat[row][col] ) return INF;
		return 0;
	}
	int & res = dp[row][col][choosen];
	if( res >= 0 ) return res;
	res = INF;
	// supongamos q elegimos la columna...
	
	int a1 = doit(2*col, row-1, choosen+1), a2 = doit(2*col+1, row-1, choosen+1);
	if( a1 != INF && a2 != INF )
		res = min( mat[row][col] + a1+a2, res);
//	if( row == 3 ) printf("%i\n", res);
	// si no lo elegimos...
	a1 = doit(2*col, row-1, choosen), a2 = doit(2*col+1, row-1, choosen);
	if( a1 != INF && a2 != INF )
		res = min( a1+a2, res);

	return res;
}

int main()
{
	int i,j ,k;
	int casos; cin >> casos;
	for( int h = 0 ; h < casos; h ++ )
	{
		cin >> P;
		int cant = 1<<P;
		int fila = 0;
		while( cant )
		{
			for( int i = 0 ; i < cant ; i++ )
			{
				cin >> mat[fila][i];
//				printf("%i ", mat[fila][i] );
			}
			fila ++;
			cant /= 2;
		}
		
		REP(j, 3000) REP(i, 15) REP(k, 15) dp[i][j][k] = -1;

		


	       cout << "Case #" << (h+1) << ": " << doit(0, fila-1, 0) << endl;
	}return 0;
}











