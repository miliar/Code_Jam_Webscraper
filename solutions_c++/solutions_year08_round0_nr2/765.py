#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
const int maxn=1600;

int na,nb,tr,t;
int astart[maxn],bstart[maxn],aend[maxn],bend[maxn];

int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		scanf("%d",&tr);
		scanf("%d%d",&na,&nb);
		memset(astart,0,sizeof(astart));
		memset(bstart,0,sizeof(bstart));
		memset(aend,0,sizeof(aend));
		memset(bend,0,sizeof(bend));
		for(int i=0;i<na;i++)
		{
			int m,s;
			scanf("%d:%d",&m,&s);
			astart[m*60+s]++;
			scanf("%d:%d",&m,&s);
			aend[m*60+s+tr]++;
		}
        for(int i=0;i<nb;i++)
		{
			int m,s;
			scanf("%d:%d",&m,&s);
			bstart[m*60+s]++;
			scanf("%d:%d",&m,&s);
			bend[m*60+s+tr]++;
		}
		int alft=0,blft=0,ansa=0,ansb=0;
		for(int i=0;i<maxn;i++)
		{
			if(aend[i])blft+=aend[i];
			if(bend[i])alft+=bend[i];
			if(astart[i])
			{
				if(alft>=astart[i])alft-=astart[i];
				else
				{
					ansa+=astart[i]-alft;
					alft=0;
				}
			}
			if(bstart[i])
			{
				if(blft>=bstart[i])blft-=bstart[i];
				else
				{
					ansb+=bstart[i]-blft;
					blft=0;
				}
			}
		}
		printf("Case #%d: %d %d\n",cs,ansa,ansb);
	}
	return 0;
}
