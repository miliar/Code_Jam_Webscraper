#include<stdio.h>
#include<stdlib.h>
int main()
{
	int t,ca=1;
	int n;
	int num;
	char c[10];
	int orange[110],blue[110],order[110];
	int poso,posb;
	int i,j,k;
	int dpo[110],dpb[110];
	scanf("%d",&t);
	while(ca<=t)
	{
		poso=0;
		posb=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%d",c,&num);
			if(c[0]=='O')
			{
				orange[poso++]=num;
				order[i]=0;
			}
			else
			{
				blue[posb++]=num;
				order[i]=1;
			}
		}
		dpo[0]=orange[0]-1;
		dpb[0]=blue[0]-1;
		if(poso==0)
		dpo[0]=0;
		if(posb==0)
		dpb[0]=0;
		for(i=1;i<poso;i++)
		{
			dpo[i]=orange[i]-orange[i-1]>0?orange[i]-orange[i-1]:orange[i-1]-orange[i];
			dpo[i]+=dpo[i-1];
		}
		for(i=1;i<posb;i++)
		{
			dpb[i]=blue[i]-blue[i-1]>0?blue[i]-blue[i-1]:blue[i-1]-blue[i];
			dpb[i]+=dpb[i-1];
		}
		int waito,waitb;
		waito=0;waitb=0;
		int o=0,b=0;
		for(i=0;i<n;i++)
		{
			if(order[i]==0)
			{
				if(b<posb)
				{
					if(dpo[o]+waito>=dpb[b]+waitb)
					{
						int temp=dpo[o]+waito-dpb[b]-waitb;
						waitb+=temp+1;
						waito+=1;
					}
					else
					{
						waito+=1;
					}
				}
				else
				{
					waito+=1;
					waitb+=1;
				}
				o++;
			}
			else
			{
				if(o<poso)
				{
					if(dpo[o]+waito<=dpb[b]+waitb)
					{
						int temp=dpb[b]+waitb-dpo[o]-waito;
						waito+=temp+1;
						waitb+=1;
					}
					else
					{
						waitb+=1;
					}
				}
				else
				{
					waitb+=1;
					waito+=1;
				}
				b++;
			}
//			printf("o:%d b:%d waito:%d waitb:%d\n",o,b,waito,waitb);
		}
		int ans;
		if(poso==0)
		{
			ans=dpb[posb-1]+waitb;
		}
		else if(posb==0)
		{
			ans=dpo[poso-1]+waito;
		}
		else
		{
			ans=dpo[poso-1]+waito>dpb[posb-1]+waitb?dpo[poso-1]+waito:dpb[posb-1]+waitb;
		}
		printf("Case #%d: %d\n",ca,ans);
		ca++;
	}
}
