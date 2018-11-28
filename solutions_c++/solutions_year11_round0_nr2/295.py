#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < n; i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define y0 y3487465
#define y1 y8687969

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) {
	re x > 0 ? x : -x;
}

int n;
int m;
char g[255][255];
int op[255][255];
int c, d;

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> c;
		memset (g, 0, sizeof (g));
		for (int j = 0; j < c; j++) {
			string s;
			cin >> s;
			g[s[0]][s[1]] = g[s[1]][s[0]] = s[2];
		}
		cin >> d;
		memset (op, 0, sizeof (op));
		for (int j = 0; j < d; j++) {
			string s;
			cin >> s;
			op[s[0]][s[1]] = op[s[1]][s[0]] = 1;
		}
		cin >> m;
		string s;
		cin >> s;
		string w = "";
		for (int k = 0; k < m; k++) {
			w += s[k];
			while (sz (w) > 1 && g[w[sz (w) - 2]][w[sz (w) - 1]]) {
				char c = g[w[sz (w) - 2]][w[sz (w) - 1]];
				w.erase (sz (w) - 2, 2);
				w += c;
			}
			for (int j = 0; j < sz (w); j++)
				if (op[w[j]][w[sz (w) - 1]]) {
					w = "";
					break;
				}
		}
		cout << "Case #" << i + 1 << ": [";
		for (int j = 0; j < sz (w); j++) {
			cout << w[j];
			if (j + 1 < sz (w)) cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
