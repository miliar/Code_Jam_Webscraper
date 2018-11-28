#include <iostream>
using namespace std;

int M, V;
int tree[10000];
int changeable[10000];

struct answer {
	int t;
	int f;
};

answer recurse(int node) {
	answer a;
	a.t = a.f = -1;
	if (node >= (M-1)/2) {
		if (tree[node]) a.t = 0;
		else a.f = 0;
		return a;
	}
	answer b = recurse(2*node+1), c = recurse(2*node+2);
	if (tree[node]) {
		if (b.t >= 0 && c.t >= 0) a.t = b.t+c.t;
		if (b.f >= 0 && c.f >= 0) a.f = b.f+c.f;
		if (b.f >= 0 && c.t >= 0 && (a.f < 0 || b.f+c.t < a.f)) a.f = b.f+c.t;
		if (b.t >= 0 && c.f >= 0 && (a.f < 0 || b.t+c.f < a.f)) a.f = b.t+c.f;
		if (b.f >= 0 && c.t >= 0 && changeable[node] && (a.t < 0 || b.f+c.t+1 < a.t)) a.t = b.f+c.t+1;
		if (b.t >= 0 && c.f >= 0 && changeable[node] && (a.t < 0 || b.t+c.f+1 < a.t)) a.t = b.t+c.f+1;
	} else {
		if (b.t >= 0 && c.t >= 0) a.t = b.t+c.t;
		if (b.f >= 0 && c.f >= 0) a.f = b.f+c.f;
		if (b.f >= 0 && c.t >= 0 && (a.t < 0 || b.f+c.t < a.t)) a.t = b.f+c.t;
		if (b.t >= 0 && c.f >= 0 && (a.t < 0 || b.t+c.f < a.t)) a.t = b.t+c.f;
		if (b.f >= 0 && c.t >= 0 && changeable[node] && (a.f < 0 || b.f+c.t+1 < a.f)) a.f = b.f+c.t+1;
		if (b.t >= 0 && c.f >= 0 && changeable[node] && (a.f < 0 || b.t+c.f+1 < a.f)) a.f = b.t+c.f+1;
	}
	return a;
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> M >> V;
		for (int j = 0; j < (M-1)/2; j++)
			cin >> tree[j] >> changeable[j];
		for (int j = (M-1)/2; j < M; j++)
			cin >> tree[j];
		int ans;
		if (V) ans = recurse(0).t;
		else ans = recurse(0).f;
		cout << "Case #" << i+1 << ": ";
		if (ans >= 0) cout << ans;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
}
