#include <stdio.h>
#define MIN(n,m) (((n)<(m))?(n):(m))
#define MAX(n,m) (((n)>(m))?(n):(m))
#define ABS(n,m) (((n)<0)?-(n):(n))

FILE *fin, *fout;
int N;
int D[110][110]={0};
char R[110];
int P[110];
void input(void)
{
	fscanf(fin, "%d", &N);
	int i;
	for (i=1;i<=N;++i){
		fscanf(fin, " %c %d", &R[i], &P[i]);
	}
}
void process(void)
{
	int i, j, k;
	R[0] = R[1];
	P[0] = 1;
	for (j=1;j<=100;++j){
		D[0][j] = j-1;
	}
	for (i=1;i<=N;++i){
		for (j=1;j<=100;++j){
			if (R[i] == R[i-1]){
				D[i][j] = D[i-1][1] + MAX(ABS(1-j),ABS(P[i]-P[i-1])+1);
			}else{
				D[i][j] = D[i-1][1] + MAX(ABS(P[i]-1)+1,ABS(j-P[i-1]));
			}
			for (k=2;k<=100;++k){
				if (R[i] == R[i-1]){
					D[i][j] = MIN(D[i][j],D[i-1][k]+MAX(ABS(k-j),ABS(P[i]-P[i-1])+1));
				}else{
					D[i][j] = MIN(D[i][j],D[i-1][k]+MAX(ABS(P[i]-k)+1,ABS(j-P[i-1])));
				}
			}
		}
	}
}
int output(void)
{
	int inf=D[N][1];
	int i;
	for (i=2;i<=100;++i){
		inf = MIN(inf, D[N][i]);
	}
	return inf;
}
int main(void)
{
	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");
	int T, t, o;
	fscanf(fin, "%d", &T);
	for (t=1; t<=T; ++t){
		input();
		process();
		fprintf(fout, "Case #%d: %d\n", t, output());
	}
	fclose(fin);
	fclose(fout);
	return 0;
}