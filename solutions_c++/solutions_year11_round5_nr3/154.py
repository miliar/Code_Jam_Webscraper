#include <iostream>
#include <vector>

using namespace std;

int n, m;
int anc[10002];
int size[10002];
vector<pair<int, int> > e;


int toNum(int x, int y) {
	return x * m + y + 1;
}


int find(int u) {
	if (anc[u] == -1) return u;
	return anc[u] = find(anc[u]);
}

void uni(int u, int v) {
	int i = find(u), j = find(v);
	if (i != j) {
		anc[i] = j;
		size[j] += size[i];
	}
}

void addedge(int u, int v) {
	uni(u, v);
	e.push_back(make_pair(u, v));
}

void init()
{
	cin >> n >> m;
	memset(anc, 0xff, sizeof(anc));
	for (int i = 1; i <= n * m; i++) size[i] = 1;
	e.clear();
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < m; j++) {
			if (s[j] == '-') {
				addedge(toNum(i, (j + 1) % m), toNum(i, (j + m - 1) % m));
			} else if (s[j] == '|') {
				addedge(toNum((i + 1) % n, j), toNum((i + n - 1) % n, j));
			} else if (s[j] == '/') {
				addedge(toNum((i + 1) % n, (j + m - 1) % m), toNum((i + n - 1) % n, (j + 1) % m));
			} else {
				addedge(toNum((i + n - 1) % n, (j + m - 1) % m), toNum((i + 1) % n, (j + 1) % m));
			}
		}
	}
}

void work()
{
	for (int i = 0; i < e.size(); i++) {
		size[find(e[i].first)]--;
	}
	int cnt = 0;
	for (int i = 1; i <= n * m; i++) {
		if (find(i) == i) {
			cnt++;
			if (size[i] != 0) {
				cout << 0 << endl;
				return;
			}
		}
	}
	int ret = 1;
	for (int i = 0; i < cnt; i++) {
		ret = (ret * 2) % 1000003;
	}
	cout << ret << endl;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {
		cout << "Case #" << tt << ": ";
		init();
		work();
	}
}