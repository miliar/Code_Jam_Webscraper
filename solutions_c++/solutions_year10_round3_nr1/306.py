#include<iostream>
using namespace std;
int t,n;
int a[2000],b[2000];
int ans = 0;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	for (int test = 1; test <= t; test++)
	{
		cin >> n;
		for (int i = 0 ; i< n ; i++)
		cin >> a[i]>>b[i];
		ans = 0;
		for (int i = 0 ; i< n ; i++)
		for (int j = i+1 ; j<n; j++)
		{
			if (i==j) continue;
			if ((a[i]-a[j])*(b[i]-b[j])<0)
			++ans;
		}
		cout <<"Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}
