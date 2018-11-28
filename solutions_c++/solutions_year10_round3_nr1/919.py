#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
int main()
{
	int t,k,i,j,count=0,n,x,y;
	cin>>t;
	vector <int> a,b;
	for(k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		cin>>n;
		a.clear();
		b.clear();
		count=0;
		for(i=0;i<n;i++)
		{
			cin>>x>>y;
			a.push_back(x);
			b.push_back(y);
		}
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(((a[i]>=a[j]) && (b[i]>=b[j])) || ((a[i]<=a[j]) && (b[i]<=b[j])))
					continue;
				else
					count++;
			}
		}
		cout<<count<<"\n";
	}
}
