#include <iostream>
#include <sstream>

#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cmath>

using namespace std;

int readInt()
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	int ans = 0;
	ss >> ans;

	return ans;
}

int main(int argc, char* argv[])
{
	int C = readInt();
	for (int test = 1; test <= C; ++test)
	{
		int N;
		cin >> N;
		vector<long double> x(N), y(N), R(N);
		for (int i = 0; i < N; ++i)
			cin >> x[i] >> y[i] >> R[i];

		long double ans = 1000000000.0;
		if (N == 3)
		{
			for (int i = 0; i < N; ++i)
				for (int j = i + 1; j < N; ++j)
					if ((sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])) + R[i] + R[j])/2.0 < ans &&
						R[3-i-j] < ans)
						ans = max((sqrt((x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])) + R[i] + R[j]) / 2.0, R[3-i-j]);
		}
		else if (N == 1)
			ans = R[0];
		else if (N == 2)
		{
			ans = (sqrt((x[0] - x[1])*(x[0] - x[1]) + (y[0] - y[1]) * (y[0] - y[1])) + R[0] + R[1]) / 2.0;
			ans = min(ans, max(R[0], R[1]));
		}

		cout << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}
