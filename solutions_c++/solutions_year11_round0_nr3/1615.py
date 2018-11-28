#include <iostream>
#include <cstdlib>
#include <memory.h>
using namespace std;

#define N 21
int a[1001];
int cnt[N];
int n;

int cmp(const void *a, const void * b)
{
	return *((int *)a) - *((int *)b);
}

int Solve()
{
	memset(cnt, 0, sizeof(cnt));
	int i, j;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < N; j++)
			if((a[i] >> j) & 1 == 1)
				cnt[j]++;
	}
	for(i = 0; i < N; i++)
		if(cnt[i] % 2 != 0)
			return -1;

	int sum = 0;
	for(i = 0; i < n; i++)
		sum += a[i];

/*	int subsum = 0;
	for(i = 0; i < N; i++)
	{
		if(cnt[i])// there exsit a number
		{
			for(j = 0; j < n; j++)
				if((a[j] >> j) & 1 == 1)
				{
					subsum += a[j];
					break;
				}
		}
	}*/
	return sum - a[0];
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("outcL.txt", "w", stdout);
	int cas;
	cin >> cas;
	for(int i = 1; i <= cas ; i++)
	{
		cin >> n;
		for(int j = 0; j < n; j++)
			cin >> a[j];

		qsort(a, n ,sizeof(int), cmp);

		int res = Solve();
		cout << "Case #" << i << ": ";
		if(res >= 0)
			cout << res <<endl;
		else
			cout << "NO"<<endl;

	}
	return 0;
}