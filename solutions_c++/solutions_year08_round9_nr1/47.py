#include <iostream>
#include <set>

using namespace std;

struct data
{
	int a, b, c;
};

bool	compareA(const data& x, const data& y)
{
	return x.a < y.a;
}

bool	compareB(const data& x, const data& y)
{
	return x.b < y.b;
}

int	now, task;
int	N;
data	x[10000], y[10000];

int	main()
{
	scanf("%d", &task);
	for (int now = 1; now <= task; ++now)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			scanf("%d%d%d", &x[i].a, &x[i].b, &x[i].c);
		sort(x, x + N, compareA);

		int rest = 10000;
		int ret = 0;
		multiset<int> setC;
		typedef multiset<int>::iterator MI;

		MI	p;
		for (int i = 0; i < N; ++i)
		{
			rest -= x[i].a;
			memcpy(y, x, sizeof(x));
			sort(y, y + i + 1, compareB);

			setC.clear();

			for (int j = 0; j <= i; ++j)
			{
				rest -= y[j].b;
				setC.insert(y[j].c);
				while (setC.size())
				{
					MI p = setC.end();
					--p;
					if (*p > rest)
						setC.erase(p);
					else
						break;
				}
				ret = max(ret, (int) setC.size());
				rest += y[j].b;
			}
			rest += x[i].a;
		}
		printf("Case #%d: %d\n", now, ret);
	}
	return 0;
}
