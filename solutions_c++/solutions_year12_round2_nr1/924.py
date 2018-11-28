#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>

using namespace std;

double const eps = 10e-6;
int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N;
		cin >> N;
		vector<pair<int, int> > vec(N + 1);
		double sum = 0;
		for (int i = 0; i < N; i++)
		{
			int val;
			cin >> val;
			sum += val;
			vec[i] = make_pair(i, val);
		}
		vec[N] = make_pair(N, 1000000);
		vector<double> ps(N);

		printf("Case #%d: ", t);
		sort(vec.begin(), vec.end(), [](pair<int, int> const& p1, pair<int, int> const& p2)
			{
				return p1.second > p2.second;
			});
		
		int pos = N;
		int cnt = 1;
		double ts = sum;
		while (abs(sum) > eps && pos > 0)
		{
			while (vec[pos] == vec[pos - 1])
			{
				cnt++;
				pos--;
			}

			double dif = vec[pos - 1].second - vec[pos].second;
			double p = 0;
			if (cnt * dif > sum)
			{
				p = sum / ts;
				p /= cnt;
				sum = 0;
			}
			else
			{
				sum -= cnt * dif;
				p = dif /ts;
			}

			for (int i = 0; i < cnt; i++)
			{
				ps[vec[N - i].first] += p;
			}

			pos--;
			cnt++;
		}

		for (int i = 0; i < N; i++)
		{
			printf("%f ", 100 * ps[i]);
		}

		printf("\n");
	}

	return 0;
}