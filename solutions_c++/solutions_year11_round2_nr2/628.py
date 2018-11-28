#include<cstdio>
#include<algorithm>
using namespace std;

const double eps=1e-7;
const int mx=1000010;

int n;
int d,c;
int pos[mx];
int p[mx],v[mx];

bool can(double t)
{
	int i;
	double last=pos[0]-t;
	for(i=1;i<n;i++)
	{
		if(last+d>pos[i]+t)
			return false;
		double next=pos[i]-t>last+d?pos[i]-t:last+d;
		last=next;
	}
	return true;
}

int main()
{
	int i;
	int t,ca=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&c,&d);
		n=0;
		for(i=0;i<c;i++)
		{
			scanf("%d%d",&p[i],&v[i]);
			int cnt=v[i];
			while(cnt--)
				pos[n++]=p[i];
		}
		sort(pos,pos+n);
		double ans;
		double L=0.0,R=(d+0.0)*n;
		while(R-L>eps)
		{
			double mid=(R+L)/2;
			if(can(mid))
			{
				ans=mid;
				R=mid;
			}
			else
				L=mid;
		}
		printf("Case #%d: %.7lf\n",ca++,ans);
	}
	return 0;
}
