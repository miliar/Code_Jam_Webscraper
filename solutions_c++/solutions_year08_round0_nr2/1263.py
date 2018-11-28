#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
	int i,j,k,l,n,t,na,nb,a1,a2,aa[100],ad[100],ba[100],bd[100],mi,ch,in;
	char temp[1000];
	bool fa[100],fb[100];
	scanf("%d",&n);
	for(l=0;l<n;l++)
	{
		scanf("%d",&t);
		scanf("%d %d",&na,&nb);
		for(i=0;i<(na*2);i++)
		{
			scanf(" %s",temp);
			if(i%2==0)
				aa[i/2]=((temp[0]-48)*10+(temp[1]-48))*60+(temp[3]-48)*10+(temp[4]-48);
			else
				ad[i/2]=((temp[0]-48)*10+(temp[1]-48))*60+(temp[3]-48)*10+(temp[4]-48);

		}
		for(i=0;i<(nb*2);i++)
		{
			scanf(" %s",temp);
			if(i%2==0)
				ba[i/2]=((temp[0]-48)*10+(temp[1]-48))*60+(temp[3]-48)*10+(temp[4]-48);
			else
				bd[i/2]=((temp[0]-48)*10+(temp[1]-48))*60+(temp[3]-48)*10+(temp[4]-48);

		}
		if(na==0)
			a1=0,a2=nb;
		else if(nb==0)
			a1=na,a2=0;
		else
		{
			a1=na,a2=nb;
			for(i=0;i<na;i++)
				fa[i]=true;
			for(i=0;i<nb;i++)
				fb[i]=true;
			for(i=0;i<na;i++)
			{
				ch=ad[i]+t;
				mi=9999;
				for(j=0;j<nb;j++)
				{
					if(fb[j]==false)
						continue;
					if(ch<=ba[j] && mi>ba[j])
					{
						mi=ba[j];
						in=j;
					}
				}
				if(mi!=9999)
				{
					a2--;
					fb[in]=false;
				}
			}
			for(i=0;i<nb;i++)
			{
				ch=bd[i]+t;
				mi=9999;
				for(j=0;j<na;j++)
				{
					if(fa[j]==false)
						continue;
					if(ch<=aa[j] && mi>aa[j])
					{
						mi=aa[j];
						in=j;
					}
				}
				if(mi!=9999)
				{
					a1--;
					fa[in]=false;
				}
			}
		}
		printf("Case #%d: %d %d\n",(l+1),a1,a2);
	}
	return 0;
}
