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

#define sqr(x) (x)*(x)
#define two(i) (1<<(i))
#define getbit(i,n) (((n)>>(i))&1)
#define setbit(i,n,t) ((t)?((n)|(two(i))):((n)&~(two(i))))
#define subset(m,n) (((m)&(n))==(m))
#define F first
#define S second
#define pi M_PI
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
#define debug true
template <class T, class U> void updmax(T &w, U n) {if (n > w) w = n;}
template <class T, class U> void updmin(T &w, U n) {if (n < w) w = n;}
using namespace std;
typedef pair <int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

#define maxn 111
int a[maxn][maxn], num[maxn][maxn], sh, sc, cnt;
const int dh[] = {-1,0,0,1};
const int dc[] = {0,-1,1,0};

int go(int h, int c) {
	if (num[h][c] != -1) return num[h][c];
	int amin = vocung, rd = -1;
	lap(d, 4) {
		int nh = h + dh[d], nc = c + dc[d];
		if (0 <= nh && nh < sh && 0 <= nc && nc < sc && a[h][c] > a[nh][nc]) {
			if (a[nh][nc] < amin) {
				amin = a[nh][nc];
				rd = d;
			}
		}
	}
	if (amin == vocung) num[h][c] = cnt++;
	else num[h][c] = go(h + dh[rd], c + dc[rd]);
	return num[h][c];
}

int ind[maxn];

int main() {
#ifndef ONLINE_JUDGE
    freopen("b2.in", "r", stdin);
    freopen("out.out", "w", stdout);
#endif

    int ntest; cin >> ntest;
    lap(test,ntest) {
    	cin >> sh >> sc;
    	lap(i,sh) lap(j,sc) cin >> a[i][j];
    	xoa(num,-1);
    	cnt = 0;
    	lap(i,sh) lap(j,sc) if (num[i][j] == -1) go(i,j);

    	printf("Case #%d:\n", test+1);
    	xoa(ind, -1);
    	int cur = 0;
    	lap(i,sh) {
    		lap(j,sc) {
    			if (j) printf(" ");
    			if (ind[num[i][j]] == -1)
    				ind[num[i][j]] = cur++;
    			printf("%c", 'a' + ind[num[i][j]]);
    		}
    		printf("\n");
    	}
    }

#ifndef ONLINE_JUDGE
    fclose(stdin);
    fclose(stdout);
#endif
    return 0;
}
