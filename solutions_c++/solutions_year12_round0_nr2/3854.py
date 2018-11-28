#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		int n, s, p, sum = 0, num[100] = {}, ans[100] = {};
		cin >> n >> s >> p;
		for(int j = 0; j < n; j++)
			cin >> num[j];
		for(int j = 0; j < n; j++)
		{
			int tmp = num[j] / 3;
			if(tmp >= p)
				ans[j]++;
			else if((tmp + 1) >= p && ((tmp * 2 + tmp + 1) == num[j] || ((tmp + 1) * 2 + tmp == num[j])))
				ans[j]++;
			else if((tmp + 2) >= p && (tmp * 2 + tmp + 2) == num[j] && s)
			{
				ans[j]++;
				s--;
			}
			else if((tmp + 2) >= p && ((tmp + 2) * 2 + tmp) == num[j] && s)
			{
				ans[j]++;
				s--;
			}
			else
			{
				tmp = num[j] / 4;
				if((tmp * 3 + 3) == num[j] && (tmp + 2) >= p && s)
				{
					ans[j]++;
					s--;
				}
				tmp++;
				if((tmp * 3 + 3) == num[j] && (tmp + 2) >= p && s)
				{
					ans[j]++;
					s--;
				}
			}
			if(ans[j])
				sum++;
		}
		cout << "Case #" << i << ": " << sum << endl;
	}
	return 0;
}