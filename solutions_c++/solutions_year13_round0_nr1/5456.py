#include <list>
#include <set>
#include <map>
#include <ctime>
#include <stack>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <deque>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iterator>
#include <cassert>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <complex>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
 
#define For(i,n) for( int i=0; i < n; i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define ALL(c)  c.begin() , c.end()
#define LL long long
#define int64 LL
#define Set(t,v) memset((t), (v), sizeof(t))

typedef vector < int > VI;
typedef pair< int , int > PII;
#define fr first
#define se second
#define pi M_PI
#define rad(x) (x)*acos(-1)/180.0
#define EPS 1e-6
#define INF 10000*10000
stringstream ss;
#define two(x) ( 1LL<<x )
#define sq(x) ( (x)*(x) )
LL mod = 1000000007LL;

/**************************Code****************************/

char mat[4][4];

int ok( int x , int y )
{
	int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
	for( int i = 0 ; i < 4 ; i ++ )
	{
		if( y+i < 4 )
			c1 += mat[x][y+i] == mat[x][y] || mat[x][y+i] == 'T';
		if( x+i < 4 )
			c2 += mat[x+i][y] == mat[x][y] || mat[x+i][y] == 'T';
		if( x+i < 4 && y+i < 4 )
			c3 += mat[x+i][y+i] == mat[x][y] || mat[x+i][y+i] == 'T';
		if( x+i < 4 && y-i >= 0 )
			c4 += mat[x+i][y-i] == mat[x][y] || mat[x+i][y-i] == 'T';
	}
	return c1 == 4 || c2 == 4 || c3 == 4 || c4 == 4;
}

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		int comp = 0;
		For( i , 4 )
			For( j , 4 )
				cin >> mat[i][j], comp = mat[i][j] == '.';
		char win = -1;
		For( i , 4 )
			For( j , 4 )
				if( ( mat[i][j] == 'X' || mat[i][j] == 'O' ) && ok( i , j ) )
					win = mat[i][j];
		if( win != -1 )
			cout << "Case #" << ++ cc << ": " << win << " won" << endl;
		else if( comp )
			cout << "Case #" << ++ cc << ": Game has not completed" << endl;
		else
			cout << "Case #" << ++ cc << ": Draw" << endl;
	}
	return 0;
}