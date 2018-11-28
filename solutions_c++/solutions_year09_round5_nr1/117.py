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

struct state {
	vector <pii> data;
	void sap() {
		sort(data.begin(), data.end());
	}
};

bool operator == (const state &x, const state &y) {return x.data == y.data;}
bool operator < (const state &x, const state &y) {return x.data < y.data;}

map<state,int> M;
deque <state> Q;
int sh, sc;
bool wall[111][111];

void go (int at, state &x, bool vis[]) {
	if (vis[at]) return;
	vis[at] = true;
	lap(i,x.data.size()) if (vis[i] == false) {
		int h1 = x.data[at].first;
		int c1 = x.data[at].second;
		int h2 = x.data[i].first;
		int c2 = x.data[i].second;
		if (abs(h1-h2) + abs(c1-c2) == 1)
			go(i, x, vis);
	}
}

bool connected(state &x) {
	bool vis[5];
	xoa(vis,false);
	go(0, x, vis);
	lap(i,x.data.size()) if (!vis[i]) return false;
	return true;
}

bool valid(int h, int c) {
	return 0 <= h && h < sh && 0 <= c && c < sc && wall[h][c] == false;
}

bool b[111][111];
void sinh (state &a) {
	xoa(b, 0);
	lap(i,a.data.size())
		b[a.data[i].first][a.data[i].second] = 1;

	bool good = connected(a);
	lap(i,a.data.size()) {
		int h = a.data[i].first;
		int c = a.data[i].second;
		
		rep(dh,-1,1) rep(dc,-1,1) if (dh == 0 ^ dc == 0) {
			int nh = h + dh;
			int nc = c + dc;
			int kh = h - dh;
			int kc = c - dc;

			state next = a;
			if (valid(nh,nc) && valid(kh,kc) && b[nh][nc] == 0 && b[kh][kc] == 0) {
				next.data[i] = make_pair(nh,nc);
				bool ok = true;
				if (!good) {
					bool now = connected(next);
					if (!now) ok = false;
				}
				if (!ok) continue;
				next.sap();
				if (M.count(next)) continue;
				M[next] = M[a] + 1;
				Q.push_back(next);
			}
		}
	}
}

int solve (state dau, state cuoi) {
	M.clear();
	M[dau] = 0;
	Q.clear();
	Q.push_back(dau);

	while (!Q.empty()) {
		dau = Q.front();
		Q.pop_front();
		if (dau == cuoi)
			return M[cuoi];
		sinh(dau);
	}
	return -1;
}

//#include <conio.h>
#define testing 0
int main () {
#ifndef ONLINE_JUDGE
	freopen ( "a2.in" , "r" , stdin );
	if (!testing) freopen ( "out.out" , "w" , stdout );
#endif

	int ntest; read(ntest);
	lap(test,ntest) {
		cin >> sh >> sc;

		state dau, cuoi;
		lap(i,sh) lap(j,sc) {
			char ch;
			cin >> ch;
			if (ch == '#') wall[i][j] = true;
			else wall[i][j] = false;
	
			if (ch == 'o' || ch == 'w') 
				dau.data.push_back(make_pair(i,j));
			if (ch == 'x' || ch == 'w')
				cuoi.data.push_back(make_pair(i,j));
		}

		int res = solve(dau, cuoi);
		printf("Case #%d: %d\n", test+1, res);
	}

#ifndef ONLINE_JUDGE
	fclose ( stdin );
	fclose ( stdout );
#endif
	return 0;
}
