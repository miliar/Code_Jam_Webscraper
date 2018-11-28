#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

//#define debug

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long lint;

const int inf = 0x7fffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 20000;

char buffer[Size];

int n, m;

vector<string> ar;
const int size = 10100;

int dp[size][27];

void fillDp() {
	For(i, 0, sz(ar)) {
		string s = ar[i];
		For(j, 0, 26) {
			lint res = 0;
			lint p = 1;
			For(k, 0, sz(s)) {
				if(s[k] == j + 'a') {
					res += p * 1;
				}
				p <<= 1;
			}
			dp[i][j] = res;
		}
		dp[i][26] = sz(s);
	}
}


string getRes(string list) {
	map<int, vector<pii> > tm;
	For(i, 0, n) {
		if(tm.count(dp[i][26]) == 0)
			tm[dp[i][26]] = vector<pii>();
		tm[dp[i][26]].pb(mp(i, 0));
	}
	vector<vector<pii> > m;
	for(map<int, vector<pii> >::iterator it = tm.begin(); it != tm.end(); it++) {
		m.pb(it->second);
	}

	vector<vector<pii> > temp;
	For(i, 0, sz(list)) {
		temp.clear();
		int  c = list[i] - 'a';
		For(i, 0, sz(m)) {
			tm.clear();
			vector<pii> &v = m[i];
			For(i, 0, sz(v)) {
				int t = v[i].first;
				int val = v[i].second;
				if(tm.count(dp[t][c]) == 0)
					tm[dp[t][c]] = vector<pii>();
				tm[dp[t][c]].pb(mp(t, val));
			}
			for(map<int, vector<pii> >::iterator it = tm.begin(); it != tm.end(); it++) {
				temp.pb(it->second);
				if(sz(tm) > 1 && it->first == 0) {
					For(i, 0, sz(temp.back())) {
						temp.back()[i].second++;
					}
				}
			}
		}
		m = temp;
	/*	For(i, 0, sz(temp)) {
			For(j, 0, sz(temp[i])) {
				cerr << ar[temp[i][j].first] << " " << temp[i][j].second << endl;
			}
			cerr << "------" << endl;
		}
		cerr << endl;
*/	}
	int mRes = 0, mI = 0;
	For(i, 0, sz(m)) {
		For(j, 0, sz(m[i])) {
			if(m[i][j].second > mRes) {
				mRes = m[i][j].second;
				mI = m[i][j].first;
			}
			else
				if(m[i][j].second == mRes) {
					mI = min(mI, m[i][j].first);
				}
		}
	}

	return ar[mI];
}

int solution(int nTest) {
	scanf("%d%d", &n, &m);
	ar.clear();
	For(i, 0, n) {
		scanf("%s", buffer);
		ar.pb(buffer);
	}

	fillDp();

	printf("Case #%d: ", nTest + 1);

	For(i, 0, m) {
		scanf("%s", buffer);
		printf("%s", (getRes((string)buffer).c_str()));
		if(i < m - 1)
			printf(" ");
	}
	printf("\n");



	return 1;
}

int main() {
	freopen("input.txt", "r", stdin);
#ifndef debug
	freopen("output.txt", "w", stdout);
#endif

	int i = 0, n = 999999;

	scanf("%d", &n);

	while(i < n && solution(i))
		i++;

	return 0;
}

