#include <stdio.h>

int a[1001][1001],nr;
long intrv, g[1001];
long long sr;

bool exists(int v[])
{
	int i,j,k;
	bool ok = false;
	for(i=0;i<nr;++i)
	{
		ok = v[0]==a[i][0];
		if(!ok)
			continue;
		for(j=1;j<=a[i][0];++j)
		{
			if(a[i][j]!=v[j])
			{
				ok = false;
				break;
			}
		}
		if(ok)
			break;
	}
	if(!ok)
	{
		for(i=0;i<=v[0];i++)
			a[nr][i] = v[i];
		nr++;
		return false;
	}
	else
	{
		if(!sr)
		{
			for(j=i;j<nr;++j)
				for(k=1;k<=a[j][0];++k)
					sr += g[a[j][k]];
			intrv = nr-i;
		}
		return true;
	}
}

long long sol(long r, long k, int n)
{
	long i, rem;
	long long s, s2=0;
	int p = 0, pant, v[1001];
	for (i=1; i<=r; ++i)
	{
		s = v[0] = 0;
		pant = p;
		while (s + g[p] <= k)
		{
			v[++v[0]] = p;
			s += g[p++];
			p %= n;
			if(p == pant)
				break;
		}
		if(exists(v))
		{
			if(r - i > intrv)
			{
				rem = (r - i) / intrv;
				i += rem * intrv - 1;
				s2 += sr * rem;
				p = pant;
			}
			else
				s2 += s;
		}
		else
			s2 += s;
	}
	return s2;
}

int main()
{
	long k, r;
	long long ans;
	int t, i, j, n;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for (i=1; i<=t; ++i)
	{
		scanf("%ld %ld %d",&r,&k,&n);
		for (j=0; j<n; ++j)
			scanf("%ld",&g[j]);
		sr = nr = 0;
		ans = sol(r,k,n);
		printf("Case #%d: %lld\n",i,ans);
	}
	return 0;
}
