#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

const int MAXN = 30;

char st[MAXN];
int cnt[MAXN];
bool pos[11];
vector<string> D, v[2];

int gao(string pat, string list) {
//printf("pat = %s\n", pat.c_str());
	int len = pat.length();
	
	v[0].clear();

	memset(cnt, 0, sizeof(cnt));
	for (int i = 0; i < (int)D.size(); i++) {
		if (D[i].length() == pat.length()) {
			v[0].push_back(D[i]);
			for (int j = 0; j < len; j++) {
				cnt[D[i][j] - 'a']++;
			}
		}
	}

	int ret = 0, t0 = 0, t1;
	for (int i = 0; i < (int)list.length(); i++) {
		if (!cnt[list[i] - 'a']) continue;
//printf("guess %c", list[i]);
		t1 = 1 - t0;
		v[t1].clear();
		bool yes = false;
		memset(pos, false, sizeof(pos));
		for (int j = 0; j < len; j++) {
			if (pat[j] == list[i]) {
				yes = true;
				pos[j] = true;
			}
		}
//printf(", pos[len - 1] = %d", pos[len - 1]);
		if (!yes) ret--;
		for (int j = 0; j < (int)v[t0].size(); j++) {
			bool yes = true;
			for (int k = 0; k < len; k++) {
				if (pos[k] && v[t0][j][k] != list[i]) {
					yes = false;
					break;
				}
				if (v[t0][j][k] == list[i] && !pos[k]) {
					yes = false;
					break;
				}
			}
//printf(", yes = %d, now = %s", yes, v[t0][j].c_str());
			if (yes) {
				v[t1].push_back(v[t0][j]);
			} else {
				for (int k = 0; k < len; k++) {
					cnt[v[t0][j][k] - 'a']--;
				}
			}
		}
		t0 = t1;
//printf(", ret = %d\n", ret);
		if (v[t0].size() == 1) break;
	}
	return ret;
}

void solve() {
	int n, m;
	scanf("%d%d", &n, &m);
	memset(cnt, 0, sizeof(cnt));
	D.clear();
	for (int i = 0; i < n; i++) {
		scanf("%s", st);
		string ss = st;
		D.push_back(ss);
	}
	
	for (int j = 0; j < m; j++) {
//puts("");puts("");
		scanf("%s", st);
		int ans = -1, ans_score = 10000000;
		for (int i = 0; i < n; i++) {
			int score = gao(D[i], st);
			if (score < ans_score) {
				ans_score = score;
				ans = i;
			}
		}
		printf(" %s", D[ans].c_str());
//puts("");puts("");
	}
	puts("");
}

int main() {
	int test;
	scanf("%d", &test);
	for (int i = 0; i < test; i++) {
		printf("Case #%d:", i + 1);
		solve();
	}
	return 0;
}
