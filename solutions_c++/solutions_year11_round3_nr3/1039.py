#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(ini,n) for(int i=ini;i<n;i++)
int fre[110];
int main()
{
	int t,n,h,l;
	cin>>t;
	
	for(int test=1;test<=t;test++)
	{
		cout<<"Case #"<<test<<": ";
		cin>>n>>l>>h;
		rep(0,n)
		{
			cin>>fre[i];
		}
		int i;
		for(i=l;i<=h;i++)
		{
			int f;
			for(f=0;f<n;f++)
			{
				if(!(i<fre[f] && fre[f]%i==0 || i>=fre[f] && i%fre[f]==0))
				break;
			}
			
			if(f==n)
			{
				cout<<i<<endl;
				goto next;
			}
			
		}
		if(i>=h+1)
		cout<<"NO"<<endl;
	next: int a;
	}





	return 0;
}
