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
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int a[2000],b[2000];
	int i,j,l,t,n,k;
	cin>>t;
	for(l=1;l<=t;++l)
	{
		cin>>n;
		for(i=0;i<n;++i)
			cin>>a[i]>>b[i];
		int ans = 0;
		for(i=0;i<n;++i)
			for(j=i+1;j<n;++j)
				if((a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j] ))
					++ans;
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}


	return 0;

}