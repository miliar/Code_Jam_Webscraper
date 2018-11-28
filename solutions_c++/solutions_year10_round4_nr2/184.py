#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
long long test,p,a[2050],b[2050],f[2050][15],n;
int oo=100000*2000;

void init()
{
	cin>>p;	
	n=1<<p;
	for (int i=1;i<=n*2;i++)
		for (int j=0;j<=p+1;j++) 
			f[i][j]=oo;
	for (int i=n;i>=1;i--) 
	{
		cin>>a[i];
		for (int j=0;j<=a[i];j++) f[i+n-1][j]=0;
	}
	for (int i=n-1;i>=1;i--) cin>>b[i];
}

void dp(long long i,long long k)
{
	if (i>=n) return;
	if (k>p) { f[i][k]==oo; return; }
	long long x,y;
    dp(i*2,k);    dp(i*2,k+1);
    dp(i*2+1,k);  dp(i*2+1,k+1);
	x=f[i*2][k+1]+f[i*2+1][k+1];
	y=f[i*2][k]+f[i*2+1][k]+b[i];
	f[i][k]=min(x,y);
//	cout<<i<<" "<<k<<" "<<f[i][k]<<endl;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>test;
	long long  ans=oo;
	for (long long t=1;t<=test;t++)
	{
		init();
		for (int i=0;i<=p;i++) dp(1,i);
		ans=f[1][0];
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	fclose(stdin);	fclose(stdout);
	return 0;
}
	

