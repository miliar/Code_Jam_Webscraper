// Theme Park.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
using namespace std;

long long   a[1001];//每组人的size

long long  num[1001];//第i组人作为队列开头时的收入
long long  rank[1010];
long long mark[1001];



int main()
{
	freopen("debug\\in.txt","r",stdin);
	freopen("debug\\out.txt","w",stdout);
	long long  repeat;
	cin>>repeat;
	long long i,j,k,r,m,n,top,start;
	int cases=1;
	while(repeat--)
	{
		memset(mark,0,sizeof(mark));
		cin>>r>>n>>m;//运行r次，容量为n，m组人
		for(i=1;i<=m;i++)
			scanf("%d",&a[i]);
		rank[1]=1;
		mark[1]=true;
		i=1;
		top=1;
		while(1)
		{
			num[i]=0;
			for(j=i;j<i+m;j++)
			{
				k=j;
				if(k>m)
					k-=m;
				if(num[i]+a[k]<=n)
					num[i]+=a[k];
				else break;
			}
			if(!mark[k])
			{
				mark[k]=true;
				rank[top+1]=k;
				top++;
				i=k;
			}
			else 
			{
				rank[top+1]=k;
				top++;
				break;
			}
			
			
			
		}
		
		for(i=1;i<=top;i++)
			if(rank[i]==rank[top])
				break;
		start=i;
		
		
		long long ans=0;
		long long tmp;
		if(r<start)
		{
			for(i=1;i<=r;i++)
				ans+=num[rank[i]];
		}
		else
		{
			for(i=1;i<start;i++)
				ans+=num[rank[i]];
			r=r-start+1;
			tmp=0;
			for(i=start;i<top;i++)
				tmp+=num[rank[i]];
			ans=ans+r/(top-start)*tmp;
			r=r%(top-start);
			for(i=start;i<start+r;i++)
				ans+=num[rank[i]];
		}
		printf("Case #%d: ",cases++);cout<<ans<<endl;

	}



	return 0;
}

