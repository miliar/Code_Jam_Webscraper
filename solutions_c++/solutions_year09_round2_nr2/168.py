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
#define out(x) debug && cout << #x << ": " << (x) << endl;
#define out2(x,y) debug && cout << "(" << #x << ": " << (x) << ") , (" << #y << ": " << (y) << ")" << endl;
#define out3(x,y,z) debug && cout << "(" << #x << ": " << (x) << ") , (" << #y << ": " << (y) << ") , (" << #z << ": " << (z) << ")" << endl;
#define out4(x,y,z,w) debug && cout << "(" << #x << ": " << (x) << ") , (" << #y << ": " << (y) << ") , (" << #z << ": " << (z) << ") , (" << #w << ": " << (w) << ")" << endl;
#define outstl(a) {debug && cout << #a << " . size () = " << (a) . size () << endl; lapit ( it , a ) debug && cout << *it << " "; debug && cout << endl;}
#define outmap(a) {debug && cout << #a << " . size () = " << (a) . size () << endl; lapit ( it , a ) debug && cout << #a << " [ " << it -> first << " ] = " << it -> second << endl;}
#define out1d(a,n) {debug && cout << #a << ":"; lap ( _i , n ) debug && cout << " " << (a)[ _i ]; debug && cout << endl;}
#define outpair1d(a,n) {debug && cout << #a << ":" << endl; lap ( _i , n ) out2 ( a[_i].first , a[_i]. second );}
#define out2d(a,sh,sc) {debug && cout << #a << ": " << endl; lap ( _i , sh ) { lap ( _j , sc ) debug && cout << (a) [ _i ] [ _j ] << " "; debug && cout << endl;}}
#define getRand(n) (((rand()<<16)+rand())%(n))
#define debug true
using namespace std;
typedef pair <int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
template <class T, class U> void updmax(T &w, U n) {if (n > w) w = n;}
template <class T, class U> void updmin(T &w, U n) {if (n < w) w = n;}

//#include <conio.h>

string s;

string stupid () {
	return "";
}

string solve(string s) {
	if (!next_permutation(s.begin(), s.end())) {
		sort(s.begin(), s.end());
		string t;
		while (s[0] == '0') {
			t += '0';
			s.erase(0,1);
		}
		t += '0';
		s.insert(1,t);
	}
	return s;
}

#define testing 0
int main () {
#ifndef ONLINE_JUDGE
	freopen ( "b2.in" , "r" , stdin );
	if (!testing) freopen ( "out.out" , "w" , stdout );
#endif

	int ntest; read(ntest);
	lap(test,ntest) {
		cin >> s;
		string r = solve(s);
		printf("Case #%d: %s\n", test+1, r.c_str());
	}

#ifndef ONLINE_JUDGE
	fclose ( stdin );
	fclose ( stdout );
#endif
	return 0;
}
