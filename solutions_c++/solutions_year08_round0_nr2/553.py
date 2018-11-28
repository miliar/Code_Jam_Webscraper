#include<stdio.h>
#include<algorithm>
#include<functional>
#include<iostream>
using namespace std;

struct time
{
	int arri_m;
	int dep_m;
	char sot;
} table[210],tarri;

bool cmp(const time &a,const time &b)
{
	if(a.dep_m==b.dep_m)
	{
		 return a.arri_m<b.arri_m;
	}
	else return a.dep_m<b.dep_m;

}
int main()
{
	int limitt;
	int na,nb;
	int n;
	int i,j;
	int avif[210];
	int ah,am,dh,dm;
	int num[2];
	int cases=0;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	while(1==scanf("%d",&n))
	{
		while(n--)
		{
			scanf("%d",&limitt);
			scanf("%d %d",&na,&nb);
			for(i=0;i<na;i++)
			{
				scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
				table[i].dep_m=dh*60+dm;
				table[i].arri_m=ah*60+am;
				table[i].sot='A';
			}
			for(i=0;i<nb;i++)
			{
				scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
				table[i+na].dep_m=dh*60+dm;
				table[i+na].arri_m=ah*60+am;
				table[i+na].sot='B';
			}


			sort(&table[0],&table[na+nb],cmp);

			memset(avif,0,sizeof(avif));
			num[0]=num[1]=0;
			for(i=0;i<na+nb;i++)
			{
				if(avif[i]==0)
				{
					tarri.arri_m=table[i].arri_m;
					tarri.sot=table[i].sot;
					avif[i]=-1;
					for(j=i+1;j<na+nb;j++)
					{
						if(avif[j]==0&&tarri.arri_m+limitt<=table[j].dep_m&&tarri.sot!=table[j].sot)
						{
							tarri.arri_m=table[j].arri_m;
							tarri.sot=table[j].sot;
							avif[j]=-1;
						}

					}
					num[table[i].sot-'A']++;
				}
				
			}
			printf("Case #%d: %d %d\n",++cases,num[0],num[1]);
		}
	}
	return 0;
}