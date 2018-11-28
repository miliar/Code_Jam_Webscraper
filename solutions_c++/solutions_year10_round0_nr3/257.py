#include <iostream>
#include <cstring>

using namespace std;


long long times[1001];
long long cost[1001];
int groups[1001];

int Next(int start, int n, long long limit, long long & tot)
{
	tot = 0;
	int i;
	for (i = start; i < n; i++)
	{
		tot += groups[i];
		if (tot > limit)
		{
			tot -= groups[i];
			break;
		}
	}
	if (i >= n)
	{
		for (i = 0; i < start; i++)
		{
			tot += groups[i];
			if (tot > limit)
			{
				tot -= groups[i];
				break;
			}
		}
	}
	return i;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cases;
	cin>>cases;
	for (int t = 1; t <= cases; t++)
	{
		memset(times, 0xff, sizeof(times));
		memset(cost, 0xff, sizeof(cost));
		
		long long r, k, n;
		long long total = 0;
		cin >> r >> k >> n;
		cost[0] = 0;
		times[0] = r;
		for (int i = 0; i < n; i++) { cin>>groups[i]; }
		int next = 0;
		while(r > 0)
		{
			long long tot = 0;
			r--;
			next = Next(next, n, k, tot);
			total += tot;
			if (times[next] != -1)
			{ // found it!
				total += (total - cost[next]) * (r / (times[next] - r));
				r %= (times[next] - r);
				while (r > 0)
				{
					r--;
					next = Next(next, n, k, tot);
					total += tot;
				}
			}
			else
			{
				times[next] = r;
				cost[next] = total;
			}
		}
		cout << "Case #" << t << ": " << total << endl;
	}
	return 0;
}