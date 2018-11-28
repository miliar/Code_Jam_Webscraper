#include<iostream>
#include<stdio.h>
#include<memory.h>
#include<map>
#include<vector>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,ca=0;
	scanf("%d",&t);
	while(t--)
	{
		map<int,int>qu;
		__int64 ans=0;
		char a[100];
		scanf("%s",a);
		printf("Case #%d: ",++ca);
		int q[300];
		memset(q,-1,sizeof(q));
		q[a[0]]=1;
		int x=0;
		for(i=0;a[i];i++)
		{
			if(q[a[i]]==-1)
			{
				q[a[i]]=x;
				x++;
				if(x==1)
					x++;
			}
		}
		if(x==0)
			x=2;
		for(i=0;a[i];i++)
		{
			ans=ans*x+q[a[i]];
		}
		printf("%I64d\n",ans);
	}
	return 0;
}
