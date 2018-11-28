#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <math.h>
#include <memory.h>
using namespace std;

int T, C, D, N;
char form[100][100];
bool opp[100][100];
char in[1000];

char list[1000];

int main() {
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d ", &C);
		memset(form, 0, sizeof(form));
		memset(opp, 0, sizeof(opp));
		for (int i = 0; i < C; i++) {
			scanf("%s ", in);
			form[in[0]-'A'][in[1]-'A'] = in[2];
			form[in[1]-'A'][in[0]-'A'] = in[2];
		}
		scanf("%d ", &D);
		for (int i = 0; i < D; i++) {
			scanf("%s ", in);
			opp[in[0]-'A'][in[1]-'A'] = true;
			opp[in[1]-'A'][in[0]-'A'] = true;
		}
		scanf("%d ", &N);
		scanf("%s ", in);
		int pos = 0;
		for (int i = 0; i < N; i++) {
			list[pos] = in[i];
			while(pos > 0 && form[list[pos]-'A'][list[pos-1]-'A']) {
				list[pos-1] = form[list[pos]-'A'][list[pos-1]-'A'];
				pos--;
			}
			for (int k = 0; k < pos; k++)
				if (opp[list[k]-'A'][list[pos]-'A'])
					pos = -1;
			pos++;
		}
		printf("[");
		for (int i = 0; i < pos; i++) {
			if (i > 0)
				printf(", ");
			printf("%c", list[i]);
		}
		printf("]\n");
	}
	return 0;
}
