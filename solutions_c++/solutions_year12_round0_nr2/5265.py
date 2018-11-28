#include <iostream>
#include <string>
using namespace std;

int main()
{
//	freopen("data", "r", stdin);
	int T, N, S, p;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		int cnt = 0;
		cin >> N >> S >> p;
		cout << "Case #" << t << ":" << " ";
		for(int i=0; i<N; i++)
		{
			int n;
			cin >> n;
			int ave = n / 3, left = n - ave * 3;
			if (left == 0)
			{
				if (ave >= p) cnt ++;
				else if (S > 0 && ave + 1 >= p && ave != 0)
				{
					S --;
					cnt ++;
				}
			} else if (left == 1)
			{
				if (ave + 1 >= p) cnt ++;
			} else if (left == 2)
			{
				if (ave + 1 >= p)
				{
					cnt ++;
				} else if (S >0 && ave + 2 >= p)
				{
					S --;
					cnt ++;
				}
			}
		}
		cout << cnt << endl;
	}
	return 0;
}
