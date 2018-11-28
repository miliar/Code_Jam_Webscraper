#include<iostream>
#include<algorithm>
using namespace std;
#define N 900
long long a[N],b[N];
bool cmp(int a,int b)
{
	if(a>b) return 1;
	else return 0;
}
int main()
{
	
	freopen("A-large.in","r",stdin);
	freopen("Alarge.out","w",stdout);
	long long i,j,k,n,s,ns(0);
	cin>>s;
	while(ns<s)
	{
		cin>>n;
		for(i=0;i<n;i++)
			cin>>a[i];
		sort(a,a+n);
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(b,b+n,cmp);
		k=0;
		for(i=0;i<n;i++)
			k+=(a[i]*b[i]);
		cout<<"Case #"<<++ns<<": "<<k<<endl;
	}
	return 0;
}
