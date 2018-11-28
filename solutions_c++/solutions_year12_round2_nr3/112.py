#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

const int maxSum = 2000000;
int num[maxSum+1];

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n;
		cin >> n;
		for (int i = 0; i <= maxSum; ++i)
			num[i] = -1;
		num[0] = 0;
		int ss[500];
		for (int i = 0; i < n; ++i)
			cin >> ss[i];
		cout << "Case #" << (t+1) << ":" << endl;
		for (int i = 0; i < n; ++i)
		{
			int s = ss[i];
			for (int j = 0; j <= maxSum; ++j)
			{
				if (num[j] != -1 && num[j] != s)
				{
					if (num[j + s] != -1)
					{
						// Print result
						{
							cout << s;
							int x = j;
							while (x != 0)
							{
								cout << " " << num[x];
								x -= num[x];
							}
							cout << endl;
						}
						{
							int x = j+s;
							cout << num[x];
							x -= num[x];
							while (x != 0)
							{
								cout << " " << num[x];
								x -= num[x];
							}
							cout << endl;
						}
						goto next_case;
					}
					num[j + s] = s;
				}
			}
		}
		cout << "Impossible" << endl;
next_case:
		;
	}
	return 0;
}
