#include <stdio.h>

const int MAX_L = 20;
const int MAX_D = 5000;
const int MAX_N = 500;

char w[MAX_D][MAX_L];

char tw[MAX_L*50];
int m[MAX_L][30];

int l, d, n;

int doesExist(int s)
{
	for (int i = 0; i < l; i++)
		if (m[i][w[s][i]-'a'] == 0)
			return 0;
	return 1;
}

int main()
{
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-large.out","w");
	
	fscanf(fin, "%d %d %d", &l, &d, &n);

	for (int i = 0; i < d; i++)
		fscanf(fin, "%s", w[i]);

	for (int i = 0; i < n; i++) {
		fscanf(fin, "%s", tw);

		for (int j = 0; j < l; j++)
			for (int k = 0; k < 30; k++)
				m[j][k] = 0;

		int len = 0;
		for (int j = 0; tw[j] != '\0'; j++) {
			if (tw[j] == '(') {
				int k = j+1;
				while (tw[k] != ')') {
					m[len][tw[k]-'a'] = 1;
					k++;
				}
				len++;
				j = k;
			}
			else {
				m[len][tw[j]-'a'] = 1;
				len++;
			}
		}

		int nbw = 0;
		for (int j = 0; j < d; j++)
			if (doesExist(j))
				nbw++;
		fprintf(fout, "Case #%d: %d\n", i+1, nbw);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
