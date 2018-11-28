#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
long long ans[51];
long long po[8]={1,10,100,1000,10000,100000,1000000,10000000};
int len(long long x)
{
	int i=0;
	while(x>0) { x /= 10; i++;}
	return i;
}
int rotate(long long x,long long a,long long b,int s)
{
//	cout<<"dbjb";
	long long lt[8];
	long long q=0,r,y=x,p=0;
	for(int i=0; i<s; i++)
	{
		x=y;
		r=x%po[i+1];
		 x/=po[i+1];
		x += po[s-i-1]*r;
		if(x>=a && x<=b && x>y)  { lt[p]=x;p++;}
	}
	sort(lt,lt +p);
	for(int i=0; i<p-1; i++)
	if(lt[i] != lt[i+1]) q++;
	if(p>0) q++;
	return q;
}
int main()
{
	int T;cin>>T;long long a,b;int s;
	for(int i=0; i<T; i++)
	{
		cin>>a>>b;long long j=a;s=len(a);ans[i]=0;
		while(j<=b)
		{
			ans[i] += rotate(j,a,b,s);
			j++;
		}
	}
	for(int i=0; i<T; i++) 
	{ cout<<"Case #"<<(i+1)<<": "<<ans[i]<<endl; }
}
