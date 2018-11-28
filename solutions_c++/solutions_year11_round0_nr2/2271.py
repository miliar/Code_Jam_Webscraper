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

char str[1000], S[1000];

void CheckCombine(string &s, vector < string > & combine)
{
	int l = s.length();
	if (l < 2) return;
	for (int i = 0; i < combine.size(); ++i)
	{
		if (s[l-2] == combine[i][0] && s[l-1] == combine[i][1] ||
			s[l-2] == combine[i][1] && s[l-1] == combine[i][0])
		{
			s.erase(l-2, 2);
			s += combine[i][2];
			return;
		}
	}
}

void CheckOpposed(string &s, vector < string > & opposed)
{
	int l = s.length();
	for (int i = 0; i < opposed.size(); ++i)
	{
		int A = false, B = false;
		for (int j = 0; j < l; ++j)
		{
			if (s[j] == opposed[i][0]) A = true;
			if (s[j] == opposed[i][1]) B = true;
		}
		if (A && B)
		{
			s.clear();
			return;
		}
	}
}

int main () {
	int i, j, CAS;
	int C, D, n;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		vector < string > combine, opposed;

		scanf("%d", &C);
		for (int i = 0; i < C; ++i) scanf("%s", str), combine.push_back(str);

		scanf("%d", &D);
		for (int i = 0; i < D; ++i) scanf("%s", str), opposed.push_back(str);

		scanf("%d", &n);
		scanf("%s", S);
		string s = "";

		for (int symb = 0; S[symb]; ++symb)
		{
			s += S[symb];
			CheckCombine(s, combine);
			CheckOpposed(s, opposed);
		}
		
		printf("Case #%d: [", cas);
		for (int i = 0; i < s.size(); ++i)
		{
			printf("%c%s", s[i], i+1 == s.size() ? "" : ", ");
		}
		printf("]\n");

		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


