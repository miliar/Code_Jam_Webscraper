// Theme Park.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
struct Node
{
	__int64 next,value;
}nodes[1005];
__int64 person[1005];
int main()
{
	freopen("e:\\C-large.in","r",stdin);
	freopen("e:\\2.out","w",stdout);
	__int64 T,R,k,n;
	__int64 sum,ans;
	scanf("%I64d",&T);
	for(int t=1;t<=T;t++)
	{
		sum=ans=0;
		scanf("%I64d%I64d%I64d",&R,&k,&n);
		for(int i=0;i<n;i++)
		{
			scanf("%I64d",&person[i]);
			sum+=person[i];
			if(sum<=k)
			{
				nodes[0].next=i+1;
				nodes[0].value=sum;
			}
		}
		if(sum<=k) ans=sum*R;
		else
		{
			for(int i=1;i<n;i++)
			{
				__int64 temp=nodes[i-1].value-person[i-1];
				__int64 nextnode=nodes[i-1].next;
				while(temp+person[nextnode]<=k)
				{
					temp+=person[nextnode];
					nextnode=(nextnode+1)%n;
				}
				nodes[i].next=nextnode;
				nodes[i].value=temp;
			}
			__int64 start=0;
			for(int i=0;i<R;i++)
			{
				ans+=nodes[start].value;
				start=nodes[start].next;
			}
		}
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}

