#include<stdio.h>

#define MAX_N 20
#define PATRICK 0
#define SEAN 1

unsigned int N, Values[MAX_N];
unsigned int Use[MAX_N];
unsigned int Max_Sean_Sum;
unsigned int First = 1;

void read_input()
{
	scanf("%u\n", &N);
	for (int n = 0; n < N; n++)
		scanf("%u", Values + n);
	scanf("\n");
}

unsigned int sean_sum()
{
	unsigned int ret = 0;
	for (int x = 0; x < N; x++)
		if (Use[x] == SEAN)
			ret += Values[x];
	return ret;
}

unsigned int patrick_difference()
{
	unsigned int p = 0;
	for (int x = 0; x < N; x++)
		if (Use[x] == PATRICK)
			p ^= Values[x];

	unsigned int s = 0;
	for (int x = 0; x < N; x++)
		if (Use[x] == SEAN)
			s ^= Values[x];

	return (p > s) ? (p - s) : (s - p);
}


unsigned int num_of_candies(int who)
{
	unsigned int ret = 0;
	for (int x = 0; x < N; x++)
		if (Use[x] == who)
			ret++;
	return ret;
}

void go(int j)
{
	if (j == N)
	{
		unsigned int pd = patrick_difference();
		if (pd == 0 && num_of_candies(PATRICK) > 0 && num_of_candies(SEAN) > 0)
		{
			unsigned int s = sean_sum();
			if (s > Max_Sean_Sum || First == 1)
			{
				Max_Sean_Sum = s;
				First = 0;
			}
		}
		return;
	}
	Use[j] = PATRICK;
	go(j + 1);
	Use[j] = SEAN;
	go(j + 1);
	return;
}

void process()
{
	Max_Sean_Sum = 0;
	First = 1;
	go(0);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++)
	{
		read_input();

		process();
		printf("Case #%d: ", t);
		if (First == 1)
			printf("NO\n");
		else
			printf("%u\n", Max_Sean_Sum);

	}
	return 0;
}