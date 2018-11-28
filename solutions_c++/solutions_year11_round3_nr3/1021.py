#include<iostream>
bool flag;
int t, n, l,h;
int a[10010];
int ans;
using namespace std;

int main()
{
		freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin >> t;
	for (int st = 1; st <= t; ++st)
	{
		cin >> n >> l >> h;
		for (int i = 0 ; i < n; ++i)
		{
			cin >> a[i];
		}
		ans = -1;
		for (int i = l; i <= h; ++i)
		{
			if (ans != -1 ) break;
			flag = true;
			for (int j = 0 ; j < n; j++)
			{
				if (i > a[j])
				{
					if (i % a[j] != 0)
					{
						flag =false;
						break;
					}
				}
				else
				{
					if (a[j] % i != 0)
					{
						flag =false;
						break;
					}
				}
			}
			if (flag)
			{
				ans = i;
				break;
			}
		}
		printf("Case #%d: " ,st);
		if (ans == -1)
		cout << "NO" << endl;
		else
		{
			cout << ans <<endl;
		}
	}
	return 0;
}
