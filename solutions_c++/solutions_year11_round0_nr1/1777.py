#include <vector>
#include <iostream>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T(0);
	cin >> T;
	for(int t(0); t < T; ++t)
	{
		int N(0);
		cin >> N;
		int Blue(0);
		int Orange(0);
		int ans(0);
		int pB(1);
		int pO(1);
		char robot;
		int button;
		bool B(false);
		bool O(false);
		int time(0);
		for(int i(0); i < N; ++i)
		{
			cin >> robot >> button;
			if(robot == 'B')
			{
				int cur(abs(button - pB) + 1);
				if(Blue + cur <= time)
				{
					ans++;
					time++;
					Blue = time;
				}
				else
				{
					ans += (cur + Blue - time);
					time = cur + Blue;
					Blue = time;
				}
				pB = button;
			}
			else
			{			
				int cur(abs(button - pO) + 1);
				if(Orange + cur <= time)
				{
					ans++;
					time++;
					Orange = time;
				}
				else
				{
					ans += (cur + Orange - time);
					time = cur + Orange;
					Orange = time;
				}
				pO = button;
			}
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}