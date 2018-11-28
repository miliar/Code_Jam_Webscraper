#include<iostream>
using namespace std;
int t, n ,a[1020],ini[1020];
double ans;
int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out","w",stdout);
	cin >> t;
	for (int l = 1 ; l <= t; ++l)
	{
		cin >> n;
		ans = 0;
		for (int i = 0; i < n ; ++ i)
		{
			cin >> a[i];
			ini[i] = a[i];
		}
		sort(a, a+n);
		for (int i = 0  ; i < n; ++i)
		{
			if (ini[i] != a[i])
			{
				ans +=1;
			}
		}
		cout << "Case #"<<l<<": ";
		printf("%.6f\n",ans);
	}
	return 0;
}
