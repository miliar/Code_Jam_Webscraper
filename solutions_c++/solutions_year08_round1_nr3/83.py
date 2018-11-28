#include <iostream>
#include <cmath>
using namespace std;

long n,t,i,kk,total,w,z1,z2;
long a[2000],c[2000],q1,q2;
long b[2000];

long cal2(long x)
{
	long w,q;
	long z;
	z=x;
	q=1;
	for (w=31;w>=1;w--) if (z>=b[w])
	{
		q=(q*c[w])%1000;
		z=z-b[w];
	}
	return q;
}


long cal(long x)
{
	long v1,v2,g,q;
	if (x==1) return 6;
	else if (x==2) return 28;
	if (x%2==0) 
	{
		q=x/2;
		v1=cal(q);
		g=cal2(q);
		return (v1*v1+2000-2*g)%1000;
	}
	else
	{
		q=x/2;
		v1=cal(q);
		v2=cal(q+1);
		g=cal2(q);
		return (v1*v2+6000-6*g)%1000;
	}
}


int main()
{
	freopen("C-large.in","r",stdin);
	freopen("test.out","w",stdout);
	a[1]=6;
	c[1]=4;
	b[1]=1;
	for (i=2;i<=31;i++)
	{
		c[i]=(c[i-1]*c[i-1])%1000;
		a[i]=(a[i-1]*a[i-1]+1000-2*c[i-1])%1000;
		b[i]=b[i-1]*2;
	}
	cin>>t;
	for (kk=1;kk<=t;kk++)
	{
		cin>>n;
		total=(cal(n)+999)%1000;
		if (total<10) cout<<"Case #"<<kk<<": "<<"00"<<total<<endl;
		else if (total<100 && total>=10) cout<<"Case #"<<kk<<": "<<"0"<<total<<endl;
		else cout<<"Case #"<<kk<<": "<<total<<endl;
	}
	return 0;
}

