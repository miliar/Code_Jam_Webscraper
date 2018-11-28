#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

#define SZ(x) (int)(x).size()
#define FOR(i, seq, n) for(int i = (seq); i < (n); ++i)
#define FORD(i, seq, n) for(int i = (seq); i >= (n); --i)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define REPD(i, n) for(int i = (n) - 1; i >= 0; --i)
#define ALL(x) (x).begin(), (x).end()
#define SQR(x) (x)*(x)
typedef unsigned long long u64;
typedef signed long long i64;
typedef pair<int, int> pii;
#define X first
#define Y second
#define pb push_back

bool check(char a, char b, char x, char y)
{
	return a == x && b == y || a == y && b == x;
}

int main()
{
	int T; cin >> T;
	REP (t, T) {
		int C; cin >> C;
		vector<string> comb;
		REP (i, C) { string tmp; cin >> tmp; comb.pb(tmp); }
		int D; cin >> D;
		vector<string> opp;
		REP (i, D) { string tmp; cin >> tmp; opp.pb(tmp); }

		int N;
		string inp;
		cin >> N >> inp;

		vector<char> list;

		REP (i, N) {
			list.pb(inp[i]);
			bool v = false;
			while (true) {
				bool a = false;
				if (list.size() >= 2)
				{
					int k = list.size() - 1;
					REP (j, C) if (check(list[k], list[k - 1], comb[j][0], comb[j][1])) {
						list.pop_back();
						list.pop_back();
						list.pb(comb[j][2]);
						a = true;
						v = true;
						break;
					}
				}
				if (!a) break;
			}

			if (!v && list.size() >= 2)
				REP (j, D) REP (k, list.size() - 1)
					if (check(list[k], inp[i], opp[j][0], opp[j][1])) {
							list.clear();
							goto stop;
					}
stop:;
		}

		cout << "Case #" << (t + 1) << ": [";
		REP (i, list.size()) cout << (i ? ", " : "") << list[i];
		cout << "]" << endl;
	}
	return 0;
}
