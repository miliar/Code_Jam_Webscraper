#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>


int cases;
long long res;


void sorthl(long long *a, int sz)
{
	long long temp;
	for( int i=0;i<sz-1;i++)
	{
		for(int j=i+1; j<sz;j++)
		{
			if(a[i]<a[j])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
}

void sortlh(long long *a, int sz)
{
	long long temp;
	for( int i=0;i<sz-1;i++)
	{
		for(int j=i+1; j<sz;j++)
		{
			if(a[i]>a[j])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
}

int main(int argc, char **argv)
{
int num, xn_n, xp_n, yn_n, yp_n;
long long xn[810];
long long yn[810];
long long xp[810];
long long yp[810];
long long a;

    freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);


	scanf("%d",&cases);
	for(int N=1; N<=cases; N++)
	{
		res=0;
		xp_n=0;
		xn_n=0;
		yp_n=0;
		yn_n=0;
		scanf("%d",&num );
		for(int i=0;i<num;i++)
		{
				scanf("%lld",&a);
				if(a<0)
					xn[xn_n++]=a;
				else
					xp[xp_n++]=a;
					
		}

		for(int i=0;i<num;i++)
		{
				scanf("%lld",&a);
				if(a<0)
					yn[yn_n++]=a;
				else
					yp[yp_n++]=a;
		}

		sortlh(xn,xn_n);
		sorthl(yn,yn_n);

		sortlh(xp,xp_n);
		sorthl(yp,yp_n);

		//sorthl(x,num);
		//sortlh(y,num);

		for(int i=0;i<xp_n;i++)
			xn[xn_n+i]=xp[i];

		for(int i=0;i<yn_n;i++)
			yp[yp_n+i]=yn[i];


		for(int i=0;i<num;i++)
		{   res+=xn[i]*yp[i];
		}

		printf("Case #%d: %lld\n",N,res);

	}

	return 0;

}


