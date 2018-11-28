#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
//#include <cmath>
//#include "lcgrand.c"

using namespace std;

const int nmax=50;

int x[nmax],v[nmax];

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,n,m,i,j,b,tm,ans,taken;
	char s[200];
	string q;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n>>m>>b>>tm;
		for(i=0;i<n;i++) cin>>x[i];
		for(i=0;i<n;i++) cin>>v[i];

		ans=0;
		taken=0;
		for(i=n-1;i>=0 && taken<m;i--)
		{
			if (x[i]+v[i]*tm<b) continue;
			ans+=n-i-1-taken;
			++taken;
		}

		printf("Case #%d: ",t);
		if (taken<m) puts("IMPOSSIBLE"); else printf("%d\n",ans);
	}
	

	return 0;
}