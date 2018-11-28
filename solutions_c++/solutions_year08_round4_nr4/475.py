/*
 *  Google Code Jam 2008
 *  Round 2 - Problem D - PermRLE
 */


#include <stdio.h>
#include <string>

#define INPUT_FILE	"input.txt"
#define OUTPUT_FILE	"output.txt"

using namespace std;

int T, K;
string S;
long MinSol = 0;
int Flag[16], Perm[16];


string Shuffle(string s, int perm[])
{
	int i, j;
	string rez = s;

	for (i = 0; i * K < s.size(); i++)
	{
		// de la i * k, k pozitii
		for (j = 0; j < K; j++)
		{
			rez[i * K + j] = s[i * K + perm[j] - 1];
		}
	}

	return rez;
}

int Compress(string s)
{
	int i, gr = 1;

	for (i = 1; i < s.size(); i++)
	{
		if (s[i] != s[i - 1])
			gr++;
	}

	return gr;
}

void back(int lev)
{
	int i;

	if (lev == K)
	{
		string sNow = Shuffle(S, Perm);
		int cnt = Compress(sNow);

		if (cnt < MinSol)
			MinSol = cnt;
	} else
	for (i = 1; i <= K; i++)
		if (!Flag[i])
		{
			Flag[i] = 1;
			Perm[lev] = i;

			back(lev + 1);

			Flag[i] = 0;
		};
}

void Solve()
{
	MinSol = S.size();

	back(0);
}


int main()
{
	int i;
	char sz[50000];


	freopen(INPUT_FILE, "rt", stdin);
	freopen(OUTPUT_FILE, "wt", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++)
	{
		scanf("%d\n%s\n", &K, &sz);

		S = sz;

		Solve();

		printf("Case #%d: %d\n", i, MinSol);
	}

	fclose(stdout);
	fclose(stdin);


	return 0;
}
