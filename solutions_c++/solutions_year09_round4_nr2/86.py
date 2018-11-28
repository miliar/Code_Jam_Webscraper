#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <list>

#define lap(i,n) for ( int i = 0 , _n = (n); i < _n; ++i )
#define rep(i,a,b) for ( int i = (a) , _b = (b); i <= _b; ++i )
#define repd(i,a,b) for ( int i = (a) , _b = (b); i >= _b; --i )
#define lapit(p,c) for ( __typeof ( (c) . begin () ) p = (c) . begin (); p != (c) . end (); ++p )
#define MP make_pair
#define PB push_back
#define LL long long
#define vocung 0x3F3F3F3F
#define xoa(x,w) memset(x,w,sizeof x)
#define all(x) (x).begin(), (x).end()

#define two(i) (1<<(i))
#define getbit(i,n) (((n)>>(i))&1)
#define setbit(i,n,t) ((t)?((n)|(two(i))):((n)&~(two(i))))
#define subset(m,n) (((m)&(n))==(m))
#define F first
#define S second
#define read(a) scanf ( " %d " , & a )
#define read2(a,b) scanf ( " %d %d " , & a , & b )
#define read3(a,b,c) scanf ( " %d %d %d " , & a , & b , & c )
#define read4(a,b,c,d) scanf ( " %d %d %d %d " , & a , & b , & c , & d )
#define out(a) debug && cout<<#a<<": "<<a<<endl;
#define out2(a,b) debug && cout<<"("<<#a<<": "<<a<<"),("<<#b<<": "<<b<<")"<<endl;
#define out3(a,b,c) debug && cout<<"("<<#a<<": "<<a<<"),("<<#b<<": "<<b<<"),("<<#c<<": "<<c<<")"<<endl;
#define out4(a,b,c,d) debug && cout<<"("<<#a<<": "<<a<<"),("<<#b<<": "<<b<<"),("<<#c<<": "<<c<<"),("<<#d<<": "<<d<<")"<<endl;
#define out1d(a,n) {debug && cout<<#a<<": "<<endl; lap(_i,n) debug && cout<<a[_i]<< " "; debug && cout<<endl;}
#define outp1d(a,n) {debug && cout<<#a<<": "<<endl; lap(_i,n) debug && cout<<"("<<a[_i].first<<","<<a[_i].second<<")"<<endl;}
#define out2d(a,sh,sc) {debug && cout<<#a<<": "<<endl; lap(_i,sh) { lap(_j,sc) debug && cout<<a[_i][_j]<<" "; debug && cout<<endl;} }
#define outstl(a) {debug && cout<<#a<<": "<<endl; lapit(it,a) debug && cout<<*it<<" "; debug && cout<<endl;}
#define outpstl(a) {debug && cout<<#a<<": "<<endl; lapit(it,a) debug && cout<<"("<<it->first<<","<<it->second<<")"<<endl;}
#define getRand(n) (((rand()<<16)+rand())%(n))
#define sqr(x) ((x)*(x))
#define abs(x) ((x)>0?(x):-(x))
#define sqrt(x) (sqrt((double)(x)))
#define debug true
template <class T, class U> void updmax(T &w, U n) {if (n > w) w = n;}
template <class T, class U> void updmin(T &w, U n) {if (n < w) w = n;}
using namespace std;
typedef pair <int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int sh, sc, maxFall;
int a[55][55], hang[55];

int f[two(6)][two(6)][55][55];

set <pair<int,pair<pii,pii> > > tap;

pair<pii,pii> state(int cur, int below, int h, int c) {
	return make_pair(make_pair(cur,below), make_pair(h,c));
}
int solve () {
	xoa(f, vocung);
	f[hang[0]][hang[1]][0][0] = 1;
	tap.clear();
	tap.insert(make_pair(0, state(hang[0], hang[1], 0, 0)));
	while (!tap.empty()) {
		int cur = tap.begin()->second.first.first;
		int below = tap.begin()->second.first.second;
		int h = tap.begin()->second.second.first;
		int c = tap.begin()->second.second.second;
		tap.erase(tap.begin());

		int cost = f[cur][below][h][c];
		if (h == sh-1) return f[cur][below][h][c];

		rep(c2,c-1,c+1) if (c2 != c && 0 <= c2 && c2 < sc && getbit(c2,cur) == 0) {
			int newh = sh-1;
			rep(nh,h+1,sh-1) {
				int co = false;
				if (nh == h+1) co = getbit(c2,below);
				else co = a[nh][c2];
				if (co) {
					newh = nh - 1;
					break;
				}
			}
			if (newh - h <= maxFall) {
				int ncur, nbelow;
				if (newh == h) {
					ncur = cur;
					nbelow = below;
				}
				else if (newh == h+1) {
					ncur = below;
					nbelow = hang[newh + 1];
				}
				else {
					ncur = hang[newh];
					nbelow = hang[newh + 1];
				}
				if (f[ncur][nbelow][newh][c2] > cost) {
					tap.erase(make_pair(f[ncur][nbelow][newh][c2], state(ncur, nbelow, newh, c2)));
					f[ncur][nbelow][newh][c2] = cost;
					tap.insert(make_pair(f[ncur][nbelow][newh][c2], state(ncur, nbelow, newh, c2)));
				}
			}
		}

		rep(c2,c-1,c+1) if (c2 != c && 0 <= c2 && c2 < sc && getbit(c2,cur) == 0 && getbit(c2,below) == 1) {
			int ncur = cur;
			int nbelow = setbit(c2,below,0);
			if (f[ncur][nbelow][h][c] > cost + 1) {
				tap.erase(make_pair(f[ncur][nbelow][h][c], state(ncur, nbelow, h, c)));
				f[ncur][nbelow][h][c] = cost + 1;
				tap.insert(make_pair(f[ncur][nbelow][h][c], state(ncur, nbelow, h, c)));
			}
		}
	}
	return vocung;
}
//#include <conio.h>
#define testing 0
int main () {
#ifndef ONLINE_JUDGE
	freopen ( "b.in" , "r" , stdin );
	if (!testing) freopen ( "out.out" , "w" , stdout );
#endif

	int ntest; read(ntest);
	lap(test,ntest) {
		cin >> sh >> sc >> maxFall;
		lap(i,sh) lap(j,sc) {
			char ch; cin >> ch;
			if (ch == '#') a[i][j] = 1;
			else a[i][j] = 0;
		}

		xoa(hang, 0);
		lap(i,sh) lap(j,sc) if (a[i][j]) 
			hang[i] = setbit(j,hang[i],1);

		int res = solve();
		if (res == vocung) {
			printf("Case #%d: No\n", test+1);
		}
		else printf("Case #%d: Yes %d\n", test+1, res - 1);
	}

#ifndef ONLINE_JUDGE
	fclose ( stdin );
	fclose ( stdout );
#endif
	return 0;
}
