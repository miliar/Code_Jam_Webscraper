#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
using namespace std;

char word[10010][14];
char order[30];
int finish[10010];
int ordpos[30];

int mask[10010][30];

int ans, anstime;
void work2(int tried, int start, const vector<int>& ws) {
	if (ws.empty())
		return;
	map<int, vector<int> > w;
	w[0] = vector<int>();
	for (unsigned i = 0; i < ws.size(); ++i) {
		w[mask[ws[i]][start]].push_back(ws[i]);
		if (finish[ws[i]] == start) {
			w[mask[ws[i]][start]].pop_back();
			if (anstime < tried || (anstime == tried && ans > ws[i] )) {
				ans = ws[i];
				anstime = tried;
			}
		}
	}
	if (w.size() == 1) // No word has this letter.
		work2(tried, start + 1, w[0]);
	else {
		for (map<int, vector<int> >::iterator it = w.begin();
				it != w.end(); ++it) {
			work2(tried + (it->first == 0), start + 1, it->second);
		}
	}
}

void work() {
	int n, m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i) {
		scanf("%s", word[i]);
	}
	for (int i = 0; i < m; ++i) {
		anstime = -1;
		scanf("%s", order);
		for (int j = 0; j < 26; ++j) {
			ordpos[order[j] - 'a'] = j;
		}
		vector<vector<int> > ord(12);
		for (int j = 0; j < n; ++j) {
			int l = strlen(word[j]);
			ord[l].push_back(j);
			int f = -1;
			for (int k = 0; k < 26; ++k)
				mask[j][k] = 0;
			for (int k = 0; word[j][k]; ++k) {
				if (f < ordpos[word[j][k] - 'a'])
					f = ordpos[word[j][k] - 'a'];
				mask[j][ordpos[word[j][k] - 'a']] |= 1 << k;
			}
			finish[j] = f;
		}
		for (unsigned j = 0; j < 11; ++j) {
			work2(0, 0, ord[j]);
		}
		printf(" %s", word[ans]);
	}
	printf("\n");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d:\n", Ti);
		printf("Case #%d:", Ti);
		work();
	}
}
