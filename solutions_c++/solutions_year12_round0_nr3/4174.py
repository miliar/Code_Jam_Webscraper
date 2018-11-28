#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
bool cmp(int,int);
bool cmp(int a,int b)
{
	return a<b;
}
int Count(int x,int max)
{
	int a[11],i=0,j,y,k,t=x,n=0,sum=0,b[11],g,temp;
	while(t!=0)
	{
		a[n++]=t%10;
		t=t/10;
	}
	for(i=0,j=n-1;i<j;i++,j--)
		a[i]^=a[j]^=a[i]^=a[j];
	for(k=1;k<n;k++)
	{
		temp=a[n-1];
		for(j=n-1;j>=1;j--)
			a[j]=a[j-1];
		a[0]=temp;
		for(j=0,y=0;j<n;j++)
				y=y*10+a[j];
		if(y>x&&y<=max) sum=sum+1;
	}
	return sum;
}
int main()
{
    int t,i,j,a,b,s;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>a>>b;
		for(j=a,s=0;j<b;j++)
			s=s+Count(j,b);
		cout<<"Case #"<<i<<": "<<s<<endl;
	}
    return 0;
}
