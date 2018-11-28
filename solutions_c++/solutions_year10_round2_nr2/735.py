#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	int cases;
	cin >> cases;
	for(int ci = 0; ci < cases; ++ci)
	{
		long long n, k, b, t;
		cin >> n >> k >> b >> t;

		vector<long long> x_i(n, 0);
		for(int i = 0; i < n; ++i)
			cin >> x_i[i];
		for(int i = 0; i < n; ++i)
		{
			long long v_i;
			cin >> v_i;
			x_i[i] = (x_i[i] + v_i * t >= b);
		}

		long long slowies = 0;
		long long swaps = 0;

		for(long long i = n; ; )
		{
			if(!k)
			{
				cout << "Case #" << (ci + 1) << ": " << swaps << endl;
				break;
			}
			if(!i--)
			{
				cout << "Case #" << (ci + 1) << ": IMPOSSIBLE" << endl;
				break;
			}
			if(!x_i[i])
				++slowies;
			else
			{
				swaps += slowies;
				--k;
			}
		}
	}

	return 0;
}
