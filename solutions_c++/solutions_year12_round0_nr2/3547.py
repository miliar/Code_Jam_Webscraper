#include<iostream>
#include<vector>

#include <algorithm>
using namespace std;
bool myfunction(int i,int j) 
{ 
	return (i>j); 
}
int main()
{
	int t;
	int i;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int n,s,p;
		cin>>n>>s>>p;
			
		int p3=3*p;
		vector<int> a(n);
		int count=0;
		for(i=0;i<n;i++)
			cin>>a[i];
		sort(a.begin(),a.end(),myfunction);
		//cout<<p3;
		for(i=0;i<n;i++)
		{
		//	cout<<a[i]<<" ";
			if(a[i]>p3-3)
				count++;
			else if(s>0)
			{
				if((a[i]==p3-3 || a[i]==p3-4) && a[i]>0)
				{
					count++;
					s--;
				}
				else
					break;
			}
			else if(s==0)
				break;
			else
				break;
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
	}
}
