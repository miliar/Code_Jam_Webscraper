#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int MAXN = 300;

int opp[MAXN][MAXN], nopp[MAXN];
int gen[MAXN][MAXN];
int T, C, D, N;
char opstr[MAXN], genstr[MAXN];
char text[MAXN], res[MAXN];
int len;
int in[MAXN];

int main()
{
	scanf("%d", &T);
	for (int ncas = 1; ncas <= T; ncas++) {
		
		memset(nopp, 0, sizeof(nopp));
		memset(gen, -1, sizeof(gen));
		memset(in, 0, sizeof(in));

		scanf("%d", &C);
		for (int i = 0; i < C; i++) {
			scanf("%s", genstr);
			int a = genstr[0], b = genstr[1], g = genstr[2];
			gen[a][b] = gen[b][a] = g;
		}
		scanf("%d", &D);
		for (int i = 0; i < D; i++) {
			scanf("%s", opstr);
			int a = opstr[0], b = opstr[1];
			opp[a][nopp[a]++] = b;	opp[b][nopp[b]++] = a;
		}
		scanf("%d", &N);
		scanf("%s", text);
		len = 0; res[len ++] = text[0]; in[text[0]] ++;
		for (int i = 1; i < N; i++) {
			int ele = text[i];
			bool combine = false;
			bool clr = false;
			if (len != 0 && gen[res[len - 1]][ele] != -1) {
				in[res[len - 1]]--;
				res[len - 1] = gen[res[len - 1]][ele];
				in[res[len - 1]]++;
				combine = true;
			}
			if (!combine) {
				for (int j = 0; j < nopp[ele]; j++) {
					if (in[opp[ele][j]] != 0) {
						memset(in, 0, sizeof(in));
						len = 0;
						clr = true;
						break;
					}
				}
			}
			if ((!combine) && !(clr))  {
				res[len++] = ele;
				in[ele]++;
			}

		}
		printf("Case #%d: [", ncas);
		if (len != 0) printf("%c", res[0]);
		for (int i = 1; i < len; i++) {
			printf(", %c", res[i]);
		}
		printf("]\n");
	}
	return 0;
}
