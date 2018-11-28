#include <iostream>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int main()
{
	int nCase,n,s,p,a[101];
	int i,j,ans,temp,tmp;
	freopen("B-large.in","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d",&nCase);
	for(i=1;i<=nCase;i++)
	{
		memset(a,0,sizeof(a));
		scanf("%d%d%d",&n,&s,&p);
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[j]);
		}
		temp=3*p-4;
		if(temp<=0)
		temp=temp+1;
		if(temp<=0)
		temp=temp+2;
		tmp=3*p-2;
		if(p==1)
		{
			temp=1;
			tmp=1;
		}
		if(p==0)
		{
			printf("Case #%d: %d\n",i,n);
			continue;
		}
		ans=0;
		for(j=0;j<n;j++)
		{
			if(a[j]>=tmp)
				ans++;
			else if(a[j]>=temp&&s>0)
			{
				ans++;
				s--;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
