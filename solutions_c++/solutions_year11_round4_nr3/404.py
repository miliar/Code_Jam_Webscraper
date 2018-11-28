#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#define maxN 1000000

using namespace std;

long long N;
bool Flag[maxN + 1];
int prime[maxN], pc = 0;

int main()
{
	memset(Flag, 0, sizeof Flag);
	for (int i = 2; i <= maxN; i++)
		if (!Flag[i])
		{
			prime[pc++] = i;
			for (int j = 2; i * j <= maxN; j++)
				Flag[i * j] = true;
		}
	int T;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		cin >> N;
		long long ans = 0;
		for (int i = 0; i < pc; i++)
		{
			long long cur = 0, tmp = prime[i];
			while (tmp <= N)
			{
				cur++;
				tmp *= (long long) prime[i];
			}
			if (cur > 0)
				ans += cur - 1;
		}
		if (N != 1)
			ans++;
		printf("Case #%d: ", z);
		cout << ans << endl;
	}
	return 0;
}
