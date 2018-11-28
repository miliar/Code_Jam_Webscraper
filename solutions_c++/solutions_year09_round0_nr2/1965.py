#include <iostream>
using namespace std;

int H, W, m[100][100];
char label[100][100], ch;

char DP(int i, int j)
{
	if(label[i][j] != 'A')
		return label[i][j];
	else {
		int min = 10000, ii, jj;
		if(i > 0 && m[i-1][j] < m[i][j]) {
			ii = i-1;
			jj= j;
			min = m[i-1][j];
		}
		if(j > 0 && m[i][j-1] < m[i][j] && m[i][j-1] < min) {
			ii = i;
			jj = j-1;
			min = m[i][j-1];
		}
		if(j < W-1 && m[i][j+1] < m[i][j] && m[i][j+1] < min) {
			ii = i;
			jj = j+1;
			min = m[i][j+1];
		}
		if(i < H-1 && m[i+1][j] < m[i][j] && m[i+1][j] < min) {
			ii = i+1;
			jj = j;
			min = m[i+1][j];
		}
		if(min != 10000) {
			label[ii][jj] = DP(ii, jj);
			return label[ii][jj];
		} else {
			ch++;
			label[i][j] = ch;
			return ch;
		}
	}
}

int main()
{
	FILE *fp;
	fp = fopen("output.txt", "w");
	int T, i, j;
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++) {
		scanf("%d%d", &H, &W);
		for(i = 0; i < H; i++) {
			for(j = 0; j < W; j++) {
				scanf("%d", &m[i][j]);
				label[i][j] = 'A';
			}
		}
		ch = 'a'-1;
		for(i = 0; i < H; i++) {
			for(j = 0; j < W; j++) {
				label[i][j] = DP(i, j);
			}
		}
		fprintf(fp, "Case #%d:\n", cases);
		for(i = 0; i < H; i++) {
			for(j = 0; j < W; j++) {
				fprintf(fp, "%c", label[i][j]);
				if(j != W-1)
					fprintf(fp, " ");
			}
			fprintf(fp, "\n");
		}
	}
	fclose(fp);
	return 0;
}