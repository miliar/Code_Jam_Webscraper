# include <iostream>
# include <fstream>
# include <cmath>
# include <algorithm>
using namespace std;

int nonnegative(int x)
{
	return x < 0 ? 0 : x;
}

int main()
{
	ifstream cin ("A-in.txt");
	ofstream cout ("A-out.txt");
	int T;
	cin >> T;
	char r[110];
	int p[110];
	int n;
	int case_num = 0;
	while(T - case_num++ > 0)
	{
		int curO = 1;
		int bonusO = 0;
		int ans = 0;
		int curB = 1;
		int bonusB = 0;
		cin >> n;
		for(int i = 0; i < n; ++i)
		{
			cin >> r[i] >> p[i];
			if(r[i] == 'O')
			{
				ans += nonnegative(abs(curO - p[i]) - bonusO) + 1;
				bonusB += nonnegative(abs(curO - p[i]) - bonusO) + 1;
				bonusO = 0;
				curO = p[i];

			}
			else
			{
				ans += nonnegative(abs(curB - p[i]) - bonusB) + 1;
				bonusO += nonnegative(abs(curB - p[i]) - bonusB) + 1;
				bonusB = 0;
				curB = p[i];
			}
		}
		cout << "Case #" << case_num << ": " << ans << "\n";
	}
	return 0;
}
