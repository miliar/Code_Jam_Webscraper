#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct node_t {
	int t, G, C, I;
	int ch[2];
};
typedef vector<node_t> tree;

void solve(void) {
	int M, V; cin >> M >> V;
	tree T(M);
	int half = (M - 1) / 2;
	for (int x = 0; x < M; x++) {
		if (x < half) {
			T[x].t = 0;
			cin >> T[x].G >> T[x].C;
		} else {
			T[x].t = 1;
			int val; cin >> val;
			T[x].I = val;
			T[x].ch[val] = 0;
			T[x].ch[1-val] = -1;
		}
	}
	for (int x = half-1; x >= 0; x--) {
		int l = 2*x+1;
		int r = 2*x+2;
		int l0 = T[l].ch[0];
		int l1 = T[l].ch[1];
		int r0 = T[r].ch[0];
		int r1 = T[r].ch[1];
		if ((l0 == -1) && (r0 == -1)) {
			T[x].ch[0] = -1;
		} else if ((l0 != -1) && (r0 != -1)) {
			if (T[x].G) { //and
				T[x].ch[0] = min(l0, r0);
			} else if (T[x].C) {
				T[x].ch[0] = min(min(l0, r0) + 1, l0 + r0);
			} else {
				T[x].ch[0] = l0 + r0;
			}
		} else if (l0 != -1) {
			if (T[x].G) { //and
				T[x].ch[0] = l0;
			} else if (T[x].C) {
				T[x].ch[0] = l0 + 1;
			} else {
				T[x].ch[0] = -1;
			}
		} else {
			if (T[x].G) { //and
				T[x].ch[0] = r0;
			} else if (T[x].C) {
				T[x].ch[0] = r0 + 1;
			} else {
				T[x].ch[0] = -1;
			}
		}
		if ((l1 == -1) && (r1 == -1)) {
			T[x].ch[1] = -1;
		} else if ((l1 != -1) && (r1 != -1)) {
			if (T[x].G == 0) { //or
				T[x].ch[1] = min(l1, r1);
			} else if (T[x].C) {
				T[x].ch[1] = min(min(l1, r1) + 1, l1 + r1);
			} else {
				T[x].ch[1] = l1 + r1;
			}
		} else if (l1 != -1) {
			if (T[x].G == 0) { //or
				T[x].ch[1] = l1;
			} else if (T[x].C) {
				T[x].ch[1] = l1 + 1;
			} else {
				T[x].ch[1] = -1;
			}
		} else {
			if (T[x].G == 0) { //or
				T[x].ch[1] = r1;
			} else if (T[x].C) {
				T[x].ch[1] = r1 + 1;
			} else {
				T[x].ch[1] = -1;
			}
		}
	}
	int cc = T[0].ch[V];
	if (cc != -1) {
		cout << cc;
	} else {
		cout << "IMPOSSIBLE";
	}
	
}

int main(void) {
	int nc; cin >> nc;
	for (int ic = 1; ic <= nc; ic++) {
		cout << "Case #" << ic << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
