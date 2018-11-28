#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<utility>
using namespace std;
int main()
{
	int t;
	cin>>t;
	
	for(int q=0;q<t;q++)
	{
		map<pair<long ,long>,int >ma;
		long a,b;
		cin>>a>>b;
		int nod=1;
		long x=a,pow=1;
		x/=10;			
		while(x)
		{
			x=x/10;
			pow*=10;
			nod++;
		}
		long count=0;
		for(long i=a;i<=b;i++)
		{
			x=i;
			for(int j=1;j<nod;j++)
			{
				long m=x%10;
				x/=10;
				m=m*pow+x;
				if(m>i && m<=b && !ma[make_pair(i,m)])
				{
					//cout<<i<<" "<<m<<"\n";		
					count++;
					ma[make_pair(i,m)]=1;
				}
				x=m;
			}
		}
		cout<<"Case #"<<q+1<<": "<<count<<"\n"; 
		
	}	
}
