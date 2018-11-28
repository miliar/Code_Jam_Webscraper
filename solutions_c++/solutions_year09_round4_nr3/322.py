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

int f[two(16)], high[two(16)];

int countBit (int n) {
	int res = 0;
	for (;n;n&=(n-1)) ++res;
	return res;
}

#define testing 0
int main () {
#ifndef ONLINE_JUDGE
	freopen ( "c.in" , "r" , stdin );
	if (!testing) freopen ( "out.out" , "w" , stdout );
#endif

//	int a[111][111];
	vector<int> a[111];
	bool less[111][111];
	int ntest; read(ntest);
	lap(test,ntest) {
		int n, len; read2(n,len);
		lap(i,n) a[i].resize(len);
		lap(i,n) lap(j,len) read(a[i][j]);
		sort(a,a+n);

		xoa(less,0);
		lap(i,n) lap(j,n) if (i != j) {
			less[i][j] = true;
			lap(k, len) if (a[i][k] >= a[j][k]) less[i][j] = false;
		}
		
		//lap(mask, two(n)) f[mask] = countBit(mask);
		xoa(f, vocung);
		lap(mask, two(n)) {
			int last = -1;
			bool ok = true;
			lap(i,n) if (getbit(i,mask)) {
				if (last != -1) {
					if (!less[last][i]) ok = false;
				}
				last = i;				
				high[mask] = two(last);
			}
			if (ok) {
				//out(mask);
				f[mask] = 1;
			}
		}
		lap(mask, two(n)) if (f[mask] == vocung) {
			for (int sub = mask; sub & high[mask]; sub = (sub - 1) & mask) {
				int other = mask ^ sub;
				updmin(f[mask], f[sub] + f[other]);
			}
		}
		printf("Case #%d: %d\n", test+1, f[two(n)-1]);
	}

#ifndef ONLINE_JUDGE
	fclose ( stdin );
	fclose ( stdout );
#endif
	return 0;
}
