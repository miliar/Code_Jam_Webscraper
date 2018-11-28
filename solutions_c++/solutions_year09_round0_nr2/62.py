#include <stdio.h>
#define MOST_MAX_VALUE	99999

int H, W;
int MAP[110][110]={0};
char PRT[110][110]={0};
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};
char basin;
char flow(int x, int y)
{
	int i, MIN=MOST_MAX_VALUE, d = -1;
	for (i=0;i<4;++i){
		if (1<=x+dx[i] && x+dx[i]<=H && 1<=y+dy[i] && y+dy[i]<=W){
			if (MIN>MAP[x+dx[i]][y+dy[i]]){
				MIN = MAP[x+dx[i]][y+dy[i]];
				d = i;
			}
		}
	}
	
	if (d != -1 && MIN<MAP[x][y]){
		if (PRT[x+dx[d]][y+dy[d]]!=0) PRT[x][y] = PRT[x+dx[d]][y+dy[d]];
		else PRT[x][y] = flow(x+dx[d], y+dy[d]);
	}
	else{
		PRT[x][y] = ++basin;
	}
	return PRT[x][y];
}
int main(void)
{
	int T;
	int i, j;
	int test_case;
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &T);
	for (test_case = 1; test_case<=T; ++test_case){
		fscanf(fin, "%d %d", &H, &W);
		for (i=1;i<=H;++i){
			for (j=1;j<=W;++j){
				fscanf(fin, "%d", &MAP[i][j]);
			}
		}
		basin = 'a'-1;
		for (i=1;i<=H;++i){
			for (j=1;j<=W;++j){
				if (PRT[i][j] == 0){
					flow(i,j);
				}
			}
		}
		fprintf(fout, "Case #%d:\n", test_case);
		for (i=1;i<=H;++i){
			for (j=1;j<=W;++j){
				fprintf(fout, "%c ", PRT[i][j]);
				PRT[i][j] = 0;
			}
			fprintf(fout, "\n");
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}