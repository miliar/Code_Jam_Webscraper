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

string dt[5010];
bool table[20][200];
char buffer[501];

int main()
{
	int L, D, T;
	fscanf(in, "%d %d %d\n", &L, &D, &T);

	
	REP(i, D) {
		fgets(buffer, 20, in);
		buffer[strlen(buffer)-1] = 0;
		dt[i] = buffer;
	}
	//REP(i, D)	cout << "XX" << dt[i] << "YY" << endl;



	FOR(tc, 1, T) {
		fprintf(out, "Case #%d: ", tc);

		fgets(buffer, 500, in);
		int bufn = strlen(buffer);
		if(buffer[bufn-1]=='\n'){ buffer[bufn-1] = 0; bufn--; }

		CLR(table, false);
		int nn = 0, state = 0;
		REP(i, bufn) {
			char x = buffer[i];
			if(x=='(')	state = 1;
			else if(x==')')	{ state =0; nn++; }
			else {
				table[nn][x] = true;
				if(state==0)	nn++;
			}
		}

		int sol = 0;

		REP(i, D) {
			bool flag = false;
			REP(j, L) {
				if(!table[j][dt[i][j]]) { flag = true; break; }
			}
			if(!flag)	sol++;
		}

		fprintf(out, "%d\n", sol);
	}

	return 0;
}