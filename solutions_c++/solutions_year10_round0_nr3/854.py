#include <cstdio>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
#include <algorithm>
#include <set>
#include <deque>
#include <stack>
#include <numeric>
#include <functional>
#include <map>
#include <queue>
using namespace std;
struct pp
{
	long long s,n;
};
long long t,q,r,k,n,a,i,j,sum,s,kl,ip;
	pp nt[1000];
	vector<long long > v;
int main(void)
{
	FILE *f;
	f=fopen("Cb.in","r");
	freopen("Cb.out","w",stdout);
	fscanf(f,"%lld",&t);
	for (q=1;q<=t;q++)
	{
		v.clear();
		fscanf(f,"%lld%lld%lld",&r,&k,&n);
		for (i=0;i<n;i++)
		{
			fscanf(f,"%lld",&a);
			v.push_back(a);
		}
		for (i=0;i<n;i++)
		{
			nt[i].n=-1;
			nt[i].s=-1;
		}
		i=0;
		j=0;
		sum=0;
		while ((j<r)&&(nt[i].n==-1))
		{
			nt[i].n=j;
			nt[i].s=sum;
			s=0;
			ip=i;
			while ((s+v[i])<=k)
			{
				s+=v[i];
				i=(i+1)%n;
				if (i==ip)
					break;
			}
			sum+=s;
			j++;
		}
		if (j==r)
			printf("Case #%lld: %lld\n",q,sum); else
		{
			r-=(j-nt[i].n);
			r-=nt[i].n;
			kl=r/(j-nt[i].n);
			r%=(j-nt[i].n);
			sum+=kl*(sum-nt[i].s);
			j=0;
			while (j<r)
			{
				s=0;
				while ((s+v[i])<=k)
				{
					s+=v[i];
					i=(i+1)%n;
				}
				sum+=s;
				j++;
			}
			printf("Case #%lld: %lld\n",q,sum);
		}
	}
	fclose(f);
	fclose(stdout);
	return 0;
}

