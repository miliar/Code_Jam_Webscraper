#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int Prime[1 << 20];

void PreWork()
{
	for (int i = 2; i < (1 << 20); i ++)
		for (int j = i + i; j < (1 << 20); j += i)
			Prime[j] = 1;
}

void Work()
{
	unsigned long long N;
	cin >> N;
	if (N == 1)
	{
		cout << 0 << endl;
		return;
	}
	unsigned long long Ans = 1;
	for (int i = 2; i * i <= N; i ++)
	{
		if (Prime[i])
			continue;
		unsigned long long t = i;
		while (t * i <= N)
		{
			t *= (unsigned long long) i;
			Ans ++;
		}
	}
	cout << Ans << endl;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	PreWork();
	int Cases;
	scanf("%d", &Cases);
	for (int i = 1; i <= Cases; i ++)
	{
		printf("Case #%d: ", i);
		Work();
	}
	return 0;
}