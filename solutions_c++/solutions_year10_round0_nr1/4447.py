#include <iostream>
using namespace std;
int main() {
	int f, id, n, k, i, j, flag;
	bool used[35];
	scanf("%d", &f);
	for (id = 1; id <= f; id++) {
		scanf("%d%d", &n, &k);
		memset(used, 0, sizeof(used));
		for (i = 0; i < k; i++) {
			for (j = 0; (j < n) && used[j]; j++) {
				used[j] = 0;
				
			}
			used[j] = 1;
		}
		printf("Case #%d: ", id);
		for (i = 0; i < n && used[i]; i++);
		if (i == n) puts("ON");
		else puts("OFF");
	}
}
