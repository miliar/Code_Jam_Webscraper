#include<iostream>
using namespace std;
__int64 zz[1002],up;
__int64 total=0;
__int64 use[1002],vv[1002];
int ins[1002];
int round,n;
int main()
{
	int cas;
	
	int cc,i,j,k,y;
	cc=0;
	__int64 tem;
	freopen("C://C-small-attempt0.in","r",stdin);
	freopen("C://out.txt","w",stdout);
scanf("%d",&cas);
	while(cas--)
	{
		cc++;
		scanf("%d %I64d %d",&round,&up,&n);
		total=0;
		for(i=0;i<n;i++)
		{
			scanf("%I64d",zz+i);
			total+=zz[i];
			ins[i]=-1;
		}
		__int64 mak=0,tp;
		i=0;
		while(1)
		{
			if(up>=total)
			{
				
			
				vv[i]=total;
                ins[i]=i;
				j=i;
				mak=total;
			break;
               
			}
			else
			{
				tem=up;
				j=i;
				mak=0;
			while(tem)
				{
					if(zz[j]>tem)
						break;
					k=j;
					 	tem-=zz[j];
					mak+=zz[j];
					j=(j+1)%n;
				
				
				}
			      vv[i]=mak;
				  ins[i]=j;
				  if(ins[j]!=-1)
					  break;

			}
			i=j;

		}
		tp=1;
	    if(ins[i]!=i)
		{
		  k=ins[j];
		  mak=vv[j];
		  tp=1;
		  while(k!=j)
		  {
			  mak+=vv[k];
			  tp++;
			  k=ins[k];
		  }
		
		}
		int ind=0;
		__int64 w,e,r,ans=0;
		while(round)
		{
			if(ind==j)
			{
				w=round/tp;
				round-=w*tp;
				ans+=w*mak;
				if(round==0)
					break;
				j=1000000;
				
			}
			else
			{
				round--;
				ans+=vv[ind];
				ind=ins[ind];
			}
		}
		printf("Case #%d: %I64d\n",cc,ans);
	}
	return 0;
}




		  

	


		
		





