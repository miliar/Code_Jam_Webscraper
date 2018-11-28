#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int p = 10007;
int inverses[15000];

int data[200][200];
int field[200][200];
int blockR[20];
int blockC[20];
const int SIZE = 100000000;
short fact[SIZE];

void computeInverses()
{
	int j, k;
	inverses[0] = 0;
	for (j = 1; j < p; j++)
		inverses[j] = 0;
	for (j = 1; j < p; j++)
	{
		if (inverses[j] == 0)
		{
			for (k = 1; k < p; k++)
			{
				if (j * k % p == 1)
				{
					inverses[j] = k;
					inverses[k] = j;
					break;
				}
			}
		}
	}
}

void computeFact()
{
	fact[0] = 1;
	fact[1] = 1;
	int i;
	for (i = 2; i < SIZE; i++)
	{
		int newVal;
		if (i % p == 0)
		{
			newVal = (int) (fact[i-1]) * (i / p);
		}
		else
		{
			newVal = (int) (fact[i-1]) * (i % p);
		}
		newVal %= p;
		fact[i] = (short) newVal;
	}
}

int getFact(int n)
{
	return fact[n];
}

int getNumP(int n)
{
	return n / p;
}

int comb(int t, int a, int b)
{
	int np = getNumP(t) - getNumP(a) - getNumP(b);
	if (np > 0)
		return 0;

	int ans = getFact(t);
	ans *= inverses[getFact(a)];
	ans %= p;
	ans *= inverses[getFact(b)];
	ans %= p;
	return ans;
}

int main()
{
	int numCase;
	scanf("%d", &numCase);
	int i, j, k;
	int r, c, nm;
	computeInverses();
	computeFact();
	for (i = 0; i < numCase; i++)
	{
		scanf("%d %d %d", &r, &c, &nm);
		for (j = 0; j < nm; j++)
		{
			scanf("%d %d", &blockR[j], &blockC[j]);
			blockR[j]--;
			blockC[j]--;
		}
		blockR[nm] = blockC[nm] = 0;
		blockR[nm+1] = r-1;
		blockC[nm+1] = c-1;
//		printf("%d %d\n", r-1, c-1);
		nm += 2;

		for (j = 0; j < nm; j++)
		{
			for (k = 0; k < nm-1; k++)
			{
				if (blockR[k] > blockR[k+1] || (blockR[k] == blockR[k+1] && blockC[k] > blockC[k+1]))
				{
					int tmp = blockR[k];
					blockR[k] = blockR[k+1];
					blockR[k+1] = tmp;
					tmp = blockC[k];
					blockC[k] = blockC[k+1];
					blockC[k+1] = tmp;
				}
			}
		}
/*		for (j = 0; j < nm; j++)
		{
			printf("%d %d\n", blockR[j], blockC[j]);
		}*/
//		printf("here\n");
		int ans = 0;
		int cto = (1 << nm);
		for (j = 0; j < cto; j++)
		{
			vector<int> ind;
			for (k = 0; k < nm; k++)
			{
				if ((j & (1 << k)) != 0)
					ind.push_back(k);
			}

			int len = ind.size();

			if (len < 2 || ind[0] != 0 || ind[len-1] != nm-1)
				continue;
			int smallAns = 1;
			for (k = 0; k < len-1; k++)
			{
				int x = blockR[ind[k+1]] - blockR[ind[k]];
				int y = blockC[ind[k+1]] - blockC[ind[k]];
//				printf("%d %d %d %d %d\n", k, x, y, blockC[ind[k+1]], blockC[ind[k]]);
				if ((2 * y - x) % 3 != 0 || (2 * x - y) % 3 != 0)
				{
					smallAns = 0;
					break;
				}
				int a = (2 * y - x) / 3;
				int b = (2 * x - y) / 3;
				if (a < 0 || b < 0)
				{
					smallAns = 0;
					break;
				}
				int t = a + b;
				int value = comb(t, a, b);
//				printf("%d %d %d %d\n", t, a, b, value);
				smallAns *= value;
				smallAns %= p;
			}
//			printf("%d %d\n", j, smallAns);
			if (len % 2 == 0)
				ans += smallAns;
			else
				ans -= smallAns;
			ans = (ans + p) % p;
		}

/*		for (j = 0; j < r; j++)
			for (k = 0; k < c; k++)
				field[j][k] = 0;
		for (j = 0; j < nm; j++)
		{
			int c1, c2;
			scanf("%d %d", &c1, &c2);
			field[c1-1][c2-1] = 1;
		}
		int numPos = 0;
		for (j = 0; j < r; j++)
			for (k = 0; k < c; k++)
			{
				if (j == 0 && k == 0)
					data[j][k] = 1;
				else
					data[j][k] = 0;
				if ((j != 0 || k != 0) && field[j][k] == 0)
				{
					if (j-2 >= 0 && k-1 >= 0)
						data[j][k] += data[j-2][k-1];
					if (j-1 >= 0 && k-2 >= 0)
						data[j][k] += data[j-1][k-2];
				}
				data[j][k] %= p;
//				printf("%d %d\n", j, k, data[j][k]);
			}*/
		printf("Case #%d: %d\n", i+1, ans);
//		exit(0);
	}

	return 0;
}
