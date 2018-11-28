#include <stdio.h>
#include<math.h>

int main()
{
	int T=0,n=0,s=0,p=0,x=0,i=0,j=0,k=0,l=0,m=0,f=0,G=0,g=0,p1=0;
	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("\n%d %d %d",&n,&s,&p);
		if((p-2)<=0)
			p1=0;
		else
			p1=p-2;
		G=0;
		for(j=1;j<=n;j++)
		{
			scanf("%d",&x);
			f=0;
			if(x<p)
				continue;
			if((x==p && x==0) || p==0)
			{
				G=G+1;
				continue;
			}
			k=p;
			for(k=p;(k<=((x/2)+1) && k<=10);k++)
			{
				if(f==1)
				   break;
				for(g=1;g<=2;g++)
			    {
				if(f==1)
					break;
				//printf("K: %d ",k);
				l=p1;
				for(l=p1;((l<=10) && (l<=(k+2)));l++)
				{
				 	if(f==1)
						break;
					if(abs(k-l)>2)
						continue;
					//printf("L: %d ",l);
					m=p1;
					for(m=p1;((m<=10) && (m<=(k+2)));m++)
					{
						if((abs(m-k)>2) || (abs(l-m)>2))
							continue;
						//printf("M: %d k+l+m %d ",m,k+l+m);
						if((k+l+m)==x)
						{
							if((abs(m-k)!=2) && (abs(l-m)!=2) && (abs(k-l)!=2) && g==1)
							{
								G=G+1;
								//printf("\nCase #X: %d %d %d \n",k,l,m);
								f=1;
								break;
							}
							if(((abs(m-k)==2) || (abs(l-m)==2) || (abs(k-l)==2)) && s!=0 && g==2)
							{
								G=G+1;
								//printf("\nCase #X: %d %d %d \n",k,l,m);
								s=s-1;
							    f=1;
								break;
							}
							
						}
					}
				}
				}
		    }
		}
	    printf("Case #%d: %d\n",i,G);
	}
}