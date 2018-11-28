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

double toDouble(const string& s)
{
	stringstream in(s);
	double ret;
	in >> ret;
	return ret;
}

VS jr;
char des[16000];
char line[2000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d:\n", tc);
	
		CLR(des, 0);
		int idx = 0;
		int L;
		scanf("%d\n", &L);
		while(L--) {
			gets(line);
			int len = strlen(line);
			REP(i, len) {
				int x = line[i];
				if(x=='\n') { des[idx++] = ' '; continue; }
				else if(x=='(') { des[idx++] = x; des[idx++] = ' '; }
				else if(x==')') { des[idx++] = ' '; des[idx++] = x; }
				else	des[idx++] = x;
			}
			des[idx++] = ' ';
		}
		des[idx++] = 0;

		jr.clear();
		char *p = strtok(des, " ");
		while(p!=NULL) { //loop
			jr.pb(p);
			p = strtok(NULL, " ");
		}
		
		int A;
		scanf("%d\n", &A);
		while(A--) {
			gets(line);
			MSI db;
			char *p = strtok(line, " ");
			int ii = 0;
			while(p!=NULL) {
				ii++;
				if(ii>=3) {
					string s = p;
					db[s] = 1;
				}
				p = strtok(NULL, " ");
			}

			double sol = 1.f;

			int que = 0;
			bool start = true, flag = false;
			REP(ii, jr.size()) {
				string p = jr[ii];
				if(start) {
					que++;
					start = false;
					continue;
				}
				if(que==0)	break;
				if(flag) { // find no
					if(p=="(") {
						que++;
					}
					else if(p==")") {
						que--;
					}
					if(que==0) {
						flag = false;
						que = 0;
						start = true;
					}
					continue;
				}

				if(p=="(") {
					que++;
				}
				else if(p==")") {
					que--;
				}
				else if(p[0]=='0' || p[0]=='1') { //poss
					sol *= toDouble(p);
				}
				else { //letter
					if(db.find(p)!=db.end()) { //yes
					}
					else {//no
						flag = true;
					}
					que = 0;
					start = true;
				}

			}

			printf("%lf\n", sol);
		}
		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}