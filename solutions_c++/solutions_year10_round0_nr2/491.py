#include <iostream>
#include <algorithm>
using namespace std;
int t , n  , i , j , mx , cnt;
long long a[4000];

long long g(long long a , long long b)
{
	if (b == 0) return a; else
		return g(b , a % b);
}

int main()
{
	freopen("d:/input.txt" , "r" , stdin);
	freopen("d:/output.txt" , "w" , stdout);
	cin>>t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin>>n;
		for (i = 0; i < n; i++)
			cin>>a[i];

		sort(a , a + n);

		long long ans = a[1] - a[0];

		for (i = 0; i < n - 1; i++)
				ans = g(ans , a[i+1] - a[i]);

		if (a[0] % ans == 0)
			ans = 0; else
			ans = ans - a[0] % ans;

		cout<<"Case #"<<tt<<": "<<ans<<endl;
		
		

	}

	

	return 0;
}