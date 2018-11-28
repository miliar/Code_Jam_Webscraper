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

//#include <conio.h>
#define testing 0
int main () {
#ifndef ONLINE_JUDGE
	freopen ( "d.in" , "r" , stdin );
	if (!testing) freopen ( "out.out" , "w" , stdout );
#endif

	int ntest; read(ntest);
	lap(test,ntest) {
		int n; cin >> n;
		double x[55], y[55], r[55];
		lap(i,n) cin >> x[i] >> y[i] >> r[i];

		double res = 1e20;
		lap(i,n) lap(j,n) lap(k,n) {
			if (i != j && i != k && j != k) {
				double d = sqrt(sqr(x[i]-x[j]) + sqr(y[i]-y[j]));
				d += r[i];
				d += r[j];
				
				d /= 2;
				updmax(d, r[k]);
				updmin(res, d);
			}
		}

		if (n == 1) updmin(res, r[0]);
		if (n == 2) updmin(res, max(r[0], r[1]));
		printf("Case #%d: %.6lf\n", test+1, res);
	}

#ifndef ONLINE_JUDGE
	fclose ( stdin );
	fclose ( stdout );
#endif
	return 0;
}
