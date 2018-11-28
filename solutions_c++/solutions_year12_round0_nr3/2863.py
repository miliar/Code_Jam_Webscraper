#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime> 
using namespace std;

typedef long long ll;

int getval(int n) {
	int ans=-1;
	stringstream ss; ss<<n;
	string s=ss.str();
	int sz=s.size();
	for (int i=0; i<sz; i++) {
		s=s.substr(1)+s[0];
		stringstream tt(s); int cur; tt>>cur;
		if(ans==-1) ans=cur;
		else ans=min(ans,cur);
	}
	return ans;
}

int main() {
	int t; cin>>t;
	for (int i=0; i<t; i++) {
		ll ans=0;
		int a,b; cin>>a>>b;
		map<int,int> mp;
		for (int j=a; j<=b; j++) {
			int cur=getval(j);
			mp[cur]++;
		}

		for (map<int,int>::iterator it=mp.begin(); it!=mp.end(); it++) {
			ll cur=(*it).second;
			ans+=cur*(cur-1)/2;
		}

		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
