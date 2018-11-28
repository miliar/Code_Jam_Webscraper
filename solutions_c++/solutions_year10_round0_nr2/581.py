#include<iostream>
#include<cstdio>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int ii,tt,n;
long long d[1010];

long long abss(long long x)
{
	if (x<0)return -x;
	else	return x;
}

long long gcd(long long x,long long y)
{
	if (x%y==0)
		return y;
	else
		return gcd(y,x%y);
}

int main()
{
	freopen("bs.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>tt;
	fo(ii,1,tt)
	{
		cin>>n;
		fo(i,1,n)
			cin>>d[i];
		long long t=0,ans;
		fo(i,1,n)
			fo(j,i+1,n)
				if(d[i]!=d[j])
					if (t==0)
						t=abss(d[i]-d[j]);
					else
						t=gcd(t,abss(d[i]-d[j]));
		if (t==0)
			ans=0;
		else	
			ans=(t-d[1]%t)%t;
		cout<<"Case #"<<ii<<": "<<ans<<endl;
	}
	return 0;
}
				
		
	
	
