#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <string>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

#define fi first
#define sc second
#define MP make_pair
#define pb push_back
#define PI acos(-1.0) //alternative #define PI (2.0 * acos(0.0))
#define vi vector<int>
#define vii vector<ii>
#define ALL(c) (c).begin(), (c).end()
#define RESET( c,a ) memset( (c), a, sizeof(c) )
#define REP( a,b,c ) for ( int a=b, _c=c; a<_c; ++a )
#define RED( a,b,c ) for ( int a=b, _c=c; a>=_c; --a )
#define REPI( it, c ) for ( __typeof( (c).begin() ) it=(c).begin(); it!=(c).end(); ++it )

const int big = 2000000000;
const double INF = 1e9;
const double EPS = 1e-9;

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pLL;

#define _DEBUG 1
#ifdef _DEBUG
	#define DEBUG printf
#else
	#define DEBUG if (0) printf
#endif

// NTU The Lyons' Template
//----------------------------------------------------------------------

char i[5][5];
bool cek( int m )
{
	if (m==1 or m==2)
	{
		char c = ((m==1)?'X':'O');
		REP(y,0,4)
		{
			bool ret=true;
			REP(x,0,4)
				if (i[y][x] != c && i[y][x] != 'T')
				{
					ret = false;
					break;
				}
			if (ret) return ret;
		}
		
		REP(x,0,4)
		{
			bool ret=true;
			REP(y,0,4)
				if (i[y][x] != c && i[y][x] != 'T')
				{
					ret = false;
					break;
				}
			if (ret) return ret;
		}
		
		//diagonal left-right
		{
			bool ret=true;
			REP(z,0,4)
				if (i[z][z] != c && i[z][z] != 'T')
				{
					ret = false;
					break;
				}
			if (ret) return ret;
		}
		
		//diagonal right-left
		{
			bool ret=true;
			REP(z,0,4)
				if (i[z][3-z] != c && i[z][3-z] != 'T')
				{
					ret = false;
					break;
				}
			if (ret) return ret;
		}
		
	}
	
	if (m==3)
	{
		REP(y,0,4) REP(x,0,4)
			if (i[y][x] == '.') return true;
	}
	
	return false;
}

int main()
{
	int T;
	scanf("%d", &T); scanf("%*c");
	REP( TT, 1 , T+1 )
	{
		RESET( i, 0 );
		REP(y,0,4) gets( i[y] );
		
		printf("Case #%d: ", TT);
		if (cek(1))
			printf("X won\n");
		else if (cek(2))
			printf("O won\n");
		else if (cek(3))
			printf("Game has not completed\n");
		else
			printf("Draw\n");
		
		gets( i[0] );
	}
	return 0;
}
