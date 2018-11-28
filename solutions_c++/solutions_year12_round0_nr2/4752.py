#include <iostream>

using namespace std;

int main()
{
	int t, n, s, p, k = 1;
	cin >> t;
	while(t--)
	{
		cin >> n >> s >> p;
		int c = 0;
		int a[n];
		for(int i = 0; i < n; i++)
			cin >> a[i];
		for(int i = 0; i < n; i++)
		{
			if(a[i] == 0 && p == 0)
			{
				c++;
				continue;
			}
			else if(a[i] == 0)
				continue;
			if(a[i] % 3 == 0)
			{
				if(a[i] / 3 >= p)
					c++;
				else if(a[i] / 3 + 1 >= p && s > 0)
				{
					c++;
					s--;
				}
			}
			else if(a[i] % 3 == 1)
			{
				if(a[i] / 3 + 1 >= p)
					c++;
			}
			else
			{
				if(a[i] / 3 + 1 >= p)
					c++;
				else if(a[i] / 3 + 2 >= p && s > 0)
				{
					c++;
					s--;
				}
			}
		}
		cout << "Case #" << k << ": " << c << endl;
		k++;
	}
	return 0;
}

