#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	//freopen("test.in", "w", stdout);
	long long r,k,n,t;
	long long buf;
	scanf("%lld", &t);
	long long count = 0;
	long long sum = 0;
	vector <long long> q;
	for(int i = 0; i < t; i++)
	{
		count = 0;
		sum = 0;
		scanf("%lld%lld%lld", &r, &k, &n);
		q.clear();
		for (int j = 0; j < n; j++)
		{
			scanf("%lld", &buf);
			q.push_back(buf);
		}
		for (int j = 0; j < r; j++)
		{
			count = 0;
			for(int f = 0; f < q.size(); f++)
			{
				buf = q.front();
				count += buf;
				if (count > k)
				{	
					count -= buf;
					break;
				}
				q.erase(q.begin());
				sum += buf;
				q.push_back(buf);
			}
		}
		printf("Case #%d: %lld\n", i + 1, sum);

	}
	return 0;
}
