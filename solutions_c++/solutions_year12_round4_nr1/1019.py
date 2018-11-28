#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX = 10000;

int n;
pair<int, int> vines[MAX];
int length[MAX];
int offset[MAX];
int s[MAX];
int holdPoint[MAX];

int otherAt;

bool cmp(int a, int b) {
	return offset[a] < offset[b];
}

void proc() {
	scanf("%d ", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &offset[i], &length[i]);
		s[i] = i;
		holdPoint[i] = 0;
	}

	scanf("%d", &otherAt);

	sort(s, s + n, cmp);

	int start = 0;
	for (int i = 0; i < n; i++) {
		if (s[i] == 0) {
			start = i;
		}
	}

	holdPoint[start] = offset[start];
	for (int i = start; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (offset[s[j]] - offset[s[i]] <= holdPoint[s[i]] && holdPoint[s[j]] == 0) {
				// can reach
				holdPoint[s[j]] = min(offset[s[j]] - offset[s[i]], length[s[j]]);
				if (otherAt - offset[s[j]] <= holdPoint[s[j]]) {
					printf("YES");
					return;
				}
			}
		}
		if (otherAt - offset[s[i]] <= holdPoint[s[i]]) {
			printf("YES");
			return;
		}
	}
	printf("NO");
}

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		proc();
		printf("\n");
	}

	return 0;
}
