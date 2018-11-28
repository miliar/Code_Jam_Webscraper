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

#define N 5000000
#define M 111

char s[1000000];
int L, an;
string S;
set < string > ft[M];
string animals[M];


/////////////

class NODE { public:
	double p;
	string feature;
	int left, right;
} a[N];
int last = 0;

string B[N];
int bn = 0, pos = 0;

void process ( int cur ) {

	if (B[pos] != "(") throw 0;
	++pos;

	double P;

	sscanf(B[pos].c_str(), "%lf", &P);

	a[cur].p = P;
	++pos;

	if (B[pos] == ")") {
		a[cur].feature = "";
		++pos;
		return;
	}

	a[cur].feature = B[pos];
	++pos;

	a[cur].left = last++;
	process(a[cur].left);

	a[cur].right = last++;
	process(a[cur].right);

	if (B[pos] != ")") throw 0;
	++pos;

}

/////////////

double f ( int ind ) {
	double res = 1.0;
	int pos = 0;

	for (pos = 0; ; ) {
		res *= a[pos].p;

		if (a[pos].feature == "") break;

		if (ft[ind].find( a[pos].feature ) != ft[ind].end()) {
			pos = a[pos].left;
		}
		else {
			pos = a[pos].right;
		}
	}

	return res;
}


int main () {
	int i, j, CAS, x, y;

	gets(s);
	sscanf(s, "%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {

		S = "";
		S.clear();
		last = 0;
		bn = 0;
		pos = 0;

		gets(s);
		sscanf(s, "%d", &L);

		string S1;

		for (i = 0; i < L; ++i) {
			gets(s);
			S1 += " ";
			S1 += s;
		}

		for (i = 0; i < S1.length(); ++i) {
			if (S1[i] == ')' || S1[i] == '(') {
				S += " ";
				S += S1[i];
				S += " ";
			}
			else {
				S += S1[i];
			}
		}

		stringstream sss(S);
		string token;

		while (sss >> token) {
			B[bn++] = token;
		}

		last = 1;
		process(0);

		/////////////////////

		gets(s);
		sscanf(s, "%d", &an);

		for (i = 0; i < an; ++i) ft[i].clear();

		printf("Case #%d:\n", cas);

		for (i = 0; i < an; ++i) {

			gets(s);
			stringstream ss( s );
			ss >> animals[i];
			ss >> y;

			while (y--) {
				string temp;
				ss >> temp;
				ft[i].insert(temp);
			}

			//process animal

			double res = f(i);

			printf("%.8lf\n", res);

		}
		
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


