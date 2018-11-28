#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
int O[200],B[200],otop,btop,ot,bt,o,b;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int t,n,i,d,ans,tt,z=0;
	char c,s[200];
	scanf("%d",&t);
	while(t--)
	{
		z++;
		otop=btop=ot=bt=ans=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf(" %c %d",&s[i],&d);
			if(s[i]=='O')
				O[++otop]=d;
			else
				B[++btop]=d;
		}/*
		printf("O:");
		for(i=0;i<otop;i++)
			printf(" %d",O[i]);
		printf("\nB:");
		for(i=0;i<btop;i++)
			printf(" %d",B[i]);
		printf("\n");*/
		O[0]=B[0]=o=b=1;
		for(i=1;i<=n;i++)
		{
			if(s[i]=='O')
			{
				tt=abs(O[ot+1]-o)+1;
				o=O[ot+1];
				ot++;
				ans+=tt;
				if(b<=B[bt+1])
					b=min(B[bt+1],b+tt);
				else
					b=max(B[bt+1],b-tt);
			}
			else
			{
				tt=abs(B[bt+1]-b)+1;
				b=B[bt+1];
				bt++;
				ans+=tt;
				if(o<=O[ot+1])
					o=min(O[ot+1],o+tt);
				else
					o=max(O[ot+1],o-tt);
			}
			//printf("%d: %d   o=%d b=%d\n",i,ans,o,b);
		}
		printf("Case #%d: %d\n",z,ans);
	}
}
