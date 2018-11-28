#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

int T, N;
vector<pii> btns;
vector<int> next[2];
int secs, p[2], i_n[2];

int main() {
	int btn, rob;
	char col;

	scanf("%d", &T);

	for(int i = 0; i < T; i++) {
		btns.clear();
		next[0].clear();
		next[1].clear();

		scanf("%d ", &N);

		for(int j = 0; j < N; j++) {
			scanf("%c %d ", &col, &btn);

			next[col == 'O'].push_back(btn);
			btns.push_back(pii(col == 'O', btn));
		}

		secs = 0;
		p[0] = p[1] = 1;
		i_n[0] = i_n[1] = 0;
		for(int j = 0; j < N; j++) {
			rob = btns[j].first;
			while(p[rob] != btns[j].second) {
				for(int k = 0; k < 2; k++) {
					if(i_n[k] < next[k].size()) {
						p[k] += max(min(1, next[k][i_n[k]] - p[k]), -1);
					}
				}
				secs++;
			}
			i_n[rob]++;
			if(i_n[!rob] < next[!rob].size()) {
				p[!rob] += max(min(1, next[!rob][i_n[!rob]] - p[!rob]), -1);
			}
			secs++;
		}
		printf("Case #%d: %d\n", i+1, secs);
	}
	return 0;
}
