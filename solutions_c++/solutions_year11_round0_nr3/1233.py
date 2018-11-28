#include<iostream>
using namespace std;
int t,n;
int a[2000];
int ans;
int min1;
int total;
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out","w",stdout);
	cin >> t;
	for (int l = 1 ; l <= t; ++l)
	{
		cin >> n;
		ans = 0;
		total = 0;
		min1 = 10000000;
		for (int i = 0; i <n; ++i)
		{
			cin >> a[i];
			ans = ans ^ a[i];
			if (a[i] < min1)
			min1 =a[i];
			total += a[i];
		}
		if (ans != 0)
		{
			cout << "Case #"<<l<<": NO"<<endl;
		}
		else
		{
			cout << "Case #"<<l<<": "<<total-min1<<endl;
		}
	}
	return 0;
}
