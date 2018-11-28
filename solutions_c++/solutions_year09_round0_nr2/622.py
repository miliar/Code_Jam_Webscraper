#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <ctime>
#include <utility>
#include <stdexcept>

using namespace std;

#define inf (1<<30)
#define PB push_back
#define mset(x,a) memset(x,(a),sizeof(x))
#define SIZE(X) ((int)X.size())
#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define rg(x,y) (x=x>y?x:y)
typedef vector<int> VI;
typedef vector<char> VC;
typedef vector<string> VS;
typedef long long LL;
typedef unsigned long long uLL;
#define twoL(X) (((LL)(1))<<(X))
const double PI=acos(-1.0);
const double eps=1e-11;
template <class T> T sqr(T x) {return x*x;}
template <class T> T gcd(T a, T b) {if(a<0) return (gcd(-a,b)); if(b<0) return (gcd(a,-b)); return (b==0)?a:gcd(b,a%b);}
template <class T> T lcm(T a, T b) {return a*b/gcd(a,b);}
LL toLL(string s) { istringstream sin(s); LL t; sin>>t; return t;}
int toInt(string s) {istringstream sin(s); int t; sin>>t; return t;}
string toString(LL v) {ostringstream sout; sout<<v; return sout.str();}
string toString(int v) {ostringstream sout; sout<<v; return sout.str();}
#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) ((x).begin(), (x).end())
#define cross(a, b, c)  ((c).x-(a).x)*((b).y-(a).y)-((b).x-(a).x)*((c).y-(a).y)
#define sq_dist(p, q) ((p).x-(q).x)*((p).x-(q).x)+((p).y-(q).y)*((p).y-(q).y)

int mat[105][105], r, c, h;
int flag[105][105];
int dir[4][2] = { {-1,0},{0,-1},{0,1},{1,0} };

struct point {
    int x, y;
}begin;

int can( point v, point u, int k ) {
	point t;
	int res = inf, fang;
	point p;
    for ( int i = 0; i < 4; ++i ) {
	    t.x = v.x+dir[i][0];
		t.y = v.y+dir[i][1];
		if ( t.x < 0 || t.x >= r || t.y < 0 || t.y >= c )    continue;
		if ( mat[t.x][t.y] < mat[v.x][v.y] ) {
		    if ( mat[t.x][t.y] < res ) {
			    res = mat[t.x][t.y];
				p.x = t.x, p.y = t.y;
                fang = i; 
			}
		}
	}
	if ( res == inf )    return 0;
	if ( fang == k && u.x == p.x && u.y == p.y )    return 1;
	return 0;
}

void bfs() {
    queue<point> q;
	point u, v, u0;
	q.push(begin);
	while ( !q.empty() ) {
		u = q.front();
	    //printf("%d %dok\n", u.x, u.y);
		q.pop();
		int t = inf;
		for ( int i = 0; i < 4; ++i ) {
		    v.x = u.x + dir[i][0];
			v.y = u.y + dir[i][1];
			if ( v.x < 0 || v.x >= r || v.y < 0 || v.y >= c )
				continue;
			if ( mat[v.x][v.y] < mat[u.x][u.y] && mat[v.x][v.y] < t ) {
				t = mat[v.x][v.y];
				u0.x = v.x, u0.y = v.y;
			}
			if ( mat[v.x][v.y] > mat[u.x][u.y] && !flag[v.x][v.y] ) {
			    if ( can(v, u, 3-i) ) 
				{ flag[v.x][v.y] = h;
				  q.push(v);
				}
			}
		}
		if ( t == inf )    continue;
		if ( flag[u0.x][u0.y] )    continue;
		flag[u0.x][u0.y] = h;
		q.push(u0);
	}
}

int main()
{
	freopen("1.txt", "w", stdout);
	int T, cnd = 0;
	cin >> T;
	while ( T-- ) {
	    cin >> r >> c;
		for ( int i = 0; i < r; ++i )
			for ( int j = 0; j < c; ++j )
			    cin >> mat[i][j];
		mset(flag, 0);
		h = 1;
        for ( int i = 0; i < r; ++i )
			for ( int j = 0; j < c; ++j ) {
		        if ( flag[i][j] == 0 ) {   
					flag[i][j] = h;
					begin.x = i, begin.y = j;
					bfs();
					h++;
				}
		    }
		printf("Case #%d:\n", ++cnd);
		for ( int i = 0; i < r; ++i ) {
		    for ( int j = 0; j < c; ++j ) {
				if ( j != (c-1) )
				    printf("%c ", flag[i][j]-1+'a');
				else printf("%c\n", flag[i][j]-1+'a');
			}
		}
	}
	return 0;
}
