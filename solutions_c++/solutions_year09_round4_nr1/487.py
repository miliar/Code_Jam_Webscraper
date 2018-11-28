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

//#define INF 1000000000

//#define ll long long int
//#define INF ( ((ll)1) << 60 )


//////////////////////////////// GRAPHS ///////////////////////////////

//int di[] = {-1,0,1,0   ,   -1,1,1,-1};
//int dj[] = {0,1,0,-1   ,   1,1,-1,-1};

//#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < n )   // square
//#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < m )   // rectangular



//////////////////////////////// GEOMETRY//////////////////////////////

//#define mpi 3.1415926535897932384626433832795


//////////////////////////////// STRINGS ///////////////////////////////

//inline bool isc ( char c ) { return ( 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' ); }
//inline bool isd ( char c ) { return '0' <= c && c <= '9'; }
//inline char tol ( char c ) { if ( 'A' <= c && c <= 'Z' ) c = c - 'A' + 'a'; return c; }
//inline char tou ( char c ) { if ( 'a' <= c && c <= 'z' ) c = c - 'a' + 'A'; return c; }

#define N 50

char s[N][N];
int n, a[N];




inline bool check(vector < int > & A) {
	for (int i = 0; i < n; ++i) if (A[i] > i) return false;
	return true;
}

int f ( vector < int > A ) {
	int i, j, k, res = 0;
	while (!check(A)) {
		for (i = 0; i < n; ++i) if (A[i] > i) {
			for (j = i+1; j < n; ++j) if (A[j] <= i) {
				break;
			}
			while (j > i) {
				swap(A[j], A[j-1]);
				--j;
				++res;
			}
		}
	}
	return res;
}

int main () {
	int i, j, CAS;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {

		scanf("%d", &n);
		for (i = 0; i < n; ++i) scanf("%s", s[i]);

		for (i = 0; i < n; ++i) {
			a[i] = -1;
			for (j = 0; j < n; ++j) {
				if (s[i][j] == '1') a[i] = j;
			}
		}

		vector < int > A(a, a+n);

		int res = f(A);
		
		printf("Case #%d: %d\n", cas, res);
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


