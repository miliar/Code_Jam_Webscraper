#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T(0);
	cin >> T;
	for(int t(0); t < T; ++t)
	{
		int N(0);
		cin >> N;
		vector<int> candy(N,0);
		int X(0);

		for(int i(0); i < N; ++i)
		{
			cin >> candy[i];
			X ^= candy[i];
		}
		if(X != 0)
			cout << "Case #" << t + 1 << ": NO" << endl;
		else
		{
			sort(candy.begin(), candy.end());
			int Y(candy[0]);
			X = X ^ candy[0];
			int count(1);
			while(X != Y && count < N)
			{
				X ^= candy[count];
				Y ^= candy[count];
				++count;
			}
			int sum(0);
			for(int i(count); i < N; ++i)
			{
				sum += candy[i];
			}
			cout << "Case #" << t + 1 << ": " << sum << endl;
		}
	}
	return 0;
}