#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>

using namespace std;

void process(vector<vector<int> > &partition, int mask[][27], int pos, int ans[]) {
	vector<vector<int> > newPartition;
	for (int i = 0; i < partition.size(); ++i) {
		map<int, vector<int> > M;
		for (int j = 0; j < partition[i].size(); ++j) {
			M[mask[partition[i][j]][pos]].push_back(partition[i][j]);
		}
		if (M.find(0) != M.end() && M.size() != 1) {
			for (int j = 0; j < M[0].size(); ++j) {
				++ans[M[0][j]];
			}
		}
		for (map<int, vector<int> >::iterator I = M.begin(); I != M.end(); ++I) {
			newPartition.push_back(I->second);
		}
	}
	partition = newPartition;
}

int main() {
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; ++test) {
		printf("Case #%d:", test);
		int N, M;
		scanf("%d %d", &N, &M);
		int mask[N][27];
		char word[N][11];
		memset(mask, 0, sizeof(mask));
		for (int i = 0; i < N; ++i) {
			scanf(" %s", word[i]);
			int len = strlen(word[i]);
			for (int pos = 0; pos < len; ++pos) {
				mask[i][word[i][pos] - 'a'] += 1 << pos;
			}
			mask[i][26] = len;
		}
		for (int j = 0; j < M; ++j) {
			char order[27];
			scanf(" %s", order);
			vector<vector<int> > partition;
			partition.push_back(vector<int> ());
			for (int i = 0; i < N; ++i) {
				partition[0].push_back(i);
			}
			int ans[N];
			memset(ans, 0, sizeof(ans));
			process(partition, mask, 26, ans);
			for (int k = 0; k < 26; ++k) {
				process(partition, mask, order[k] - 'a', ans);
			}
			int best = -1, besti;
			for (int i = 0; i < N; ++i) {
				if (ans[i] > best) {
					best = ans[i];
					besti = i;
				}
			}
			printf(" %s", word[besti]);
		}
		printf("\n");
	}
	return 0;
}
