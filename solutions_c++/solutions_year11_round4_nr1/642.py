#include<cstdio>
#include<algorithm>

using namespace std;

#define MX 1005

int tt;
int n,x,s,r,t;
int B[MX],E[MX],W[MX];
int SP[MX*MX];
int P[MX*MX];

int compare(int a,int b)
{
	return SP[a]<SP[b];
}

int main()
{
	scanf("%d",&tt);
	for(int t1=1;t1<=tt;++t1)
	{
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		for(int i=0;i<x;++i)
		{
			SP[i]=-1;
			P[i]=i;
		}
		for(int i=0;i<n;++i)
		{
			scanf("%d%d%d",B+i,E+i,W+i);
			for(int j=B[i];j<E[i];++j) SP[j]=W[i];
		}
		sort(P,P+x,compare);
		long double mam=t,ans=0;
		for(int i=0;i<x;++i)
		{
			int sp=SP[P[i]]==-1?s:SP[P[i]]+s;
			int sp2=SP[P[i]]==-1?r:SP[P[i]]+r;
			if (mam>0)
			{
				long double t2=1/(long double)(sp2);
				if (t2>mam)
				{
					long double s2=mam*sp2;
					ans+=mam+(1-s2)/(long double)sp;
					mam=0;
				}
				else
				{
					mam-=t2;
					ans+=t2;
				}
			}
			else ans+=1/(long double)sp;
			//printf("%.11lf %.11lf\n",(double)sp,(double)ans);
		}
		printf("Case #%d: %.11lf\n",t1,(double)ans);
	}
	return 0;
}
