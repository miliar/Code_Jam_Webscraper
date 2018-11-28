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

template <class T> void parse (vector <T> &res, string s, string delim = " " ) {
	lap(i, s.size()) if (delim.find(s[i]) != string::npos) s[i] = ' ';
	istringstream in(s);
	T what;	res.clear();
	while (in>>what) res.push_back(what);
}

template <class T> void sto (T &res, string s) {
	istringstream in(s);
	in>>res;
}

template <class T> string tos (T what) {
	ostringstream out;
	out<<what;
	return out.str();
}

#define maxn 8888
int parent[maxn], cntNode;
vector<int> next[maxn];
double node[maxn];
string trait[maxn];
bool isLeaf[maxn];

void getTree (string s) {
	lap(i,maxn) next[i].clear();
	parent[0] = -1;
	xoa(isLeaf, false);

	string t;
	lap(i, s.size()) {
		if (i - 1 > 0 && (s[i-1] == '(' || s[i-1] == ')'))
			t += ' ';
		if (s[i] == '(' || s[i] == ')') 
			t += ' ';
		t += s[i];
	}
	s = t;

	//int cur = -1;
	//while ((cur = s.find('(')) != string::npos) {
	//	s.insert(cur+1, " ");
	//	s.insert(cur, " ");
	//}
	//while ((cur = s.find(')')) != string::npos) {
	//	if (cur + 1 < s.size())
	//		s.insert(cur+1, " ");
	//	s.insert(cur, " ");
	//}

	vector<string> a; parse(a, s);
	int at = -1;
	cntNode = 0;
	lap(i, a.size()) {
		if (a[i][0] == '(') {
			if (at == -1) {
				at = 0;
				cntNode++;
			}
			else {
				int nextAt = cntNode++;
				next[at].push_back(nextAt);
				parent[nextAt] = at;
				at = nextAt;
			}
			++i;
			sto(node[at], a[i]);
			if (i + 1 < a.size() && a[i+1][0] != ')') {
				isLeaf[at] = false;
				++i;
				trait[at] = a[i];
			}
			else
				isLeaf[at] = true;
		}
		else
			if (a[i][0] == ')')
				at = parent[at];
	}
}

set<string> have;
double answer () {
	int at = 0;
	double res = 1;
	while (1) {
		res *= node[at];
		if (isLeaf[at]) break;
		else {
			if (have.count(trait[at])) 
				at = next[at][0];
			else
				at = next[at][1];
		}
	}
	return res;
}
//#include <conio.h>
#define testing 0
int main () {
#ifndef ONLINE_JUDGE
	freopen ( "a2.in" , "r" , stdin );
	if (!testing) freopen ( "out.out" , "w" , stdout );
#endif

	int ntest; cin >> ntest;
	lap(test,ntest) {
		int L; cin >> L;
		string s, c;
		getline(cin, s);
		lap(i, L) {
			getline(cin, c);
			s += " " + c;
		}
		getTree(s);

		printf("Case #%d:\n", test+1);
		int nQuery;	cin >> nQuery;
		lap(lan, nQuery) {
			string s; cin >> s;
			int cnt; cin >> cnt;
			have.clear();
			lap(i, cnt) {
				cin >> s;
				have.insert(s);
			}
			double r = answer();
			printf("%.7lf\n", r);
		}
	}

#ifndef ONLINE_JUDGE
	fclose ( stdin );
	fclose ( stdout );
#endif
	return 0;
}
