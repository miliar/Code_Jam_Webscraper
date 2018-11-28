#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#define maxN 1000

using namespace std;

int type[maxN], num[maxN];
int N;

int main()
{
	int T, z;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		cin >> N;
		for (int i = 0; i < N; i++)
		{
			char c;
			cin >> c >> num[i];
			if (c == 'O')
				type[i] = 0;
			else
				type[i] = 1;
		}
		int ans = 0, p[2] = {1, 1}, r[2] = {0, 0};
		for (int i = 0; i < N; i++)
		{
			int need = abs(num[i] - p[type[i]]);
			if (need > r[type[i]])
			{
				r[!type[i]] += need - r[type[i]];
				ans += need - r[type[i]];
			}
			r[type[i]] = 0;
			r[!type[i]] ++;
			p[type[i]] = num[i];
			ans++;
		}
		printf("Case #%d: %d\n", z, ans);
	}
	return 0;
}
