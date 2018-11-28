#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

long long p[300],s[300],ma[300];

int main()
{
	int _cn,_cc;
	long long m,f,n,i,j,k,r1,r2,si,sj,w,e,u1,u2;
	scanf("%d",&_cn);
	for (_cc=1;_cc<=_cn;++_cc)
	{
		scanf("%lld %lld %lld",&m,&f,&n);
		vector<pair<long long,long long> > q;
		for (i=0;i<n;++i) 
		{
			scanf("%lld %lld",p+i,s+i);
			++s[i];
			q.push_back(make_pair(p[i],s[i]));
		}
		sort(q.begin(),q.end());
		for (i=0;i<n;++i)
		{
			p[i]=q[i].first;
			ma[i]=s[i]=q[i].second;
			for (j=0;j<i;++j) ma[i]-=ma[j];
			if (ma[i]<0) ma[i]=0;
		}
/*		i=0;
		si=0;
		j=m;
		sj=0;
		while (i+1<j)
		{
			k=(i+j)/2;
			r1=m-k*f;
			r2=m-(k+1)*f;
			u1=0;
			u2=0;
			for (w=0;w<n;++w)
			{
				if (r1>0)
				{
					e=r1/p[w];
					if (e>k*ma[w]) e=k*ma[w];
					u1+=e;
					r1-=e*p[w];
				}
				if (r2>0)
				{
					e=r2/p[w];
					if (e>(k+1)*ma[w]) e=(k+1)*ma[w];
					u2+=e;
					r2-=e*p[w];
				}
			}
//			printf("%lld %lld  | %lld %lld\n",k,u1,k+1,u2);
			if (u1>=u2)
			{
				j=k;
				sj=u1;
			} else
			{
				i=k+1;
				si=u2;
			}
		}
		if (si<sj) si=sj;*/
		si=0;
		for (k=0;k<m;++k)
		{
			r1=m-k*f;
			u1=0;
			u2=0;
			for (w=0;w<n;++w)
			{
				if (r1>0)
				{
					e=r1/p[w];
					if (e>k*ma[w]) e=k*ma[w];
					u1+=e;
					r1-=e*p[w];
				} else break;
			}
			if (u1>=si)
			{
				si=u1;
			}
		}
		
		printf("Case #%d: %lld\n",_cc,si);
	}
	return 0;
}
