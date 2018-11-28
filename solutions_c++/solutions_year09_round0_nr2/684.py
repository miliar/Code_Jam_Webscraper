
/* Author :: Yash */
#include <vector>
#include <list>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <deque>
#include <fstream>
#include <stack>
#include <bitset>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i) 
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define PP pop()
#define EM empty()
#define INF 1000000000
#define PF push_front
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define V(x) vector< x >
#define Debug false
#define PRINT(x)        cout << #x << " " << x << endl
#define LET(x,a) 	    __typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define PRESENT(c,x) 	((c).find(x) != (c).end())
#define SZ(x) 		x.size();
#define CPRESENT(c,x) 	(find(c.begin(),c.end(),x) != (c).end())
#define D(N) 		int N
#define S(N)		scanf("%d",&N)

typedef pair<int,int>  PI;
typedef pair<int,PI>   TRI;
typedef V( int )       VI;
typedef V( PI  )       VII;
typedef V( string )    VS;
typedef long long      LL;

int H,W;
int Inp[105][105];

// H == W == 100.
// Inp[i][j] <= 10000

int memo[105][105], d[4][2] = {{-1,0},{0,-1},{0,1},{1,0}} , total; 


int Solve(int x,int y) {
	
	// Check Boundaries.
	int& ret = memo[x][y];
	if ( ret != -1 ) return ret;
	
	int val = INF , ans = 0 , t , x1, y1;
	REP(i,4) {
		
		x1 = x + d[i][0]; y1 = y + d[i][1];
		if ( x1 >= 0 && x1 < H && y1 >= 0 && y1 < W ) {

			t = Inp[x1][y1];
			if ( val > t ) { val = t; ans = i; }
		}
	}
	if ( val >= Inp[x][y] ) ret = total++;
	else {	
		ret = Solve(x + d[ans][0], y + d[ans][1]);
	}
	return ret;
}

int main() {
	
	int kases;scanf("%d",&kases);
	REP(v,kases) {

		scanf("%d%d",&H,&W);		
		REP(i,H) REP(j,W) scanf("%d",&Inp[i][j]);

		memset(memo,-1,sizeof memo);
		total = 0;
		
		REP(i,H) REP(j,W) Solve(i,j);

		assert(total <= 26 );
		printf("Case #%d:\n",v+1);
		REP(i,H) REP(j,W) printf("%c%c",'a' + memo[i][j],j == W - 1 ? 10 : 32);
	}
	return 0;
}


