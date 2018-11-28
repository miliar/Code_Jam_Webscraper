#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <iostream>

using namespace std;

int main(void)
{
	int t;
	cin>>t;
	
	for(int caseN=1;caseN<=t;caseN++)
	{
		int n;
		string field[40];
		cin>>n;
		int last[40];
		for(int i=0;i<n;i++) 
		{
			cin>>field[i];
			last[i]=-1;
			for(int j=0;j<n;j++) if(field[i][j]=='1') last[i]=j;
		}

		int ans=0;
		for(int i=0;i<n;i++)
		{
			for(int j=i;j<n;j++)
			{
				if(last[j]<=i)
				{
					for(int k=j;k>i;k--) swap(last[k], last[k-1]);
					ans+=(j-i);
					break;
				}
			}
		}

		cout<<"Case #"<<caseN<<": "<<ans<<endl;
	}

	return 0;
}
