#include <iostream>

using namespace std;

const long long oo = 1000000000LL * 1000000000LL;

int n;
double d;
double pos[256];
int num[256];

bool check(double time)
{
	double rightmost = -1e100;
	for (int i = 0; i < n; i++)
	{
		rightmost = max(rightmost + d, pos[i] - time) + (num[i] - 1) * d;
		if (rightmost > pos[i] + time)
			return false;
	}
	return true;
}

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		cin >> n >> d;
		d *= 2;
		for (int i = 0; i < n; i++)
		{
			cin >> pos[i] >> num[i];
			pos[i] *= 2;
		}
		double lower = 0, upper = 1;
		while (!check(upper))
			upper *= 2;
		while (upper > lower + 1)
		{
			double mid = (lower + upper) / 2;
			if (!check(mid))
				lower = mid;
			else
				upper = mid;
		}
//		cout << "Case #" << kase << ": " << (check(0) ? 0.0 : .5 * (double)upper) << endl;
		printf("Case #%d: %.1lf\n", kase, check(0) ? 0.0 : .5 * (double)upper);
	}
	return 0;
}
