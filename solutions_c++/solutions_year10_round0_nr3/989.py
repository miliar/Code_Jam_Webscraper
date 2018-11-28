#include <iostream>
#include <string.h>
#include <stdio.h>
#include <map>
#include <algorithm>
using namespace std;

 long long t[1010];

 long long gcd( long long a,  long long b)
{
	 if(!a)
	 	return b;
	return gcd(b % a, a);
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int c, T, i, j, k, cas;
	for(scanf("%d", &T), cas = 1; cas <= T; cas++)
	{
		int n;
		scanf("%d", &n);
		for(i = 0; i < n; i++)
		{
			cin>>t[i];
		}
		sort(t, t + n);
		 long long m = 0;
		for(i = 0; i < n; i++)
			for(j = i + 1; j < n; j++)
			{
				m = gcd(t[j] - t[i], m);
			}
		 long long ans = (m - ((t[0]) % m)) % m;
		if(ans < 0)
			ans += m;
		printf("Case #%d: ", cas);
		cout<<ans<<endl;
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}
