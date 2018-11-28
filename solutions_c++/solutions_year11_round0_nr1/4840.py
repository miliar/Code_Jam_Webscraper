#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		int N;
		cin >> N;
		int Op = 1;
		int Bp = 1;
		int OlastTime = 0;
		int BlastTime = 0;
		int ans = 0;
		for(int i = 0; i < N; ++i)
		{
			char clr;
			int bt;
			cin >> clr >> bt;
			if (clr == 'O')
			{
				int temp = abs(bt - Op); 
				Op = bt;
				temp -= ans - OlastTime;
				if (temp < 0)
				{
					temp = 0;
				}
				ans += temp + 1;
				OlastTime = ans;
			}
			else
			{
				int temp = abs(bt - Bp); 
				Bp = bt;
				temp -= ans - BlastTime;
				if (temp < 0)
				{
					temp = 0;
				}
				ans += temp + 1;
				BlastTime = ans;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}