#include <iostream>
#include <vector>
#include <algorithm>

struct Q
{
	long long p, s;
	bool operator<(const Q &q) const
	{
		return p < q.p || (p == q.p && s > q.s);
	}
	long long cost;
};

int m,f,n;
std::vector<Q> q;

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		std::cin >> m >> f >> n;

		q.resize(n + 1);
		for (int i = 0 ; i < n ; ++i)
		{
			std::cin >> q[i].p >> q[i].s;
			++q[i].s;
		}
		q[n].s = 0;
		q[n].p = 0;
		std::sort(q.begin(), q.end());
		int next = 2;
		for (int i = 2 ; i <= n ; ++i)
		{
			q[next] = q[i];
			if (f + q[1].p > q[i].p	&& q[next-1].s < q[i].s)
			{
				++next;
			}
		}
		q.resize(next);
		q[0].cost = f;
		for (size_t i = 1 ; i < q.size() ; ++i)
		{
			q[i].cost = q[i-1].cost + (q[i].s - q[i-1].s) * q[i].p;
		}
		std::vector<long long> live(m + 1);
		for (long long i = 1 ; i <= m ; ++i)
		{
			for (size_t j = 1 ; j < q.size() ; ++j)
				if (i > q[j-1].cost)
				{
					long long sum = std::min(i, q[j].cost);
					long long d1 = (sum - q[j-1].cost) / q[j].p;
					long long days = q[j-1].s;
					//while (d1 > 0)
					{
						live[i] = std::max(live[i], live[i - (q[j-1].cost + q[j].p * d1)] + days + d1);
						//--d1;
					}
				}
				else
				{
					break;
				}
		}
		std::cout << "Case #" << t << ": " << live[m] << "\n";
	}
	return 0;
}

