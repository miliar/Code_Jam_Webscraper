#include<iostream>
#include<algorithm>
using namespace std;
long long arr[1005],z[1005];

long long gcd(long long m, long long n) {
	while (true) {
		if (n!=0&&(m = m % n) == 0) return n;
		if ((n = n % m) == 0) return m;
	}
}
bool cmp(long long a,long long b)
{
	return a<b;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i,g=0,t,m,k;
	long long ans,cd;
	scanf("%d",&t);
	bool flag;
	for(g=0;g<t;g++)
	{
		flag=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lld",&z[i]);
		}
		sort(z,z+n,cmp);
		for(i=1;i<n;i++)
		{
			arr[i-1]=z[i]-z[i-1];
		}
		cd=arr[0];
		m=n-1;
		for(i=1;i<m;i++)
		{
			cd=gcd(cd,arr[i]);
		}
		for(i=0;i<n;i++)
		{
			z[i]=z[i]%cd;
			if(z[i]!=0)z[i]=cd-z[i];
		}
		k=0;ans=0;
		long long brr[1001];
		while(1)
		{
			for(i=0;i<n;i++)brr[i]=z[i]+k*cd;
			for(i=1;i<n;i++)
			{
				if(brr[i]!=brr[i-1])break;
			}
			if(i==n)
			{
				ans=z[0]+k*cd;
				break;
			}
			k++;
		}
		printf("Case #%d: %lld\n",g+1,ans);
	}
	return 0;
}
		