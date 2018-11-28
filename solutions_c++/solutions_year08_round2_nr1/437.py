#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

long long n,M,t,A,B,C,D,x0,y0,ans;
long long pnt[110][2];

int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	scanf("%lld",&t);
	for(int cs=1;cs<=t;cs++)
	{
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		memset(pnt,0,sizeof(pnt));
		ans=0;
		pnt[0][0]=x0,pnt[0][1]=y0;
		for(int i=1;i<n;i++)
		{
			x0 = (A * x0 + B) % M;
			y0 = (C * y0 + D) % M;
			pnt[i][0]=x0;
			pnt[i][1]=y0;
		}
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				for(int k=j+1;k<n;k++)
				{
					long long sumx=0,sumy=0;
					sumx=pnt[i][0]+pnt[j][0]+pnt[k][0];
					sumy=pnt[i][1]+pnt[j][1]+pnt[k][1];
					if(sumx%3==0 && sumy%3==0)ans++;
				}
			}
		}
		printf("Case #%d: %lld\n",cs,ans);
	}
	return 0;
}
