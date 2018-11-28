#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n;
		cin >> n;
		double s[200];
		double sum = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> s[i];
			sum += s[i];
		}
		cout << "Case #" << (t+1) << ":";
		cout << fixed;
		for (int i = 0; i < n; ++i)
		{
			double low = 0.0;
			double high = 1.0;
			while (low + 1e-9 < high)
			{
				double mid = (low+high)/2;
				double myPoint = s[i] + mid * sum;
				double votesLeft = (1.0 - mid) * sum;
				for (int j = 0; j < n; ++j)
				{
					if (i == j)
						continue;
					if (s[j] < myPoint)
						votesLeft -= myPoint - s[j];
				}
				if (votesLeft < 0)
					high = mid;
				else
					low = mid;
			}
			cout << " " << setprecision(6) << 100.0*(low+high)/2;
		}
		cout << endl;
	}
	return 0;
}
