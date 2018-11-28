#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
#include<string.h>
#include<map>
#include<math.h>
#include<string>
#include<queue>
#include<csetjmp>
#include<cstring>
#include<vector>
#define M 1000000007
int mam[5][110],mark[1100],a[1010];
int main()
{
	int i,n,m,cs=0,k,T,ans,s,j,c,t1,t2,f;
	freopen("A.txt","w",stdout);
	//while(scanf("%d%d",&n,&m))
	//{
	//	printf("%d %d\n",n^m,n|m);
	//}
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n);
		for(ans=a[1],s=a[1],i=2;i<n;i++)
		{
			ans=ans^a[i];
			s+=a[i];
		}
		if(ans!=a[0])
			printf("Case #%d: NO\n",++cs);
		else printf("Case #%d: %d\n",++cs,s);
	}
	return 0;
}