#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>

const long double eps = 1e-9;

using namespace std;


int n, q;
int dp[101][1001];
map<string, int> id;
vector <int> que;



bool Good(char c)
{
	if (c >= '0' && c <= '9') return true;
	if (c >= 'a' && c <= 'z') return true;
	if (c >= 'A' && c <= 'Z') return true;
	if (c == ' ') return true;
	return false;
}

void Load()
{
	memset(dp, -1, sizeof(dp));
	id.clear();
	char c;
	string s;
	int i, j, k;
	cin >> n;
	que.clear();
	for (i = 1; i <= n; i++) {
		dp[i][0] = 0;
		s.clear();
		c = getchar();
		while (!Good(c))c = getchar();
		while (Good(c)) {
			s += c;
			c = getchar();
		}
		id[s] = i;
	}
	cin >> q;
	for (i = 1; i <= q; i++) {
		s.clear();
		c = getchar();
		while (!Good(c))c = getchar();
		while (Good(c)) {
			s += c;
			c = getchar();
		}
		que.push_back(id[s]);
	}
	cerr << n << " " << q << "\n";
}


void Solve()
{
	int i, j, k;
	for (i = 0; i < q; i++) {
		for (j = 1; j <= n; j++) {
			if (dp[j][i] == -1) continue;
			for (k = 1; k <= n; k++) {
				if (k == que[i] || k == j) continue;
				if (dp[k][i + 1] < 0 || dp[k][i + 1] > dp[j][i] + 1) {
					dp[k][i + 1] = dp[j][i] + 1;
				}
			}
			if (j != que[i]) {
				if (dp[j][i + 1] < 0 || dp[j][i + 1] > dp[j][i]) dp[j][i + 1] = dp[j][i];
			}
		}
	}
	j = -1;
	for (i = 1; i <= n; i++) {
		if (dp[i][q] < 0) continue;
		if (dp[i][q] < j || j == -1) j = dp[i][q];
	}
	cout << j << "\n";
}

void Save()
{
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		printf("Case #%d: ", tt);
		Load();
		Solve();
		Save();
	}
	return 0;
}