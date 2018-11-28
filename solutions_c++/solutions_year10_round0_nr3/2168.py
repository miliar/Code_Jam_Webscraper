#include <cstdlib>
#include <iostream>
#include<fstream>

using namespace std;
long g[2000];
int main()
{
	ifstream cin("C-small-attempt4.in");
	ofstream cout("C-small-attempt4.out");
	long i,j,t,n,m,k,r,sum,ans,p,q;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>r>>k>>n;
		for(i=0;i<n;i++)
		{
			cin>>g[i];
		}
		p=0;
		ans=0;
		for(i=0;i<r;i++)
		{
			sum=k;
			q=p;
			if(g[p]<=sum)
			{
				sum-=g[p];
				p++;
				if(p>=n)p=0;
			}
			while(g[p]<=sum&&p!=q)
			{
				sum-=g[p];
				p++;
				if(p>=n)p=0;
			}
			ans=ans+k-sum;
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
    return 0;
}
