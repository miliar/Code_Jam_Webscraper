#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int main()
{
int t,n,l;
cin>>t;
for(l=0;l<t;l++)
{
	cin>>n;
	int a[n],b[n],count=0,i,j;
	for(i=0;i<n;i++)
	{
	cin>>a[i]>>b[i];
	}
	for(i=0;i<n;i++)
	{
	for(j=0;j<n;j++)
	{
	if(((a[i]<a[j])&&b[i]>b[j])||((a[i]>a[j])&&b[i]<b[j]))
	count++;
	}
	}
	cout<<"Case #"<<l+1<<": "<<(count/2)<<endl;
}
}
