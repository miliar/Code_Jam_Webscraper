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

// Google CodeJam 2012 Round 2
// Author: Fdg

pair <int,int> v[10002];
int len[10002];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;++test) {
		printf("Case #%d: ",test);
		int n,d;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%d%d",&v[i].first,&v[i].second);
		scanf("%d",&d);
		bool ok=false;
		memset(len,0,sizeof(len));
		len[0]=min(v[0].second,v[0].first);
		int maxd=v[0].first+len[0],last=1;
		for(int i=0;i<n;++i) {
			if (v[i].first+len[i]>=d) {
				ok=true;
				break;
			}
			maxd=max(maxd,v[i].first+len[i]);
			while(last<n&&maxd>=v[last].first) {
				len[last]=min(v[last].second,v[last].first-v[i].first);
				++last;
			}
		}
		puts(ok ? "YES" : "NO");
	}
	return 0;
}
