#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
#define M 4
double p[M];
double w[M];
double t[M];
int a,b;
int main()
{
	int C;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&C);
	for(int c=1;c<=C;c++)
	{
		scanf("%d%d",&a,&b);
		scanf("%lf",&p[1]);
		w[1]=1-p[1];
		t[1]=p[1];
		//cout<<p[1]<<endl;
		for(int i=2;i<=a;i++)
		{
			scanf("%lf",p+i);
			//cout<<p[i]<<' ';
			w[i]=w[i-1]+t[i-1]*(1-p[i]);
			t[i]=t[i-1]*p[i];
		}
		double tp=0,ans=100000000;
		
		for(int j=0;j<a;j++)
		{
			//cout<<t[a-j]<<' '<<w[a-j]<<endl;
			tp=(b+1-a+2*j)*t[a-j]+(b+1-a+b+1+2*j)*w[a-j];
			if(tp<ans)ans=tp;
			//cout<<tp<<' '<<endl;;
		}
		tp=1+b+1;
		if(ans>tp)ans=tp;
		printf("Case #%d: %.6lf\n",c,ans);
	}
	return 0;	
			
}
			
			
			
			
			
			
			
			
			
			
			
			
			