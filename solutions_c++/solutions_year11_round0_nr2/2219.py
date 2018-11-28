#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#include <ext/hash_set>
using namespace __gnu_cxx;

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)

int dx[] = { 0, -1, 0, 1, -1, -1, 1, 1 };
int dy[] = { -1, 0, 1, 0, 1, -1, -1, 1 };

int c[30][30];
bool d[30][30];

int main() {
	freopen("B.in", "rt", stdin);
	freopen("B.out","wt",stdout);
	int T, C, D, N;
	string s;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(d));
		cin >> C;
		for (int i = 0; i < C; ++i) {
			cin >> s;
			c[s[0] - 'A'][s[1] - 'A'] = c[s[1] - 'A'][s[0] - 'A'] = s[2];
		}
		cin >> D;
		for (int i = 0; i < D; ++i) {
			cin >> s;
			d[s[0] - 'A'][s[1] - 'A'] = d[s[1] - 'A'][s[0] - 'A'] = 1;
		}
		cin >> N >> s;
		string curS = s.substr(0, 1);

		for (int i = 1; i < N; ++i) {
			if (curS == "")
				curS += s[i];
			else {
				char ch = curS[curS.size() - 1];
				if (c[s[i] - 'A'][ch - 'A'] != 0) {
					curS = curS.substr(0, curS.size() - 1);
					curS += c[s[i] - 'A'][ch - 'A'];
				} else {
					bool flag = 0;
					for (int j = 0; j < curS.size(); j++) {
						if (d[curS[j] - 'A'][s[i] - 'A'])
							curS = "", flag = true;
					}
					if (!flag)
						curS += s[i];
				}
			}
		}
		printf("Case #%i: [", t + 1);
		for (int i = 0; i < curS.size(); i++) {
			if (i)
				printf(", ");
			printf("%c", curS[i]);
		}
		printf("]\n");
	}
	return 0;
}
