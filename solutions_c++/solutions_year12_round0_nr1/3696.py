#include <stdio.h>
#include <string.h>

#define MAX_N 110

int decode[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

char A[MAX_N];

int main() {

	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
    	memset(A, 0, sizeof(A));
		fgets(A, sizeof(A), stdin);

		int n = strlen(A) - 1;
		for (int j = 0; j < n; j++)
			if ('a' <= A[j] && A[j] <= 'z')
				A[j] = decode[A[j] - 'a'];

		printf("Case #%d: ", i);
		fputs(A, stdout);
	}

	return 0;
}
