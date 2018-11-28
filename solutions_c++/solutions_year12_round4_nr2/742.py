#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;
#define maxn 1010
double x[maxn],y[maxn];
double r[maxn];
int N,w,l;
void findans()
{
	int ti,i,p,j;
	bool flag=true,f1;
	ti=1000000;
	double leng;
	x[0]=0.0;
	y[0]=0.0;
	x[N-1]=w;
	y[N-1]=l;
	while(flag)
	{
		//cout<<"yes"<<endl;
		for(i=1;i<N-1;i++)
		{
			x[i]=(rand()%100001*100000+rand()%100000)/10.0;
			y[i]=(rand()%100001*100000+rand()%100000)/10.0;
			if(x[i]<0)
				x[i]=-x[i];
			if(y[i]<0)
				y[i]=-y[i];
			p=(int)x[i]/w;
			x[i]=x[i]-w*p;
			p=(int)y[i]/l;
			y[i]=y[i]-l*p;
		}
		//cout<<"yes"<<endl;
		//system("pause");
		
		f1=true;
		for(i=0;i<N&&f1;i++)
			for(j=i+1;j<N&&f1;j++)
			{
				leng=(x[j]-x[i])*(x[j]-x[i])+(y[j]-y[i])*(y[j]-y[i]);
				leng=sqrt(leng);
				//cout<<leng<<endl;
				//cout<<r[j]<<endl;
				//cout<<r[i]<<endl;
				if(leng<(double)(r[j]+r[i]))
					f1=false;
				//cout<<f1<<endl;
			}
		if(f1)
			flag=false;		
	}
	printf("%.1lf %.1lf",x[0],y[0]);
	for(i=1;i<N;i++)
		printf(" %.1lf %.1lf",x[i],y[i]);
	printf("\n");
}
int main()
{
	int i,tcase,casenum=0;
	freopen("BB.in","r",stdin);
	freopen("BB.out","w",stdout);
	scanf("%d",&tcase);
	while(tcase--)
	{
		printf("Case #%d: ",++casenum);
		scanf("%d %d %d",&N,&w,&l);
		for(i=0;i<N;i++)
			scanf("%lf",&r[i]);
		findans();
	}
	return 0;
}
