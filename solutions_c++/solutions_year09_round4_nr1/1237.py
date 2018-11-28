#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int list[100], pos[100];
bool used[100];
int result = 0;
int N;

int count() {
	int result = 0;
	for (int i = 0; i < N; i++) if (pos[i] != 0) {
		for (int j = i + 1; j < N; j++) if (pos[j] != 0 && pos[j] < pos[i])
			result++;
	}
	return result;
}

void dfs(int step) {
	int temp = count();
	if (temp >= result) return;
	if (step == N) {
		result = temp;
		return;
	}
	for (int i = 0; i < N; i++) if (!used[i] && list[step] <= i) {
		used[i] = true;
		pos[step] = i + 1;
		dfs(step + 1);
		used[i] = false;
		pos[step] = 0;
	}
}

char temp[100];

int main() {
	int caseSize;
	scanf("%d", &caseSize);
	for (int T = 1; T <= caseSize; T++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%s", temp);
			list[i] = -1;
			for (int j = N - 1; j >= 0; j--)
				if (temp[j] == '1') {
					list[i] = j;
					break;
				}
		}
		result = 0x7fffffff;
		memset(used, 0, sizeof(used));
		memset(pos, 0, sizeof(pos));
		dfs(0);
		printf("Case #%d: %d\n", T, result);
	}
	return 0;
}
