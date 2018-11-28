#include <cstdio>

using namespace std;

char combine[256][256], list[256], S[256];
int Test, C, D, opposed[256][256], listn, N;

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	
	scanf("%d", &Test);
	for (int kase = 1; kase <= Test; kase++) {
		for (int i = 0; i < 256; i++) for (int j = 0; j < 256; j++) combine[i][j] = '@', opposed[i][j] = 0;
		scanf("%d", &C); while (C--) scanf("%s", S), combine[S[0]][S[1]] = combine[S[1]][S[0]] = S[2];
		scanf("%d", &D); while (D--) scanf("%s", S), opposed[S[0]][S[1]] = opposed[S[1]][S[0]] = 1;
		listn = 0;
		scanf("%d", &N); scanf("%s", S);
		for (int i = 0; i < N; i++)
			if (listn) {
				char c = combine[S[i]][list[listn]];
				if (c != '@') {
					list[listn] = c;
				} else {
					list[++listn] = S[i];
					for (int j = 1; j < listn; j++)
						if (opposed[S[i]][list[j]]) {
							listn = 0;
							break;
						}
				}
			} else list[++listn] = S[i];
		printf("Case #%d: ", kase);
		for (int i = 1; i <= listn; i++) {
			if (i == 1) printf("["); else printf(" ");
			printf("%c", list[i]);
			if (i == listn) printf("]"); else printf(",");
		}
		if (!listn) printf("[]");
		printf("\n");
	}
	
	return 0;
}
