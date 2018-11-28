#include <iostream>
using namespace std;

char words[5000][20], patten[1000];
bool flag[5000][20];
int L, D, N;

void func(int pos, int i)
{
	for(int j = 0; j < D; j++) {
		if(words[j][i] == patten[pos])
			flag[j][i] = true;
	}
}

int main()
{
	FILE *fp;
	fp = fopen("output.txt", "w");
	int i, j;
	scanf("%d%d%d", &L, &D, &N);
	for(i = 0; i < D; i++)
		scanf("%s", words[i]);
	for(int cases = 1; cases <= N; cases++) {
		for(i = 0; i < D; i++)
			memset(flag, 0, sizeof(flag));
		scanf("%s", patten);
		int pos = 0;
		for(i = 0; i < L; i++) {
			if(patten[pos] == '(') {
				pos++;
				while(patten[pos] != ')') {
					func(pos, i);
					pos++;
				}
				pos++;
			} else {
				func(pos, i);
				pos++;
			}
		}
		int cnt = 0;
		for(i = 0; i < D; i++) {
			bool tmp = true;
			for(j = 0; j < L; j++) {
				if(!flag[i][j]) {
					tmp = false;
					break;
				}
			}
			if(tmp)
				cnt++;
		}
		fprintf(fp, "Case #%d: %d\n", cases, cnt);
	}
	fclose(fp);
	return 0;
}
