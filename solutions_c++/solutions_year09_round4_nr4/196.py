#include<iostream>
#include<cmath>
using namespace std;
double x[41],y[41],r[41];
int i,n,t,casenum;
double ans;
double dist(int a,int b)
{
	return sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]));
}

int main()
{
	freopen("problem.in","r",stdin);
    freopen("problem.out","w",stdout);
	cin>>casenum;
	for (t=1;t<=casenum;t++)
	{
		cout<<"Case #"<<t<<": ";
		cin>>n;
		for (i=1;i<=n;i++)
			cin>>x[i]>>y[i]>>r[i];
		if (n==1) ans=r[1];
		if (n==2) ans=max(r[1],r[2]);
		if (n==3)
		{
			ans=1e100;
			ans=min(ans,max(r[1],(dist(2,3)+r[2]+r[3])/2));
			ans=min(ans,max(r[2],(dist(1,3)+r[1]+r[3])/2));
			ans=min(ans,max(r[3],(dist(1,2)+r[1]+r[2])/2));
		}
		printf("%.6f\n",ans);
	}
}
