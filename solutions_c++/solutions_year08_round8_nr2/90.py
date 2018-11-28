#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

const int nmax = 300, emax = 10000, nemax = nmax * 2 + 2, inf = 1000000000;
map<string, int> mc;
int nc;
struct offer {
	int c, a, b;
} o[nmax + 2];
vector<int> adj[nmax + 2][nmax + 1]; // peec kraasas
bool v[nmax + 2];
int q[nmax + 2], nq;
int d[nmax + 2];
const bool debug = false;

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int n, a, b, i, j, k, l, m, m1, r = inf;
		string t;
		
		mc.clear();
		nc = 0;
		
		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> t >> o[i].a >> o[i].b;
			if (mc.find(t) == mc.end()) mc[t] = nc++;
			o[i].c = mc[t];	
		}
		// jaabuuvee tak grafs
		o[n].c = nc, o[n].a = 0, o[n].b = 0;
		o[n + 1].c = nc, o[n + 1].a = emax + 1, o[n + 1].b = emax + 1;
		for (i = 0; i < n + 2; i++) {
			for (j = 0; j <= nc; j++) adj[i][j].clear();
			for (j = 0; j < n + 2; j++) if (j != i) {
				if (o[j].a <= o[i].b + 1 && o[j].b + 1 >= o[i].a) {
					adj[i][o[j].c].push_back(j);
					if (debug) cout << i << "->" << j << '/' << o[j].c << '\n';
				}
			}
		}
		
		for (i = 0; i < nc; i++) for (j = i; j < nc; j++) for (k = j; k < nc; k++) {
			int ct[4], t;
			ct[0] = i, ct[1] = j, ct[2] = k, ct[3] = nc;
			
			fill(v, v + n + 2, false);
			fill(d, d + n + 2, inf);
			q[0] = n, nq = 1, v[n] = true, d[n] = 0;
			for (l = 0; l < nq; l++) {
				for (m = 0; m < 4; m++) for (m1 = 0; m1 < adj[q[l]][ct[m]].size(); m1++) {
					t = adj[q[l]][ct[m]][m1];
					if (!v[t]++) q[nq++] = t, d[t] = d[q[l]] + 1;
				}
			}
			r = min(r, d[n + 1]);
		}
		
		cout << "Case #" << it << ": ";
		if (r == inf) cout << "IMPOSSIBLE"; else cout << r - 1;
		cout << '\n';
	}
	
	return 0;
}
