#include "cstdlib"
#include "cctype"
#include "cstring"
#include "cstdio"
#include "cmath"
#include "algorithm"
#include "vector"
#include "string"
#include "iostream"
#include "sstream"
#include "set"
#include "queue"
#include "stack"
#include "fstream"
#include "iomanip"
#include "bitset"
#include "list"
#include "ctime"
#include "map"
using namespace std;

typedef long long				LL;
typedef unsigned long long		ULL;
typedef unsigned char			uchar;
typedef vector <string>			vs;
typedef vector <int>			vi;
#define CC(m,what)				memset(m,what,sizeof(m))
#define FOR(i,a,b)				for( i = (a); i < (b); ++i )
#define FF(i,a)					for( i = 0; i < (a); ++i )
#define FFD(i,a)				for( i = (a)-1; i >= 0; --i )
#define FORD(i,a,b)				for( i = (a)-1; i >= (b); --i )
#define ll(a)					((a)<<1)
#define rr(a)					(((a)<<1)+1)
#define sz(a)					((int)a.size())
#define PP(n,m,a)				puts("---");FF(i,n){FF(j,m)printf("%10d", a[i][j]);puts("");}
const double eps = 1e-11;
const double Pi = acos(-1.0);

class node {
public:
	map<string, int> son;
} *root;

int		res, n, m;
string	s, dir;

void maketree() {
	node *p = root, *next;
	int i, j, k;
	j = k = 0;
	FF (i, sz(s)) {
		if ( s[i] == '/' ) {
			if ( k != 0 ) {
				dir = s.substr(j, k);
				if ( p->son.count(dir) ) {
					next = (node *)p->son[dir];
				} else {
					next = new node();
					p->son[dir] = (int)next;
				}
				p = next;
			}
			j = i+1;
			k = 0;
		} else ++k;
	}
	if ( k != 0 ) {
		dir = s.substr(j, k);
		if ( p->son.count(dir) ) {
			next = (node *)p->son[dir];
		} else {
			next = new node();
			p->son[dir] = (int)next;
		}
		p = next;
	}
}

void sureres() {
	node *p = root, *next;
	int i, j, k;
	j = k = 0;
	FF (i, sz(s)) {
		if ( s[i] == '/' ) {
			if ( k != 0 ) {
				dir = s.substr(j, k);
	//			cout << dir << endl;
				if ( p->son.count(dir) ) {
					next = (node *)p->son[dir];
				} else {
					++res;
					next = new node();
					p->son[dir] = (int)next;
				}
				p = next;
			}
			j = i+1;
			k = 0;
		} else ++k;
	}
	if ( k != 0 ) {
		dir = s.substr(j, k);
	//	cout << dir << endl;
		if ( p->son.count(dir) ) {
			next = (node *)p->son[dir];
		} else {
			++res;
			next = new node();
			p->son[dir] = (int)next;
		}
		p = next;
	}
}

void clearroot(node *root) {
	if ( !root ) return;
	for ( map<string, int>::iterator ix = root->son.begin(); ix != root->son.end(); ++ix) {
		clearroot((node *)ix->second);
	}
	root->son.clear();
	delete root;
}

void hexie() {
	res = 0;
	scanf("%d%d", &n, &m);
	root = new node();
	root->son.clear();
	while ( n-- ) {
		cin >> s;
		maketree();
	}
	while ( m-- ) {
		cin >> s;
		sureres();
	}
	clearroot(root);
}

int main() {
	int T;
	freopen("E:\\OwnCode\\c++\\acm\\in.txt","r",stdin);
	freopen("E:\\OwnCode\\c++\\acm\\data.out","w",stdout);
	scanf("%d", &T);
	for ( int i = 1; i <= T; ++i ) {
		hexie();
		printf("Case #%d: %d\n", i, res);
	}
}

