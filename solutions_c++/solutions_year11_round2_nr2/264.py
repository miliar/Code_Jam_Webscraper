#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N, D;

int go(double v, vector<pair<int, int> > &data)
{
	double leftmost = -1e200;

	for (int i = 0;i < N;i++)
	{
		int start_pos = data[i].first;
		int cnt = data[i].second;

		double left_next = leftmost + D;
		double possible_left = start_pos - v;

		double real_left = max(possible_left, left_next);
		double real_right = real_left + D * (cnt - 1);
		if (real_right - start_pos > v)
			return false;

		leftmost = real_right;
	}
	return true;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int ti = 1;ti <= t;ti++)
	{
		fprintf(stderr, "Case #%d\n", ti);
		vector<pair<int, int> > data;
		scanf("%d %d", &N, &D);
		for (int i = 0;i < N;i++)
		{
			int p, q;
			scanf("%d %d", &p, &q);
			data.push_back(make_pair(p, q));
		}
		sort(data.begin(), data.end());

		double st = 0;
		double ed = 1e100;

		for (int it = 0;it < 500;it++)
		{
			double mid = (st + ed) / 2;
			if (go(mid, data))
				ed = mid;
			else
				st = mid;
		}
		
		printf("Case #%d: %f\n", ti, (st + ed) / 2);
	}
	return 0;
}
