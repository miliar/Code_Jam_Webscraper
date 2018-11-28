#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <stdio.h>
#include <queue>



using namespace std;
int T,test;
__int64 ans,n,l,t,c,k,sum;
vector<__int64> d;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	for(test=1;test<=T;test++)
	{
		d.clear();
		cin>>l>>t>>n>>c;

		ans=t;
		sum=0;
		for(int i=0;i<c;i++)
			cin>>k,d.push_back(2*k);
		for(int i=c;i<n;i++)
			d.push_back(d[i%c]);
		for(int i=0;i<n;i++)
			sum+=d[i];
		__int64 post=0,cur=0,ost=t;
		for(int i=0;i<n;i++)
		{
			cur+=d[i];
			if(cur<=t)
			{
				ost-=d[i],d[i]=0;
				continue;
			}
			if(cur>t)
			{
				d[i]-=ost;
				break;
			}

		}
		sort(d.begin(),d.end());
		reverse(d.begin(),d.end());
		for(int i=0;i<l&&i<n;i++)
			d[i]/=2;
		for(int i=0;i<n;i++)
			ans+=d[i];
		if(sum<=ans)
		{
			ans=sum;
			cout<<"Case #"<<test<<": "<<ans<<endl;
			continue;
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}