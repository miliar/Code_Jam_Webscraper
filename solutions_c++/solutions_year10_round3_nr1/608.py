#include<iostream>
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<string>
#include<cctype>
using namespace std;
int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	int u=1;
	while(t-->0)
	{
		int n;
		cin>>n;
		int i,x,y;
		vector<int> a,b;
		for(i=0;i<n;i++)
		{
			cin>>x>>y;
			a.push_back(x);
			b.push_back(y);
		}
		int j,count=0;
		for(i=0;i<n-1;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(a[i]>a[j] &&b[i]>b[j])
					continue;
				if(a[i]<a[j] && b[i]<b[j])
					continue;
				count++;
			}
		}
		cout<<"Case #"<<u<<": "<<count<<endl;
		u++;
	}
}
