#include <iostream>
#include <algorithm>

#define MAXN 1001

using namespace std;

int main()
{
	int t, T, sum, minv, resx;
	int N, i, n;
	cin >> T;
	for (t = 0; t < T; ++t)
	{
		resx = sum = 0;
		minv = -1;
		cin >> N;
		for (i = 0; i < N; ++i)
		{
			cin >> n;
			sum += n;
			resx ^= n;
			if ((minv == -1) || (n < minv))
				minv = n;
		}
		cout << "Case #" << t+1 << ": ";
		if (resx != 0)
			cout << "NO" << endl;
		else
			cout << sum-minv << endl;
	}
	return 0;
}