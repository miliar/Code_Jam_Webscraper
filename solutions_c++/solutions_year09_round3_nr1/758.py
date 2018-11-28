#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	long long int i,j,t,k,ck,cn,p,c[1000],b[1000],l,r,sum;
	char a[1000],s[1000];
	
	freopen("a123.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> t;
	for(i=1;i<=t;i++)
	{
	cin >> s;
	
	for(j=0;j<1000;j++)
	c[j]=-1;
	
	
	l=strlen(s);
	
	
	for(j=0;j<l;j++)
	{
		if(c[s[j]]==-1)
		c[s[j]]=1;
	}
	
	p=0;
	for(j=0;j<1000;j++)
	if(c[j]==1)
	p++;
	
	for(j=0;j<1000;j++)
	c[j]=-1;
	
	b[0]=1;
	c[s[0]]=1;
	
	cn=0;
	for(j=1;j<l;j++)
	{
		if(cn==1)
		cn++;
		
		if(c[s[j]]==-1)
		{
			c[s[j]]=cn;
			b[j]=cn;
			cn++;
		}
		else
		b[j]=c[s[j]];
	}
	
	r=1;
	sum=0;
	if(p==1) p=2;
	for(j=l-1;j>=0;j--)
	{
		
		sum=sum+b[j]*r;
		r=r*p;
		
	
	}
	
	 
	cout <<"Case #"<<i <<": "<<sum<<'\n';
	}
return 0;
}
