#include <stdio.h>

int C;
int N,K,B,T;
int haalbaar[50];
int pos[50];
int speed[50];

void solve(int num)
{
	int t = 0;
	for (int i = 0; i < N; i++)
	{
		if (pos[i] + speed[i] * T < B)
			haalbaar[i] = 0;
		else
		{
			haalbaar[i] = 1;
			t++;
		}
	}
	if (t < K)
		printf("Case #%d: IMPOSSIBLE\n", num);
	else
	{
		t = 0;
		int j = 0;
		int add = 0;
		for (int i = N - 1; j < K; i--)
		{
			if (haalbaar[i] == 1)
			{
				j++;
				t += add;
			}
			else
			{
				add++;
			}
		}
		printf("Case #%d: %d\n", num, t);
	}
	/*for (int i = 0; i < N; i++)
		printf("Haalbaar[%d] = %d\n", i, haalbaar[i]);*/
}

int main()
{
	scanf("%d", &C);
	for (int i = 0; i < C; i++)
	{
		scanf("%d %d %d %d", &N, &K, &B, &T);
		for (int j = 0; j < N; j++)
		{
			int temp;
			scanf("%d", &temp);
			pos[j] = temp;
		}
		for (int j = 0; j < N; j++)
		{
			int temp;
			scanf("%d", &temp);
			speed[j] = temp;
		}
		solve(i + 1);
	}
	return 0;
}

