#include <stdio.h>

int T,n;
int set[30];
int mem[30];

int check(int b)
{
	if (b == 1)
		return 1;
	if (set[b] == 0)
		return 0;
	int t = 0;
	for (int i = 0; i <= b; i++)
	{
		if (set[i] == 1)
			t++;
	}
	return check(t);
}	

int recurs(int d)
{
	int t = 0;
	if (d == n)
	{
		return check(n);
	}
	t = recurs(d + 1);
	set[d] = 1;
	t += recurs(d + 1);
	set[d] = 0;
	return t % 100003;
}

void solve(int num)
{
	for (int i = 0; i < 30; i++)
	{
		set[i] = 0;
	}
	set[n] = 1;
	int t;
	if (mem[n] == -1)
	{
		t = recurs(2);
		mem[n] = t;
	}
	else
		t = mem[n];
	printf("Case #%d: %d\n", num, t);
}

int main()
{
	scanf("%d", &T);
	for (int i = 0; i < 30; i++)
		mem[i] = -1;
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &n);
		solve(i + 1);
	}
	return 0;
}

