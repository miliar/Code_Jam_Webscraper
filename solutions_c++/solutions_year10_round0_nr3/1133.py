#include <iostream>

using namespace std;
int t , n  , i , j , mx , cnt;
int a[4000] , p[4000] , add[4000] , next[4000];
int main()
{
	freopen("d:/input.txt" , "r" , stdin);
	freopen("d:/output.txt" , "w" , stdout);
	cin>>t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin>>cnt>>mx>>n;
		for (i = 0; i < n; i++)
		{
			cin>>a[i];
			a[i+n] = a[i];
		}
		long long ans = 0;
		for (i = 0; i < n; i++)
		{
			j = i;
			int sum = 0;
			while (j < i + n && sum + a[j] <= mx)
			{
				sum += a[j];
				j++;
			}

			next[i] = (j) % n;
			add[i] = sum;

		}

		int st = 0;
		for (i = 0; i < cnt; i++)
		{
			ans += add[st];
			st = next[st];
		}

		cout<<"Case #"<<tt<<": "<<ans<<endl;
		
		

	}

	

	return 0;
}