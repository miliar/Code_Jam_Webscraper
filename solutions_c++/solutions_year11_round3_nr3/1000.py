#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
#include<climits>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
	int cases;
	cin>>cases;
	for(int numCase=1;numCase<=cases;numCase++)
	{
		int n,l,h;
		cin>>n>>l>>h;
		vector<int> a(n);
		for(int i=0;i<n;i++)
		cin>>a[i];
		int found=0,win;

		for(int i=l;i<=h;i++)
		{
			int count=0;
			for(int j=0;j<n;j++)
			{
				int mini=min(a[j],i);
				int maxi=max(a[j],i);
				if((maxi%mini)!=0)
				{
					count=1;
					break;
				}
					
			}
			if(count==0)
			{
				found=1;
				win=i;
				break;
			}

		}
		
		cout<<"Case #"<<numCase<<": ";
		if(found==1)
			cout<<win<<endl;
		else cout<<"NO"<<endl;
	}	
	return 0;
}
