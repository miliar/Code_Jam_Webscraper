#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <queue>

using namespace std;

int main()
{
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t, n, temp;
	int r, k;
	int peoples;
	long long res;
	int num;
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++)
	{	
		res = 0;
		scanf("%d%d%d", &r, &k, &n);	
		queue <int> q;
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &temp);
			q.push(temp);
		}

		for (int j = 0; j < r; j++)
		{
			peoples = 0;
			num = 0;
			while (peoples + q.front() <= k && num < n) 
			{
				peoples += q.front();
				num++;
				q.push(q.front());
				q.pop();
			}
			res += peoples;
		}
		printf("Case #%d: %lld\n", i+1, res);
	}

	return 0;
}