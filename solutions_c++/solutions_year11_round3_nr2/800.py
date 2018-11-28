#include<cmath>
#include<cstdio>
#include<cstring>
#include<map>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
using namespace std;

int mm[1000005];
int len[1000005];
int ll[1000005];
int Min(int a,int b)
{
	return a<b?a:b;
}
int cmp(int a,int b)
{
	return a>b;
}
int main ()
{
	//freopen("in.txt","r",stdin);
	//freopen("a.out","w",stdout);
	int T,temp,left,xxx=0;
	int tans;
	int ans,i,j,k,l,t,n,c,cnt,sum;
	scanf("%d",&T);
	while(T--)
	{
		xxx++;
		printf("Case #%d: ",xxx);
		scanf("%d%d%d%d",&l,&t,&n,&c);
		for(i=0;i<c;i++)
		{
			scanf("%d",&mm[i]);
		}
		cnt=0;
		for(i=0;i<n;i++)
		{
			len[i]=mm[cnt++];
			if(cnt==c)cnt=0;
		}
		tans=0;
		for(i=0;i<n;i++)
		{
			tans+=len[i]*2;
			if(tans>=t)break;
		}
		int sp=0;
		if(tans>t)
		{
			tans-=len[i]*2;
			temp=t-tans;
			tans=t;
			ll[sp]=len[i]-(temp)*0.5;
			sp++;
		}
		i++;
		for(;i<n;i++)ll[sp++]=len[i];
		sort(ll,ll+sp,cmp);
		for(i=0;i<l&&i<sp;i++)
		{
			tans+=ll[i];
		}
		for(;i<sp;i++)tans+=ll[i]*2;
		printf("%d\n",tans);
	}
}
