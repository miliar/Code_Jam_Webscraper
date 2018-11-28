#include <stdio.h>
#include <string.h>

int N;
char S[1000];
char B[] = "welcome to code jam";

int main() {
	scanf("%d", &N);
	for (int case_x = 1; case_x <= N; case_x++) {
		scanf(" "); gets(S);
		int bef[20], aft[20];
		bzero(bef, sizeof(bef));
		bzero(aft, sizeof(aft));
		bef[0] = 1;
		for (int i = 0; S[i]; i++) {
			memcpy(aft, bef, sizeof(aft));
			for (int j = 0; B[j]; j++) if (S[i] == B[j])
			 aft[j + 1] = (aft[j + 1] + bef[j]) % 1000;
			memcpy(bef, aft, sizeof(aft));
		}
		printf("Case #%d: %04d\n", case_x, bef[19]);
	}
	return 0;
}
