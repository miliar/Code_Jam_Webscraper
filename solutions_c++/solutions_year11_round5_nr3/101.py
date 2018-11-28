/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

#define LET(x,a) __typeof(a) x (a)
#define ITER(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOREACH(it,v) ITER(it,v.begin(),v.end())

#define FILLA(a,x) memset(&a,x,sizeof(a))
#define FILL(a,x) memset(a,x,sizeof(a))
#define CLEARA(a,x) FILLA(a,0)
#define CLEAR(a) FILL(a,0)

#define m_p make_pair
#define fst first
#define snd second
typedef pair<int,int> PII;
typedef long long ll;
template<class T> void check_max( T&a, T b ){ if ( a < b ) a = b; }
template<class T> void check_min( T&a, T b ){ if ( a > b ) a = b; }

//#define debug

const int MAXN = 10;
int Map[MAXN][MAXN];
int r,c;

int mv[4][2][2] = { { {0,1},{0,-1} }, {{1,0},{-1,0}}, {{1,1},{-1,-1}}, {{1,-1},{-1,1}} };

int nx[MAXN][MAXN], ny[MAXN][MAXN];
int MOD( int a, int b ){
	return (a%b+b)%b;
}
void trans( int x, int y, int id, int cs ){
	nx[x][y] = MOD(x+mv[id][cs][0],r);
	ny[x][y] = MOD(y+mv[id][cs][1],c);
}
int id[MAXN][MAXN];
bool ok( int state ){
	REP(i,0,r)REP(j,0,c){
		int ch = Map[i][j];
		int cs = !!(state&( 1<<( i*c+j ) ));

		if ( ch=='-' )
			trans(i,j,0,cs);
		else if ( ch == '|')
			trans(i,j,1,cs);
		else if ( ch == '\\')
			trans(i,j,2,cs);
		else if ( ch == '/')
			trans(i,j,3,cs);
	}

	memset(id,0,sizeof(id));
	REP(i,0,r)REP(j,0,c){
		id[nx[i][j]][ny[i][j]] ++;
	}
	REP(i,0,r)REP(j,0,c)
		if ( id[i][j] != 1 )
			return false;
	return true;
}

int main(){
	int T; cin >> T;
	REP(Case,1,T+1){
		cin>>r>>c;
		REP(i,0,r){
			string s;
			cin >> s;
			REP(j,0,c) Map[i][j] = s[j];
		}
		int ans = 0;
		int maxs = 1<<(r*c);
		REP(s,0,maxs){
			if ( ok(s) )
				ans++;
		}
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}
