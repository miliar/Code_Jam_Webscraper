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

char num[30];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);

		gets(num);
		int N = strlen(num);
		string inp = num;

		reverse(ALL(inp));

		string sol;
		bool succeed = false;
		FOR(i, 1, N-1) {
			int cur = inp[i];
			int best = INT_MAX;
			VI temp;
			REP(j, i) {
				if(inp[j] > cur) {
					best = min(best, (int)inp[j]);
				}
				temp.pb(inp[j]);
			}
			if(best!=INT_MAX) {
				temp.pb(cur);
				sort(ALL(temp));
				inp[i] = best;
				int k = i;
				bool flag = false;
				REP(i, temp.size()) {
					if(!flag && temp[i]==best) {
						flag = true;
						continue;
					}
					inp[--k] = temp[i];
				}
				reverse(ALL(inp));
				succeed = true;
				break;
			}
		}
	
		if(!succeed) {
			VI temp;
			REP(i, inp.size()) {
				temp.pb(inp[i]);
			}
			sort(ALL(temp));
			inp.clear();
			int mem;
			REP(i, temp.size()) {
				if(temp[i]!='0') {
					inp.pb(temp[i]);
					mem = i;
					break;
				}
			}
			inp.pb('0');
			FOR(i, 0, temp.size()-1) {
				if(i==mem)	continue;
				inp.pb(temp[i]);
			}
		}

		cout << inp << endl;
		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}