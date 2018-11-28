//#pragma comment(linker, "/STACK:100000000")

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a) : (-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))
#define UNIQUE(p) sort(ALL(p)), p.resize( (int)(unique(ALL(p)) - p.begin()) )

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second

#define INF 1000000000


//////////////////////////////// GRAPHS ///////////////////////////////

int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};

#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < m )   // rectangular

//////////////////////////////// STRINGS ///////////////////////////////

//inline bool isc ( char c ) { return ( 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' ); }
//inline bool isd ( char c ) { return '0' <= c && c <= '9'; }
//inline char tol ( char c ) { if ( 'A' <= c && c <= 'Z' ) c = c - 'A' + 'a'; return c; }
//inline char tou ( char c ) { if ( 'a' <= c && c <= 'z' ) c = c - 'a' + 'A'; return c; }

int n, m;

#define N 111
#define M 12321

int a[N][N];

int rank[M], parent[M];

inline void init() {
	for (int i = 0; i < M; i++) {
		parent[i] = i;
		rank[i] = 0;
	}
}

inline int mfind(int x) {
	if (x != parent[x]) parent[x] = mfind(parent[x]);
	return parent[x];
}

inline void munion(int x, int y) {
	x = mfind(x), y = mfind(y);
	if (x == y) return;

	if (rank[x] > rank[y]) {
		parent[y] = x;
	}
	else {
		parent[x] = y;
		if (rank[x] == rank[y]) rank[y]++;
	}
}

char res[N][N];

int main () {
	int i, j, k, CAS;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {

		mset(a,0);
		init();
		mset(res,0);

		scanf("%d%d", &n, &m);

		for (i = 0; i < n; ++i) for (j = 0; j < m; ++j) scanf("%d", &a[i][j]);

		for (i = 0; i < n; ++i) for (j = 0; j < m; ++j) {
			int r = a[i][j], ri = -1;
			for (k = 0; k < 4; ++k) {
				int ii = i+di[k], jj = j+dj[k];
				if (inr(ii,jj) && r > a[ii][jj]) {
					r = a[ii][jj];
					ri = k;
				}
			}
			if (ri != -1) {
				munion( i*m + j, (i+di[ri])*m + j+dj[ri] );
			}
		}

		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				mfind(i*m+j);
			}
		}

		map < int , char > A;
		char last = 'a';

		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				if (A.find( parent[i*m+j] ) != A.end()) {
					res[i][j] = A[ parent[i*m+j] ];
				}
				else {
					res[i][j] = last;
					A[ parent[i*m+j] ] = last;
					++last;
				}
			}
		}


		printf("Case #%d:\n", cas);

		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				printf("%c%c", res[i][j], (j==m-1?'\n':' '));
			}
		}
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


