#include <stdio.h>

const int MAX_T = 501;
char t[MAX_T];
int nbT;

char w[20] = "welcome to code jam";

int dyn[MAX_T][20];

int subs(int s1, int s2)
{
	if (w[s2] == '\0')
		return 1;
	if (t[s1] == '\0')
		return 0;

	if (dyn[s1][s2] == -1) {
		int nb = 0;
		if (t[s1] == w[s2]) 
			nb = subs(s1+1, s2+1);
		nb = (nb+subs(s1+1, s2))%10000;
		dyn[s1][s2] = nb;
	}
	return dyn[s1][s2];
}

int main()
{
	FILE *fin = fopen("C-large.in", "r");
	FILE *fout = fopen("C-large.out","w");

	fscanf(fin, "%d", &nbT);
	for (int i = 0; i < nbT; i++) {
		char c = '\n';
		while (c == '\n' || c == '\r') fscanf(fin, "%c", &c);
		int len = 0;
		while (c != '\n' && c != '\r') {
			t[len] = c;
			len++;
			fscanf(fin, "%c", &c);
		}
		t[len] = '\0';
		
		for (int j = 0; j < MAX_T; j++)
			for (int k = 0; k < 20; k++)
				dyn[j][k] = -1;

		int nbs = subs(0,0);
		fprintf(fout, "Case #%d: ", i+1);
		if (nbs < 10)
			fprintf(fout, "000%d\n", nbs);
		else if (nbs < 100)
			fprintf(fout, "00%d\n", nbs);
		else if (nbs < 1000)
			fprintf(fout, "0%d\n", nbs);
		else
			fprintf(fout, "%d\n", nbs);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
