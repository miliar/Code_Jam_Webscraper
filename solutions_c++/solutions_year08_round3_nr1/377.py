#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <string>
#include <ctime>
using namespace std;
typedef pair<int,int> PI;
int main()
{
		int t,kase=1;
		cin>>t;
		while(t--)
		{
			
			long long int p,k,l,temp;
			cin>>p>>k>>l;
			vector<long long int> f;
			for(int i=0;i<l;i++)
			{
				cin>>temp;
				f.push_back(temp);
			}
			cout<<"Case #"<<kase++<<": ";
			if(p*k<l) {
				cout<<"Impossible"<<endl;
				continue;
			}
			sort(f.rbegin(),f.rend());
			long long int level=1;
			long long int cnt=0;
			long long int ans=0;
			for(int i=0;i<l;i++)			
			{
				ans+=level*f[i];
				
				cnt++;
				if(cnt==k)
				{
					cnt=0;
					level++;
				}
				
			}
			cout<<ans<<endl;
		}
		return 0;
}
