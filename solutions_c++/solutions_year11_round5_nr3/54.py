#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

const int MOD = 1000003;

vector<int> vs[20010];
int used[20010];

int mod(int a, int m) {
	return (a % m + m) % m;
}

int getpos(int i, int j, int r, int c) {
	i = mod(i, r); j = mod(j, c);
	return i * c + j;
}

int dfs(int pos, int s = 1) {
	used[pos] = 1;
	int res = s;
	for(int i = 0; i < vs[pos].size(); ++i) if(!used[vs[pos][i]]) {
		res += dfs(vs[pos][i], -s);
	}
	return res;
}

int main() {
	int T;
	cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		int r, c;
		cin >> r >> c;
		for(int i = 0; i < 2 * r * c; ++i) {
			vs[i].clear();
			used[i] = 0;
		}
		for(int i = 0; i < r; ++i) {
			char in[200];
			scanf("%s", in);
			for(int j = 0; j < c; ++j) {
				int v = i * c + j;
				switch(in[j]) {
					case '|':
						vs[v].push_back(getpos(i - 1, j, r, c) + r * c);
						vs[getpos(i - 1, j, r, c) + r * c].push_back(v);
						vs[v].push_back(getpos(i + 1, j, r, c) + r * c);
						vs[getpos(i + 1, j, r, c) + r * c].push_back(v);
						break;
					case '-':
						vs[v].push_back(getpos(i, j - 1, r, c) + r * c);
						vs[getpos(i, j - 1, r, c) + r * c].push_back(v);
						vs[v].push_back(getpos(i, j + 1, r, c) + r * c);
						vs[getpos(i, j + 1, r, c) + r * c].push_back(v);
						break;
					case '/':
						vs[v].push_back(getpos(i - 1, j + 1, r, c) + r * c);
						vs[getpos(i - 1, j + 1, r, c) + r * c].push_back(v);
						vs[v].push_back(getpos(i + 1, j - 1, r, c) + r * c);
						vs[getpos(i + 1, j - 1, r, c) + r * c].push_back(v);
						break;
					case '\\':
						vs[v].push_back(getpos(i - 1, j - 1, r, c) + r * c);
						vs[getpos(i - 1, j - 1, r, c) + r * c].push_back(v);
						vs[v].push_back(getpos(i + 1, j + 1, r, c) + r * c);
						vs[getpos(i + 1, j + 1, r, c) + r * c].push_back(v);
						break;
				}
			}
		}
		for(int i = r * c; i < 2 * r * c; ++i) {
			if(vs[i].size() == 1) {
				used[vs[i][0]] = 1;
				used[i] = 1;
			}
		}
		int res = 1;
		for(int i = 0; i < r * c; ++i) if(!used[i]) {
			if(dfs(i)) res = 0;
			else res = (res * 2) % MOD;
		}
		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}
