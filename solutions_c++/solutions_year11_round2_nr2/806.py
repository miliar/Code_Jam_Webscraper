#include<stdio.h>
#include<stdlib.h>
#define eps 1e-9
#include<math.h>
double pp[1000010],p[1000010];
int v[210];
double max(double x,double y)
{
	return x>y?x:y;
}
FILE *f;


int main()
{
	int ca,i,j,k,test=0,ok,d,c,cnt;
	double mid,l,r,x;
	f=fopen("B.out","w");
	scanf("%d",&ca);
	while(ca--)
	{
		scanf("%d%d",&c,&d);
		cnt=0;
		for(i=1;i<=c;i++)
		{
		  scanf("%lf%d",&pp[++cnt],&v[i]);
		  for(j=1;j<v[i];j++)
		  {
			cnt++;
		    pp[cnt]=pp[cnt-1];
		  }
		}

		//for(i=1;i<=cnt;i++) printf("%lf ",pp[i]);
		l=0.0;r=100000000000.0;
		while(r-l>eps)
		{
			mid=(l+r)/2;
			for(i=1;i<=cnt;i++) p[i]=pp[i];
			ok=1;
			p[1]-=mid;
            
			//printf("mid=%lf\n",mid);
			for(i=2;i<=cnt;i++)
			{
			  x=max(p[i-1]+d,p[i]-mid);
			  //printf("x=%lf",x);system("pause");
			  if(fabs (x-p[i]) >mid+eps) 
			  {
				 ok=0;
				 break;
			  }
			  p[i]=x;
			}
			//for(i=1;i<=cnt;i++) printf("%lf  ",p[i]);system("pause");

			if(ok) r=mid-eps;
			else l=mid+eps;
		}
		fprintf(f,"Case #%d: %.7lf\n",++test,mid);
	}
	system("pause");
	return 0;
}

		
			  
