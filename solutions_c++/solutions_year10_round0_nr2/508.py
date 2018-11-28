#include<iostream>
#include<stdio.h>
using namespace std;
int gcd(int x,int y)
{
	if(y==0)return x;
	else return gcd(y,x%y);
}
FILE *in=fopen("H://c.in","r");
FILE *out=fopen("D://out.txt","w");
void work()
{
	int a[4];
	int n,m;
	int ans;
	fscanf(in,"%d",&n);
	for(int i=0;i<n;i++)
	{
		fscanf(in,"%d",&a[i]);
	}
	if(n==2)
	{
		m=a[1]-a[0];
		if(m<0)m=0-m;
		ans=m;
	}
	if(n==3)
	{
		m=a[0]-a[1];
		if(m<0)m=0-m;
		n=a[1]-a[2];
		if(n<0)n=0-n;
		ans=gcd(n,m);
	}
   m=a[0]%ans;
   ans=(ans-m)%ans;
   fprintf(out,"%d\n",ans);
}
int main()
{
	int test;
	fscanf(in,"%d",&test);
	for(int cas=1;cas<=test;cas++)
	{
		fprintf(out,"Case #%d: ",cas);
	    work();
	}
	return 0;
}
		
