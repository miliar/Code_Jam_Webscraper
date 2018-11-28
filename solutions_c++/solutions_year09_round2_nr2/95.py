#include <cstdio>
#include <cctype>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

char str[100];
int ct[10];

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int i, j, T, n;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%s", str);
		memset(ct, 0, sizeof(ct));
		n = strlen(str);
		for (i = 0; i < n; i++) ct[str[i] - '0']++;
		if (next_permutation(str, str + n)) {
			printf("%s\n",str);
		}
		else {
			for (i = 1; i < 10; i++) if (ct[i] > 0) break;
			str[0] = i + '0';
			ct[i]--;
			ct[0]++;
			j = 1;
			for (i = 0; i < 10; i++) {
				while(ct[i]) {
					ct[i]--;
					str[j++] = i + '0';
				}
			}
			str[j++] = 0;
			printf("%s\n",str);
		}
	}
	return 0;
}
