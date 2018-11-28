#include<iostream>
#include<cstring>
#include<math.h>
using namespace std;

int check(int a[],int b[],int n)
{
int j,k,count=0;
	for(j=0;j<(n-1);j++)
	{
		for(k=j+1;k<n;k++)
		{
			if((a[k]>a[j]&&b[k]<b[j])||(a[j]>a[k]&&b[j]<b[k]))
			count++;
		}
	}
return count;
}
int main()
{
    int t,n,i,j,k,ans;
	int a[1000],b[1000];
	i=0;
	cin>>t;
	while(i<t)
	{
		cin>>n;
		for(j=0;j<n;j++)
		cin>>a[j]>>b[j];
		ans=check(a,b,n);
		cout<<"Case #"<<i+1<<": "<<ans<<"\n";
		i++;
	}
    return 0;
}
