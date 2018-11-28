//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int n, T, t, i, m, s, x, total;
	scanf("%d", &T);
	for (t=1;t<=T;++t)
	{
		s = 0;
		total = 0;
		m=10000000;
		scanf("%d", &n);
		for(i=0;i<n;++i)
		{
			scanf("%d", &x);
			if (x<m) m=x;
			s = x ^ s;
			total += x;
		}
		if (s==0)
		{
			printf("Case #%d: %d\n", t, total-m);
		} else
			printf("Case #%d: NO\n", t);
	}

	return 0;
}