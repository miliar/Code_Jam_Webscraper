#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<=(b); i++)
#define FORD(i, b, a) for(int i=(b); i>=(a); i--)
#define FORE(ty, it, data) for(ty::iterator it=data.begin(); it!=data.end(); it++)
#define ALL(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define EPS 1e-10
const double PI = acos(-1.0);

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef map<string, int> MSI;

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }


////////////////////////////////////////////////////////////////////////////////////////////////////////


FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

char B[510];
char *A = "welcome to code jam";
int AN, BN;
int table[22][510];

int main()
{
	AN = strlen(A);
	int T;
	fscanf(in, "%d\n", &T);
	FOR(tc, 1, T) {
		fprintf(out, "Case #%d: ", tc);

		fgets(B, 505, in);
		BN = strlen(B);
		if(B[BN-1]=='\n') { B[BN-1] = 0; BN--; }

		CLR(table, 0);
		table[0][0] = (A[0] == B[0])?1:0;
		FOR(j, 1, BN)	table[0][j] = table[0][j-1] + ((A[0]==B[j])?1:0);
		FOR(i, 1, AN) {
			table[i][0] = 0;
			FOR(j, 1, BN) {
				table[i][j] = table[i][j-1] + ((A[i]==B[j])?table[i-1][j-1]:0);
				table[i][j] %= 10000;
			}
		}
/*
		REP(i, AN) {
			REP(j, BN) {
				printf("%d ", table[i][j]);
			}
			printf("\n");
		}
*/
		fprintf(out, "%04d\n", table[AN-1][BN-1]);
	}

	return 0;
}