#include <iostream>
using namespace std;

int abs(int a, int b)
{
	if (a > b)
		return a-b;
	return a+b;
}

int main()
{
	int cases;
	int n;
	char c;
	int place;
	int last_time;
	int pre_b, pre_o;

	freopen("C:\\Users\\Haojian\\Desktop\\A-small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\Haojian\\Desktop\\output.txt", "w", stdout);

	int num = 0;
	cin >> cases;
	while (cases--)
	{
		cin >> n;

		pre_b = 1; 
		pre_o = 1;
		last_time = 0;
		char pre = 0;
		int ans = 0;

		for (int i = 0; i < n; i++)
		{
			cin >> c >> place;
			if (pre != c)
			{
				if (c == 'O')
				{
					if (last_time >= abs(place - pre_o) )
					{
						last_time = 1;
						ans++;
						pre_o = place;
					}
					else
					{
						last_time = abs(place - pre_o) - last_time + 1;
						ans += last_time;
						pre_o = place;
					}
				}
				else
				{
					if (last_time >= abs(place - pre_b) )
					{
						last_time = 1;
						ans++;
						pre_b = place;
					}
					else
					{
						last_time = abs(place - pre_b) - last_time + 1;
						ans += last_time;
						pre_b = place;
					}		 
				}
				
			}
			else
			{
				if (c == 'O')
				{
					last_time = last_time + abs(place - pre_o) + 1;
					ans += abs(place - pre_o) + 1;
					pre_o = place;
				}
				else
				{
					last_time = last_time + abs(place - pre_b) + 1;
					ans += abs(place - pre_b) + 1;
					pre_b = place;
				}
				
			}
			pre = c;
		}

	num++;
	printf("Case #%d: %d\n", num, ans);
	}
	return 0;
}