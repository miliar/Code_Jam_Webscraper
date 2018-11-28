#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <vector>
using namespace std;
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define eps 1e-9
#define f0(i,n) for (i = 0; i < n; i++)



int n , m , k , i , j , p , t , x , tm;
int a[1000] , v[1000] , b[1000];

int main()
{
	freopen("d:/input.txt" , "r" , stdin);
	freopen("d:/output.txt" , "w" , stdout);
	
	cin>>t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin>>n>>k>>x>>tm;
		for (i = 0; i < n; i++)
			cin>>a[i];

		for (i = 0; i < n; i++)
			cin>>v[i];

	int sum = 0;
	for (i = 0; i < n; i++)
		b[i] = 0;
		for (i = n-1; i >= 0; i--)
		{
			if (sum == k) break;
			if (1.0 * (x - a[i]) / v[i] - 1e-9 < tm)
				b[i] = 1 , sum++;
		}
		

		int ans = 0;
		for (i = 0; i < n; i++)
		{
			if (b[i])
				for (j = i + 1; j < n; j++)
					if (b[j] == 0)
						ans++;
		}

		cout<<"Case #"<<tt<<": ";
		if (sum < k)
			cout<<"IMPOSSIBLE\n"; else
			cout<<ans<<endl;
	}
	
	return 0;
}