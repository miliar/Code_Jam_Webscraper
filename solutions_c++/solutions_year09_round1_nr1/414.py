#include <stdio.h>
#include <string.h>

#define maxs (2000005)
#define maxn (11)
#define maxl (64)

int V[maxs][maxn];

int base[maxn];
int bn;

char S[maxl];

int ub;

int test(int num)
{
	if(num >= 100000)
	{
		int t = num;
		int sum = 0;

		while(t > 0)
		{
			int d = t % ub;
			sum += d * d;
			t /= ub;
		}

		int res = test(sum);

		return res;
	}
	else if(V[num][ub] == 0)
	{
		V[num][ub] = 1;

		int t = num;
		int sum = 0;

		while(t > 0)
		{
			int d = t % ub;
			sum += d * d;
			t /= ub;
		}

		int res = test(sum);

		if(res == 1)
			V[num][ub] = 2;

		return res;
	}
	else if(V[num][ub] == 1)
		return 0;
	else
		return 1;
}

int main()
{
	int T, t1;
	int i, j, k;

	scanf("%d", &T);

	for(i = 2; i <= 10; ++i)
	{
		V[1][i] = 2;
	}

	for(t1 = 1; t1 <= T; ++t1)
	{
		scanf("\n%[^\n]", S);

//		printf("read\n");

		for(j = 0; S[j]; ++j);

		for(k = i = 0; i < j; i += 2)
		{
			if(S[i] >= '2')
			{
				base[k++] = S[i] - '0';
			}
			else
			{
				base[k++] = 10;
			}

//			printf("%d ", base[k - 1]);
		}
//		printf("\n");

		bn = k;

		for(i = 2; 1; ++i)
		{
			for(j = 0; j < bn; ++j)
			{
				ub = base[j];
				if(!test(i))
					break;
			}

			if(j == bn)
			{
				printf("Case #%d: %d\n", t1, i);
				break;
			}
		}
	}

/*
	for(i = 2; i <= 200; ++i)
	{
		for(j = 2; j <= 10; ++j)
		{
			printf("%d", V[i][j]);
		}
		printf("\n");
	}
//*/

	return 0;
}
