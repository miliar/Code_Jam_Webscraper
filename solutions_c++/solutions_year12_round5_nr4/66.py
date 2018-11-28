#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, K, N;
string S;
bool adj[40][40], inS[40];
map<char, char> ch;
map<char, int> ind;
string from = "oieastbg", to = "01345789";

int main() {
	N = 26 + sz(to);
	FOR(i, 0, sz(from)) ch[from[i]] = to[i];
	FOR(i, 0, 26) ind['a' + i] = i;
	FOR(i, 0, sz(to)) ind[to[i]] = 26 + i;
	FOR(i, 0, 26) {
		if (ch.find('a' + i) == ch.end()) ch['a' + i] = 'a' + i;
	}
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> K >> S;
		if (K != 2) {
			cout << "fail" << endl;
			continue;
		}
		memset(adj, 0, sizeof(adj));
		memset(inS, 0, sizeof(inS));
		FOR(i, 0, sz(S)) {
			char c = S[i];
			inS[ind[c]] = true;
			inS[ind[ch[c]]] = true;
		}
		FOR(i, 0, sz(S)-1) {
			char c1 = S[i], c2 = S[i+1];
			adj[ind[c1]][ind[c2]] = true;
			adj[ind[ch[c1]]][ind[c2]] = true;
			adj[ind[c1]][ind[ch[c2]]] = true;
			adj[ind[ch[c1]]][ind[ch[c2]]] = true;
		}
		int res = 0;
		FOR(i, 0, N) FOR(j, 0, N) if (adj[i][j]) res++;
		bool diff = false;
		FOR(i, 0, N) {
			int ind = 0, outd = 0;
			FOR(j, 0, N) {
				if (i != j && adj[i][j]) outd++;
				if (i != j && adj[j][i]) ind++;
			}
			if (inS[i] && ind == 0 && outd == 0) res++;
			if (ind > outd) {
				res += (ind - outd);
				diff = true;
			}
		}
		if (!diff) res++;
		cout << "Case #" << cs << ": " << res << endl;
	}
	return 0;
}
