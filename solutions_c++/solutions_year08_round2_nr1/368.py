#include<cstdio>
#include<vector>
using namespace std;
vector<int> a[1001];
bool viz[1001];
long long nr;
long long t,A,B,p,k;
int prim(long long x)
{
	for(long long i=2;i<=x/2;i++)
		if(x%i==0) return 0;
	return 1;
}
long long nextprim(long long x)
{
	x++;
	while(!prim(x)) x++;
	return x;
}
void df(int vf)
{
	viz[vf]=1;
	for(int i=0;i<a[vf].size();i++)
		if(!viz[a[vf][i]]) df(a[vf][i]);
}
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%lld",&t);
	for(k=1;k<=t;k++)
	{
		for(int i=0;i<=1000;i++)
			a[i].clear();
		memset(viz,0,sizeof(viz));
		scanf("%lld %lld %lld",&A,&B,&p);
		p=nextprim(p-1);
		while((A/p+(A%p==0?1:2))*p<=B)
		{
			int x=(A/p+(A%p==0?0:1))*p;
			for(int i=x+p;i<=B;i+=p)
			{
				a[x-A].push_back(i-A);
				a[i-A].push_back(x-A);
			}
			p=nextprim(p);
		}
		nr=0;
		for(int i=0;i<=B-A;i++)
			if(!viz[i])
			{
				nr++;
				df(i);
			}
		printf("Case #%lld: %lld\n",k,nr);
	}
	fclose(stdout);
	return 0;
}
