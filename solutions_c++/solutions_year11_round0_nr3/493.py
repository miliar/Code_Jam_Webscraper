#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int m,n,tt,c,d,r;
int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{	
		cin >> n;
		int ans=0;
		int mi=99999999;
		int sum=0;
		for (int i=1;i<=n;++i)
		{
			scanf("%d",&m);
			ans^=m;
			sum+=m;
			mi=min(mi,m);
		}
		if (ans!=0)
		{
			printf("Case #%d: NO\n",kk);
		}
		else
		{
			printf("Case #%d: %d\n",kk,sum-mi);
		}		
	}	
	return 0;	
}