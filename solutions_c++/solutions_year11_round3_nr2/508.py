#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

const int maxint = ~0U>>2;

bool ss[100001];
int a[100001];
int T,n,p,l,t,c,ans;

void calc()
{
	int i,j,k,tmp=0;
	for(i=1;i<=n;i++)
	{
		j=i%c;
		if(j==0) j=c;
		if(ss[i]==false)
		{
			tmp+=a[j]*2;
			continue;
		}	
		if(t<=tmp)
		{
			tmp+=a[j];
			continue;
		}
		else
		{
			if(tmp+a[j]*2<=t)
			{
				tmp+=a[j]*2;
				continue;
			}
			else
			{
				k=t-tmp;
				tmp+=k+a[j]-k/2;
				if(k&1) tmp++;
			}
    	}
	}
	if(ans>tmp) ans=tmp;
}

void dfs(int x,int y)
{
	if(y==0)
	{
		calc();
		return ;
	}
	for(int i=x;i<=n;i++)
	{
		ss[i]=true;
		dfs(i+1,y-1);
		ss[i]=false;
	}
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int i,j,k;
	scanf("%d",&T);
	for(p=1;p<=T;p++)
	{
		scanf("%d%d%d%d",&l,&t,&n,&c);
		for(i=1;i<=c;i++)
		scanf("%d",&a[i]);	
		ans=maxint;
		dfs(1,l);
		printf("Case #%d: %d\n",p,ans);
	}
	return 0;
}
