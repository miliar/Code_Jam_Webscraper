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
__int64 ans,n,t;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	vector<int> v;
	for(test=1;test<=T;test++)
	{
		ans=0;
		cin>>n;
		v.clear();
		v.push_back(0);
		for(int i=0;i<n;i++)
			cin>>t,v.push_back(t);
		for(int i=1;i<=n;i++)
			if(v[i]!=i)
				ans++;
		
		cout<<"Case #"<<test<<": "<<ans<<".000000"<<endl;

	}
	return 0;
}