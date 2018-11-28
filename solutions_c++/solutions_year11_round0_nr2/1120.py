#include <stdio.h>
using namespace std; 

char lC[40][40];
char lD[40][40];
char lN[200];

int main() {
	int T;
	scanf("%d", &T);
	for (int _=0; _<T; _++) {
		printf("Case #%d: ", _+1);
		int C, D, N;
		scanf("%d", &C);
		for (int i = 0; i < C; i++)
			scanf(" %s", lC[i]);

		scanf("%d", &D);
		for (int i = 0; i < D; i++)
			scanf(" %s", lD[i]);
		
		scanf("%d", &N);
		char temp;
		int sz = 0;
		for (int i = 0; i < N; i++) {
			scanf(" %c", &temp);
			lN[sz++] = temp;
			if (sz >= 2) {
				for (int j = 0; j < C; j++) {
					if ((lC[j][0] == temp && lC[j][1] == lN[sz-2]) ||
							(lC[j][0] == lN[sz-2] && lC[j][1] == temp)) {
						lN[sz-2] = lC[j][2];
						sz--;
						goto end;
					}
				}
			}
			for (int j = 0; j < D; j++) {
				char other = 0;
				if ( lD[j][0] == temp) other = lD[j][1];
				else if (lD[j][1] == temp) other = lD[j][0];
				else continue;
				for (int k = 0; k < sz-1; k++) if (lN[k] == other) {
					sz = 0;
					break;
				}
			}
end:;
		}
		printf("[");
		for (int i = 0; i < sz; i++) {
			if (i) printf(", ");
			printf("%c", lN[i]);
		}
		printf("]\n");
	}
	return 0;
}
