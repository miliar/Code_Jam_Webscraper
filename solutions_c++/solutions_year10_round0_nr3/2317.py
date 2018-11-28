#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream cin("c.small.in");
	ofstream cout("c.small.out");

	int cases = 0;
	cin >> cases;
	for(int i = 0; i < cases; ++i)
	{
		int rounds			= 0;
		int capacity		= 0;
		int num_of_groups	= 0;

		cin >> rounds >> capacity >> num_of_groups;

		vector<int> groups(num_of_groups);
		for(int j = 0; j < num_of_groups; ++j)
		{
			cin >> groups[j];
		}
		vector<pair<int, int> > dp(num_of_groups);
		for(int j = 0; j < num_of_groups; ++j)
		{
			int utilization = groups[j];
			int k = j + 1;
			for(; k != j; ++k)
			{
				if(k == num_of_groups)
				{
					k = 0;
					if(k == j)
					{
						break;
					}
				}
				if((utilization + groups[k]) > capacity)
				{
					break;
				}

				utilization += groups[k];
			}
			dp[j] = pair<int, int>(k, utilization);
		}
		int income = 0;
		int front = 0;
		for(int j = 0; j < rounds; ++j)
		{
			income += dp[front].second;
			front = dp[front].first;
		}
		cout << "Case #" << i + 1 << ": " << income << endl;
	}

	return 0;
}