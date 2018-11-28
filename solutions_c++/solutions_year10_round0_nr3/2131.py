// TaskC
// MS Visual Studio 2008 Express Edition
// Theme Park

#include <iostream>
#include <vector>
using namespace std;


void read_groups(vector<int>& groups)
{
	for (unsigned int i = 0; i < groups.size(); ++i)
	{
		cin >> groups[i];
	}
}

int calc_profit(int R, int k, vector<int>& groups)
{
	int N = groups.size();
	int pos = 0;
	int money = 0;

	for (int i = 0; i < R; ++i)
	{
		int used_sits = 0;
		int groups_boarded = 0;
		while (used_sits <= (k - groups[pos]) && groups_boarded < N)
		{
			used_sits += groups[pos];
			pos = (pos + 1) % N;			
			groups_boarded++;
		}
		money += used_sits;
	}
	return money;
}

int main()
{
	int T = 0;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int R = 0, k = 0, N = 0;
		cin >> R >> k >> N;
		vector<int> groups;
		groups.resize(N, 0);
		read_groups(groups);
		std::cout << "Case #" << i << ": " << calc_profit(R, k, groups) << "\n";
	}
	return 0;
}

