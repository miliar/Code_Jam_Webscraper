#include <stdio.h>
#include <stdlib.h>
int comp(const void *a ,const void *b)
{
	return ((int *)a)[2]-((int *)b)[2];
}
int main()
{
	int i,T,X,S,R,N,a[1001][3],ps=1;
	double t;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		double sum=0,count=0;
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
		for(i=0;i<N;i++)
		{
			scanf("%d%d%d",&a[i][0],&a[i][1],&a[i][2]);
			count+=a[i][1]-a[i][0];
		}
		qsort(a,N,sizeof(a[0]),comp);
		count=X-count;
		if( R*t<=count)
		{
			sum+=t;
			sum+= (count-R*t)*1.0/S;
			t=0;
		}
		else
		{
			sum+=count*1.0/R;
			t-=count*1.0/R;
		}
		for(i=0;i<N;i++)
		{
			double ss=a[i][1]-a[i][0];
			if(t==0)
			{
				sum+=ss/(a[i][2]+S);
			}
			else
			{
				if( (R+a[i][2])*t <ss )
				{
					sum+=t;
					sum+=(ss- (R+a[i][2])*t)/(S+a[i][2]);
					t=0;
				}
				else
				{
					sum+=ss/(R+a[i][2]);
					t-=ss/(R+a[i][2]);
				}
			}
		}
		printf("Case #%d: %.6f\n",ps++,sum);
	}
}