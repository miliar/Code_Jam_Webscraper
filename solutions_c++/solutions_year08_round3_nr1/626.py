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
#include <cstdlib>
#include <ctime>
using namespace std;
int test,n,p,k;
int main()
{
	cin>>test;
	for(int i1=1;i1<=test;++i1)
	{
		cin>>n>>p>>k;
		vector<int> a(k);
		for(int i=0;i<k;i++)
			cin>>a[i];
		sort(a.begin(),a.end());
		int cnt=0,ans=0;
		for(int j=0;j<a.size()-0;j++){
			if(j%p==0)
				cnt++;
			ans+=a[a.size()-j-1]*cnt;
		}
		cout<<"Case #"<<i1<<": ";
		cout<<ans<<endl;
	}
}