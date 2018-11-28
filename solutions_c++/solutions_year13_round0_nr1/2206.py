#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>

#define inf (1<<30)
#define eps 1e-5
#define ll long long
#define all(v)  v.begin() , v.end()
#define sc(x) scanf("%d",&x)
#define me(t,val) memset( t , val , sizeof(t) )

#define N 4
#define MOD 1000000007

using namespace std;

vector< string >S( N );
void Trans()
{
	vector< string >temp = S;	
	for( int i = 0 ; i < N ; ++i )
		for( int j = 0 ; j < N ; ++j )
			temp[i][j] = S[j][i];
	S = temp;
}
bool g( char c )
{
	for( int i = 0 ; i < N ; ++i )
		if( count( all(S[i]) , c ) + count( all(S[i]) , 'T' ) == 4 )return 1;
	string temp ;
	for( int i = 0 ; i < N ; ++i ) temp += S[i][i];
	if( count( all(temp) , c ) + count( all(temp) , 'T' ) == 4 )return 1;
	temp ="";
	for( int i = 0 ; i < N ; ++i ) temp += S[i][N-i-1];
	if( count( all(temp) , c ) + count( all(temp) , 'T' ) == 4 )return 1;	
	return 0;	
}
bool f( char c )
{
	if( g(c) )return 1;
	Trans();
	bool ans = g(c);
	Trans();
	return ans;	
}
int main()
{
	int tc;
	cin >> tc;
	for( int t = 0 ; t < tc ; ++t )
	{
		for( int i = 0 ; i < N ; ++i )
			cin >> S[i];
		string temp = accumulate( all(S) , string("") );
		int cntO = count( all( temp ) , 'O' ) , cntX = count( all( temp ) , 'X' ) , cntT = count( all( temp ) , 'T' );
		int cntP = N*N - cntO - cntX - cntT;
		bool Xwin = f('X') , Owin = f('O');
		printf( "Case #%d: " , t + 1 );
		if( cntP == 0 )
		{
			if( !(Xwin || Owin) )puts("Draw");
			else if( Xwin )puts("X won");
			else	puts("O won");
		}
		else
		{
			if( !(Xwin || Owin) )puts("Game has not completed");
			else if( Xwin )puts("X won");
			else	puts("O won");			
		}
	}
}
