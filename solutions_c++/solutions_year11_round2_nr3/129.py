#include <iostream>
#include <vector>
using namespace std;

const int maxn = 10;
int n, m;
int u[maxn], v[maxn];
int ans, color[maxn];

int pol_cnt, pcnt;
vector<int> poly[maxn];


void preprocess(vector<int> p) {

	bool sp = false;
	for (int i = 0; i < m; i++) {
		vector<int> p1, p2;
		for (int j = 0; j < p.size(); j++) {
			if (p[j] >= u[i] && p[j] <= v[i])
				p1.push_back(p[j]);
			if (p[j] <= u[i] || p[j] >= v[i])
				p2.push_back(p[j]);
		}

		if (p1.size() > 2 && p2.size() > 2) {
			sp = true;
			preprocess(p1);
			preprocess(p2);
			break;
		}
	}

	if (!sp)
		poly[pcnt++] = p;
}

bool used[maxn];

bool check() {
	for (int i = 0; i < pol_cnt; i++) {
		memset(used, 0, sizeof(used));
		int cnt = 0;
		for (int j = 0; j < poly[i].size(); j++)
			if (!used[color[poly[i][j]]]) {
				used[color[poly[i][j]]] = true;
				cnt ++;
			}
		if (cnt != ans) return false;
	}
	return true;
}

bool dfs(int d) {
	if (d == n) {
		return check();
	}

	for (int i = 0; i < ans; i++) {
		color[d] = i;
		if (dfs(d + 1))
			return true;
	}
	return false;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		cin >> n >> m;
		pol_cnt = m + 1;
		pcnt = 0;
		for (int i = 0; i < m; i++) {
			cin >> u[i];
			u[i] --;
		}
		for (int i = 0; i < m; i++) {
			cin >> v[i];
			v[i] --;
		}
		
		vector<int> p;
		for (int i = 0; i < n; i++)
			p.push_back(i);
		preprocess(p);

		// ans		
		for (ans = 5; ans >= 1; ans--) {
			if (dfs(0)) {
				printf("Case #%d: %d\n", tt, ans);
				for (int i = 0; i < n - 1; i++)
					printf("%d ", color[i] + 1);
				printf("%d\n", color[n - 1] + 1);
				break;
			}
		}
	}
}
