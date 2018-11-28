#include <iostream>
#include <cstdio>
using namespace std;

const int MaxN = 501;
const int MaxK = 19;
char* W = "welcome to code jam";

int cache[MaxN][MaxK];
bool flag[MaxN][MaxK];

char lajn[MaxN];
int len;

int t;

int memoiz(int n, int k)
{
	if (k == MaxK)
		return 1;
	else if (len == n)
		return 0;
	else if (flag[n][k])
		return cache[n][k];
	else
	{
		int res = memoiz(n + 1, k) % 1000;
		if (W[k] == lajn[n])
			res += memoiz(n + 1, k + 1) % 1000;

		res %= 1000;

		flag[n][k] = true;
		cache[n][k] = res;

		return res;
	}
}

int main()
{
	FILE *fin = fopen("C-small.in", "r");
	FILE *fout = fopen("w-small.out", "w");

	fscanf(fin, "%ld\n", &t);
	for (int i = 1; i <= t; i++)
	{
		fgets(lajn, sizeof(lajn), fin);
		len = strlen(lajn);

		memset(flag, 0, sizeof(flag));
		int rez = memoiz(0, 0);

		fprintf(fout, "Case #%ld: %d%d%d%d\n", i, rez/1000, (rez/100)%10, (rez/10)%10, rez%10);
	}

	fclose(fin);
	fclose(fout);
}

