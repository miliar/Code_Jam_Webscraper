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
__int64 ans,n,l,r,t;
vector<int> v;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	for(test=1;test<=T;test++)
	{
		ans=-1;
		cin>>n>>l>>r;
		
		v.clear();
		for(int i=0;i<n;i++)
			cin>>t,v.push_back(t);
		for(int i=l;i<=r;i++)
		{
			bool ok=true;
			for(int j=0;j<n;j++)
			{
				if(i<v[j]&&v[j]%i==0)
					continue;
				if(i>=v[j]&&i%v[j]==0)
					continue;
				ok=false;
				break;
			}
			if(ok)
			{
				ans=i;
				break;
			}
		}

		cout<<"Case #"<<test<<": ";
		if(ans==-1)
			cout<<"NO"<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;
}