#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;




int main()
{
	int t;	
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int n;
		cin>>n;
		vector<pair<char,int> > buttons(n);
		for(int j=0;j<n;j++)
		{
			cin>>buttons[j].first;
			cin>>buttons[j].second;
		}
		int orange_current=1,blue_current=1;
		int totaltime=0;
		int blue_time=0,orange_time=0;
		for(int i=0;i<buttons.size();i++)
		{
			int t;
			if(buttons[i].first=='O')
			{
				t=max(abs(buttons[i].second-orange_current)+orange_time+1,totaltime+1);
				orange_current=buttons[i].second;
				orange_time=t;
			}
				
			if(buttons[i].first=='B')
			{
				t=max(abs(buttons[i].second-blue_current)+blue_time+1,totaltime+1);
				blue_current=buttons[i].second;
				blue_time=t;
			}
			totaltime=t;
			//cout<<totaltime<<endl;
		}
		printf("Case #%d: %d\n",k,totaltime);


	}	
	return 0;
}
