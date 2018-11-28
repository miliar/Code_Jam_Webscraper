#include <iostream>

const int NMAX = 10000;

const int Q = 0;
const int W = 1;
const int E = 2;
const int R = 3;
const int A = 4;
const int S = 5;
const int D = 6;
const int F = 7;

FILE *f = fopen("Magicka.in", "r");
FILE *g = fopen("Magicka.out", "w");

int T;
int a[8][8]; //if a[i][j] != -1 i + j = a[i][j] 
int b[8][8];
char *sir;
char *final; //sirul de vraji
char *rez;   //rezultatul de vraji
int nrElemRez = 0;

int editSir(const char* sir)
{
	int i = 0, C = 0, DD = 0, N = 0;
	while ((sir[i] >= '0') && (sir[i] <= '9'))
	{
		C = C * 10 + sir[i] - '0';
		i++;
	}
	i++;//space
	for (int k = 0; k < C; ++k)
	{
		int x = -1, y = -1;
		if (sir[i] == 'Q') x = Q;
		if (sir[i] == 'W') x = W;
		if (sir[i] == 'E') x = E;
		if (sir[i] == 'R') x = R;
		if (sir[i] == 'A') x = A;
		if (sir[i] == 'S') x = S;
		if (sir[i] == 'D') x = D;
		if (sir[i] == 'F') x = F;

		if (sir[i + 1] == 'Q') y = Q;
		if (sir[i + 1] == 'W') y = W;
		if (sir[i + 1] == 'E') y = E;
		if (sir[i + 1] == 'R') y = R;
		if (sir[i + 1] == 'A') y = A;
		if (sir[i + 1] == 'S') y = S;
		if (sir[i + 1] == 'D') y = D;
		if (sir[i + 1] == 'F') y = F;

		if ((x != -1) && (y != -1))
		{
			a[x][y] = sir[i + 2];
			a[y][x] = sir[i + 2];
		}
		i = i + 4;
	}

	while ((sir[i] >= '0') && (sir[i] <= '9'))
	{
		DD = DD * 10 + sir[i] - '0';
		i++;
	}
	i++;
	for (int k = 0; k < DD; ++k)
	{
		int x = -1, y = -1;
		if (sir[i] == 'Q') x = Q;
		if (sir[i] == 'W') x = W;
		if (sir[i] == 'E') x = E;
		if (sir[i] == 'R') x = R;
		if (sir[i] == 'A') x = A;
		if (sir[i] == 'S') x = S;
		if (sir[i] == 'D') x = D;
		if (sir[i] == 'F') x = F;

		if (sir[i + 1] == 'Q') y = Q;
		if (sir[i + 1] == 'W') y = W;
		if (sir[i + 1] == 'E') y = E;
		if (sir[i + 1] == 'R') y = R;
		if (sir[i + 1] == 'A') y = A;
		if (sir[i + 1] == 'S') y = S;
		if (sir[i + 1] == 'D') y = D;
		if (sir[i + 1] == 'F') y = F;

		if ((x != -1) && (y != -1))
		{
			b[x][y] = 1;
			b[y][x] = 1;
		}
		i = i + 3;
	}

	while ((sir[i] >= '0') && (sir[i] <= '9'))
	{
		N = N * 10 + sir[i] - '0';
		i++;
	}
	i++;

	strncpy(final, sir + i, N);  
	final[N] = '\0';

	return N;
}

int main()
{
	fscanf(f, "%d\n", &T);
	for (int t = 0; t < T; ++t)
	{
		for (int i = 0; i < 8; ++i)
			for (int j = 0; j < 8; ++j)
				a[i][j] = -1;
		for (int i = 0; i < 8; ++i)
			for (int j = 0; j < 8; ++j)
				b[i][j] = -1;
		sir = new char[NMAX];
		final = new char[NMAX];
		rez = new char[NMAX];

		fgets(sir, NMAX, f);
		int N = editSir(sir);
		nrElemRez = 1;
		rez[0] = final[0];
		for (int i = 1; i < N; ++i)
		{
			int x = -1, y = -1;
			if (final[i] == 'Q') x = Q;
			if (final[i] == 'W') x = W;
			if (final[i] == 'E') x = E;
			if (final[i] == 'R') x = R;
			if (final[i] == 'A') x = A;
			if (final[i] == 'S') x = S;
			if (final[i] == 'D') x = D;
			if (final[i] == 'F') x = F;

			if (rez[nrElemRez - 1] == 'Q') y = Q;
			if (rez[nrElemRez - 1] == 'W') y = W;
			if (rez[nrElemRez - 1] == 'E') y = E;
			if (rez[nrElemRez - 1] == 'R') y = R;
			if (rez[nrElemRez - 1] == 'A') y = A;
			if (rez[nrElemRez - 1] == 'S') y = S;
			if (rez[nrElemRez - 1] == 'D') y = D;
			if (rez[nrElemRez - 1] == 'F') y = F;

			if ((x != -1) && (y != -1) && (a[x][y] != -1))
			{
				rez[nrElemRez - 1] = a[x][y];
			}
			else
			{
				int j = nrElemRez - 1;
				while (j >= 0)
				{
					if (rez[j] == 'Q') y = Q;
					if (rez[j] == 'W') y = W;
					if (rez[j] == 'E') y = E;
					if (rez[j] == 'R') y = R;
					if (rez[j] == 'A') y = A;
					if (rez[j] == 'S') y = S;
					if (rez[j] == 'D') y = D;
					if (rez[j] == 'F') y = F;
					if ((x != -1) && (y != -1) && (b[x][y] != -1))
					{
						/*rez[j] ='\0';
						nrElemRez = j;
						j = -5;*/
						//lista de fapt se sterge cu totul
						rez[0] = '\0';
						nrElemRez = 0;
						j = -5;
					}
					j--;
				}
				if (j != -6)
				{
					rez[nrElemRez] = final[i];
					nrElemRez++;
				}
			}
		}

		fprintf(g, "Case #%d: [", t + 1);
		for (int i = 0; i < nrElemRez; ++i)
		{
			if (i != nrElemRez - 1) fprintf(g, "%c, ", rez[i]);
							   else fprintf(g, "%c", rez[i]);
		}
		fprintf(g, "]\n");

		
		delete[] rez;
		delete[] sir;
		delete[] final;
	}

	fclose(f);
	fclose(g);

	return 0;
}