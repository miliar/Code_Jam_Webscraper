#include<iostream>
#include<algorithm>
using namespace std;
unsigned int a[1000],b[1000];
int main()
{
	unsigned int p,k,l,N,i;
	cin>>N; 
	unsigned int f=0,cnt;
	while(f<N)
	{
		cnt=0;
		cin>>p>>k>>l;
		for(i=0;i<l;i++)
		{
			cin>>a[i];
			
		}
		sort(a,a+l);
		for(i=0;i<l;i++)
		{
		
			b[i]=a[l-i-1];
		}
		for(i=0;i<l;i++)
			cnt+=(b[i]*((i/k)+1));
		f++;
		cout<<"Case #"<<f<<": "<<cnt<<endl;
	}
}
		
		
