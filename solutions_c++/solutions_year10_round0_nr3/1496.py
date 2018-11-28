#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
typedef unsigned long long ll;
using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("a.txt", "rt", stdin);
	freopen("b.txt", "wt", stdout);
	#endif

	int t;scanf("%d",&t);
	for (int ii = 0; ii < t; ++ii) {
		int r,k,n;scanf("%d%d%d",&r,&k,&n);
		vector<int>v(n,0);
		for (int i = 0; i < n; ++i) {
			scanf("%d",&v[i]);
		}
		int all = k ;
		vector<int >gto(n,0),ans(n,0);
		for (int i = 0; i < n; ++i) {
			int idx = i,tot = all;
			for(int j = 0 ; j < n && tot - v[idx] >= 0;j++)
				tot -= v[idx],idx = (idx + 1)%n;
			gto[i] = idx;
			ans[i] = all - tot;
		}

		vector<int>vis(n,0);
		ll res = 0ll;
		ll cnt = 0 ,wr = 0;
		for (int i = 0 ; cnt<r &&!vis[i];cnt++, wr = i = gto[i]) {
			res+=ans[i];
		}
		int ratio = r / cnt ;
		res+=(ll)(ratio-1)*res;
		cnt += (ll)(ratio - 1 )*cnt;
		for(int i = cnt ; i < r ; i++)
		{
			res+=ans[wr],wr = gto[wr];
		}
		cout<<"Case #"<<ii+1<<": "<<res<<endl;
	}
	return 0;
}
