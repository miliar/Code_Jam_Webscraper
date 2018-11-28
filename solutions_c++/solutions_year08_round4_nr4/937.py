#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <algorithm>

using namespace std;

int n;
int k;
char s[1001];
int perm[5];
int best = -1;
int ans;

void Init()
{
	 k = 0;
	 best = -1;
	 memset(s, 0, sizeof(s));
	 for (int i = 0; i < 5; i++)
		 perm[i] = i;
}

int Fact(int q)
{
	int rez = 1;
	for (int i = 1; i <= q; i++)
		rez *= i;
	return rez;
}

void DoIt()
{
	char tmp[1001];
	strcpy(tmp, s);
	for (int i = 0; i < strlen(s) / k; i++)
	{
		for (int j = 0; j < k; j++)
		{
			tmp[i * k + j] = s[k * i + perm[j]]; 
		}
	}
	ans = 0;
	int q = 1;
	char old = tmp[0];
	while(q < strlen(tmp))
	{
		if (tmp[q] != old)
		{
			ans++;
			old = tmp[q];
		}
		q++;
	}
	if (old == tmp[strlen(tmp) - 1])
		ans++;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n ; i++)
	{
		Init();
		scanf("%d", &k);
		scanf("%s", &s);
		for (int i = 0; i < Fact(k); i++)
		{
			DoIt();
			if (best == -1 || ans < best)
				best = ans;

			next_permutation(perm, perm + k);
		}
		printf("Case #%d: %d\n", i + 1, best);
	}
	return 0;
}