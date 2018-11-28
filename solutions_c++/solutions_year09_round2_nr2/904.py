#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char sNum[30];
int len;

void solve() {
	len = strlen(sNum);

	int i = len - 1;
	while (i >= 1 && sNum[i - 1] >= sNum[i]) i--;
	if (i == 0) {
		int j = len - 1;
		while (j >= 0 && sNum[j] == '0') j--;
		if (j != len - 1) {
			sNum[len - 1] = sNum[j];
			sNum[j] = '0';
		}
		printf("%c0", sNum[len - 1]);
		for (int j = len - 2; j >= 0; j--) printf("%c", sNum[j]);
		printf("\n");
		return;
	}
	else {
		int k = len - 1;
		while (k > i - 1 && sNum[k] <= sNum[i - 1]) k--;
		char tmp = sNum[i - 1];
		sNum[i - 1] = sNum[k];
		sNum[k] = tmp;
		sort(sNum + i, sNum + len);
		printf("%s\n", sNum);
	}
	
}//solve

int main() {
	int nCase;

	scanf("%d", &nCase);
	for (int t = 1; t <= nCase; t++) {
		scanf(" %s", sNum);

		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
