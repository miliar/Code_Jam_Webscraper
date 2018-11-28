#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,cas=0,n,a,res,mn,i,sm;
	freopen("C-large.in","r",stdin);
	freopen("C-small.out","w",stdout);
	scanf("%d",&t);
	while(cas<t)
	{
		cas++;
		mn=10000000;
		sm=0;
		res=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a);
			sm+=a;
			if(a<mn) mn=a;
			res^=a;
		}
		if(!res) printf("Case #%d: %d\n",cas,sm-mn);
		else printf("Case #%d: NO\n",cas);
	}
	return 0;
}
