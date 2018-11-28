#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<map>
#include<algorithm>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large-output.txt","w",stdout);
	int T,n,i,j,k,p,ans,bxianzou,oxianzou,bstart,ostart;
	char r;
	int count=0;
	scanf("%d",&T);
	getchar();
	while(T--)
	{
		count++;
		j=0;k=0;ostart=1;bstart=1;ans=0;bxianzou=0;oxianzou=0;
		scanf("%d",&n);
		getchar();
		for(i=0;i<n;i++)
		{
			scanf("%c%d",&r,&p);
			getchar();
			if(r=='O')
			{
				//orange[++j]=p;
				if(abs(p-ostart)+1-bxianzou>0)
				{
					if(bxianzou!=0)
					{oxianzou+=abs(p-ostart)+1-bxianzou;ans+=abs(p-ostart)+1-bxianzou;}
					else {oxianzou+=abs(p-ostart)+1-bxianzou;ans+=abs(p-ostart)+1-bxianzou;}
				}
				else {oxianzou=1;ans+=1;}
				ostart=p;
				bxianzou=0;
			}
			if(r=='B')
			{
				//blue[++k]=p;
				if(abs(p-bstart)+1-oxianzou>0)
				{
					if(oxianzou!=0)
					{bxianzou+=abs(p-bstart)+1-oxianzou;ans+=abs(p-bstart)+1-oxianzou;}
					else {bxianzou+=abs(p-bstart)+1-oxianzou;ans+=abs(p-bstart)+1-oxianzou;}
				}
				else {bxianzou=1;ans+=1;}
				bstart=p;
				oxianzou=0;
			}
		}
		printf("Case #%d: %d\n",count,ans);
	}
	return 0;
}