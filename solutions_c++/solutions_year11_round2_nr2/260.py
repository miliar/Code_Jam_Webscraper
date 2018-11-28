#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
using namespace std;
int n,T,Ti,m;

double eps=1e-3;

struct cla
{
	int a,b;
}rC[1000];

int D;
long long r[1001000],d[1001000];

bool cmp(const cla& a,const cla& b)
{
	return a.a<b.a;
}

bool xx(long long x)
{
	d[0]=r[0]-x;
	int i;
	for(i=1;i<n;i++)
	{
		if(r[i]>=d[i-1]+D)
		{
			d[i]=max(d[i-1]+D,r[i]-x);
			
		}		
		else
		{
			if(r[i]+x<d[i-1]+D)return 0;
			else d[i]=d[i-1]+D;
		}
	}
	return 1;
}

int main()
{
    freopen("z.in","r",stdin);
    freopen("z.out","w",stdout);
    int i,d,j,k,C;
    double z,da;
    long long a,b,c;
	
    scanf("%d",&T);    for(Ti=1;Ti<=T;Ti++)
//    while(scanf("%s%s",a,b)!=EOF)
    {	
		printf("Case #%d: ",Ti);
		
		scanf("%d%d",&C,&D);
		D*=2;
		for(i=0;i<C;i++)scanf("%d%d",&rC[i].a,&rC[i].b),rC[i].a*=2;
		
		sort(rC,rC+C,cmp);		
		
		
		
		n=0;
		for(i=0;i<C;i++)
		for(j=0;j<rC[i].b;j++)r[n++]=rC[i].a;
		
		
		a=-1;c=100000000000000ll;
		while(a+1<c)
		{
			b=(a+c)/2;
			if(xx(b))c=b;
			else a=b;
		//	cout<<a<<' '<<c<<endl;
		}
		
		printf("%.1lf\n",c/2.0);
		
		/*
		da=0;
		for(i=1;i<n;i++)
		{
			z=0;
			if(r[i]-r[0]>=D*i)continue;
			z=(D*i-(r[i]-r[0]))/2.0;
			if(da<z)da=z;
		}		
		
		printf("%.1lf\n",da);*/
	}	
    return 0;
}
