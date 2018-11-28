#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;



int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	long long i,j,k,l,t,n,m;
	cin>>t;
	for(l=1;l<=t;++l)
	{
		cin>>n>>m>>k;
		long long ans = 0;
		long long tmp = 0;
		n*=k;
		while(n<m)
		{
			n*=k;
			++tmp;
		}
		while(tmp > 0)
		{
			++ans;
			tmp/=2;
		}
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}
	return 0;
}