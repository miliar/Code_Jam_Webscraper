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
__int64 ans,n,t,x,m,s;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	vector<int> v;
	for(test=1;test<=T;test++)
	{
		s=0;
		m=1e9;
		cin>>n;
		v.clear();
		for(int i=0;i<n;i++)
			cin>>t,v.push_back(t),m=min(m,t),s+=t;
		x=v[0];
		for(int i=1;i<n;i++)
			x^=v[i];
		if(x)
			cout<<"Case #"<<test<<": "<<"NO"<<endl;
		else
		{
			cout<<"Case #"<<test<<": "<<s-m<<endl;
		}
	}
	return 0;
}