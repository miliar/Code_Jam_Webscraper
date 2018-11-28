#include <stdio.h>
#include <string>

int N, L;
char welcome[20]="welcome to code jam";
char para[510]={0};
int d[20][510]={0};
int main(void)
{
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	int test_case, i, j, tmp;
	fscanf(fin, "%d", &N);
	fgets(para,510,fin);
	for (test_case=1; test_case<=N; ++test_case){
		fgets(para,510,fin);
		L = strlen(para);
		--L; para[L] = 0;

		for (j=0;j<L;++j){
			if (para[j] == 'w') d[0][j] = 1;
		}
		for (i=1;i<19;++i){
			tmp = 0;
			for (j=0;j<L;++j){
				if (para[j] == welcome[i]){
					d[i][j] = tmp;
				}
				tmp = tmp + d[i-1][j];
				if (tmp>9999) tmp = tmp - 10000;
			}
		}

		tmp = 0;
		for (j=0;j<L;++j){
			tmp = tmp + d[i-1][j];
			if (tmp>9999) tmp = tmp - 10000;
		}
		fprintf(fout, "Case #%d: ", test_case);
		if (tmp<1000) fprintf(fout, "0");
		if (tmp<100) fprintf(fout, "0");
		if (tmp<10) fprintf(fout, "0");
		fprintf(fout, "%d\n", tmp);

		for (i=0;i<19;++i){
			for (j=0;j<L;++j){
				d[i][j] = 0;
			}
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}