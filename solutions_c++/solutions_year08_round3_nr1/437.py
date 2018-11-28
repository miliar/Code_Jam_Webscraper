#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <numeric>

using namespace std;

#define v vector <int>
#define vs vector <string>
#define vv vector< v >
#define forz(i,n) for(int i=0;i<n;i++)
#define fl(i,s,n) for(int i=s;i<n;i++)
#define lh(i) int(i.length())
#define sz(i) (int)(i.size())
#define pb(a) push_back(a)
#define all(a) a.begin(),a.end()
#define mp make_pair

int main()
{
	int t,ot=0;
	cin>>t;
	while(t--)
	{
		int flg=0;
		int p,k,l;
		cin>>p>>k>>l;
		vector <long long> arr(l,0);
		forz(i,l)cin>>arr[i];
		sort(all(arr));
		reverse(all(arr));
		long long cnt=1;
		long long ans=0;
		if(flg==0)
		{
			for(int i=0;i<l;i+=k)
			{
				for(int s=i;s<i+k&&s<l;s++){ans+=arr[s]*cnt;}	
				cnt++;
			}
			cout<<"Case #"<<++ot<<": "<<ans<<endl;
		}	
	}	
	return 0;
}



