#include <algorithm>
#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

int t, r, k, n;
int groups[1020];
unsigned long int ans;

void solve()
{
	queue<int> q;
	for(int i = 0; i < n; i++)
		q.push(groups[i]);
	int sum = 0;
	for(int i = 0; i < r; i++)
	{
		int nGroups = 0;
		while(sum + q.front() <= k && nGroups < n)
		{
			sum += q.front();
			q.push(q.front());
			q.pop();
			nGroups++;
		}
		ans += sum;
		sum = 0;
	}
}

int main()
{
	scanf("%d", &t);
	int nCase = 1;
	for(int i = 0; i < t; i++)
	{
		scanf("%d %d %d", &r, &k, &n);
		ans = 0;
		for(int i = 0; i < n; i++)
			groups[i] = 0;
		for(int i = 0; i < n; i++)
			scanf("%d", &groups[i]);
		solve();
		printf("Case #%d: %u\n", nCase++, ans);
	}
} 
