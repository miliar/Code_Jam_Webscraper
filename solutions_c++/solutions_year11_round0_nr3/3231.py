#include<iostream>
#include<algorithm>
using namespace std;
int tt, ii;
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d\n", &tt);
	int n, i, j, sm = 0, mn = 10000000, c, sm1;
	for(ii = 1; ii<=tt; ii++)
	{
		scanf("%d", &n);
		sm = 0; mn = 10000000; sm1 = 0;
		for(i = 1; i<=n; i++)
		{
			scanf("%d", &c);
			if(c<mn)
				mn = c;
			sm1 ^=c;
			sm+=c;
		}

		if(sm1!=0)
			printf("Case #%d: NO\n", ii);
		else
			printf("Case #%d: %d\n", ii, sm-mn);
	}
	return 0;
}