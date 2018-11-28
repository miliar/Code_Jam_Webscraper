#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

void f(long long pos, long long sum, long long s1, long long s2,long long c1,long long c2);

long long t,k,n,a[1010],p1[1010],p2[1010],maxx;

int main()
{
	freopen("C-small-attempt0.in","r",stdin); freopen("C-small.out","w",stdout);
	//freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
	
	long long c;
	
	cin>>t;
	
	for(k=1;k<=t;k++)
	{
		
		cin>>n;
		
		for(c=0;c<n;c++)
			cin>>a[c];
			
		maxx=-1;
			
		f(0,0,0,0,0,0);
		
		cout<<"Case #"<<k<<": ";
		
		if(maxx==-1) cout<<"NO";
		else cout<<maxx;
		
		cout<<endl;
	}
	return 0;
}


void f(long long pos, long long sum, long long s1, long long s2,long long c1,long long c2)
{
	//cout<<pos<<" "<<sum<<" "<<s1<<" "<<s2<<c1<<" "<<c2<<endl;
	
	if(pos==n)
	{
		if(s1==s2  && c1!=0 && c2!=0) if(sum>maxx) maxx=sum;
	}
	else
	{
		f(pos+1,sum+a[pos],s1^a[pos],s2,c1+1,c2);
	
		f(pos+1,sum,s1,s2^a[pos],c1,c2+1);
	}
}
