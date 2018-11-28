#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
const long long MAXP=1000009;
const double o=1e-7;
bool prime[MAXP+100];
long long p[80000],t,n;

void preprime()
{
	memset(prime,0,sizeof(prime));	p[0]=0;
	for (long long i=2;i<MAXP;i++)
		if (!prime[i])
		{
			p[++p[0]]=i;
			for (long long j=1;i*j<MAXP;j++)	prime[i*j]=true;
		}
}

void work()
{
	long long ans=0;
	for (int i=1;p[i]<=n && i<MAXP;i++)
	{
		ans+=(int)floor(log((double)n)/log((double)p[i])+o) -1;
	}
	if (n>1) cout<<ans+1<<endl; else cout<<0<<endl;
}

int main()
{
	freopen("c.in","r",stdin);	freopen("c.out","w",stdout);
	preprime();
	cin>>t;	
	for (long long test=1;test<=t;test++)
	{
		cin>>n;
		cout<<"Case #"<<test<<": ";
		work();
	}
	return 0;
}

