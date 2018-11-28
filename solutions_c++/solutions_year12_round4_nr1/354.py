#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 10000 + 1;
const int INF = 1012345678;

int n, d[MAXN], l[MAXN], D, swing[MAXN];

int main() {
	int taskNumber;
	scanf("%d", &taskNumber);
	for (int taskIdx = 0; taskIdx < taskNumber; taskIdx++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &D);
		fill(swing, swing + n, -INF);
		swing[0] = d[0];
		bool valid = false;
		for (int i = 0; i < n; i++) {
			if (swing[i] == -INF) continue;
			if (d[i] + swing[i] >= D) {
				valid = true;
				break;
			}
			for (int j = i + 1; j < n && d[i] + swing[i] >= d[j]; j++) {
				swing[j] = max(swing[j], min(d[j] - d[i], l[j]));
			}
		}
		printf("Case #%d: %s\n", taskIdx + 1, valid ? "YES" : "NO");
	}
	return 0;
}
