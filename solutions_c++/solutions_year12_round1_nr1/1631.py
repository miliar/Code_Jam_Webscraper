#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;
int n,m;
double p[100005],r[100005];
FILE *fp;
int main()
{
	fp=fopen("answer.out","w");
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d",&m,&n);
		r[0]=1;
		for(int i=1;i<=m;i++)
		{
			scanf("%lf",&p[i]);
			r[i]=p[i]*r[i-1];
		}
		double ans1,ans2,ans3,ans;
		ans1=ans2=ans3=0;
		ans1=(n-m+1)*r[m]+(1.0-r[m])*(2*n-m+2);
		ans2=10000000;
		for(int i=1;i<=m;i++)
		{
			ans2=min(ans2,r[m-i]*(n+2*i+1.0-m)+(2.0*n-m+2.0*i+2.0)*(1.0-r[m-i]));
		}
		ans3=2+n;
		ans=min(ans1,min(ans2,ans3));
		printf("Case #%d: %.6f\n",t,ans);
		fprintf(fp,"Case #%d: %.6f\n",t,ans);
	}
	return 0;
}

