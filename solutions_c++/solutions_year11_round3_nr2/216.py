// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

LL T;
int L,N,C;
int a[1005];
LL cum_dist[1000005];
int dist[1000005];

int fun(int b1,int b2) {
	LL ans = 0;
	for(int i=0;i<N;++i) {
		if(i!=b1 && i!=b2) {
			ans += 2 * dist[i];
			continue;
		}
		LL mt = max(T, ans);
		LL slow_dist = min((mt - ans) /2, (LL)dist[i]);
		LL rem_dist = max(0LL,dist[i] - slow_dist);
		ans += slow_dist * 2 + rem_dist;
	}
	return ans;
}

LL get_gain(int i) {
	LL mt=max(cum_dist[i],T);
	LL slow_dist = min((mt - cum_dist[i]) /2, (LL)dist[i]);
	LL rem_dist = max(0LL,dist[i] - slow_dist);
	return rem_dist;
}

void print(vector<LL> &a) {
	puts("");
	for(int i=0;i<SZ(a);++i) cout<<a[i]<<" ";
	puts("");
}

void solve() {
	cin>>L>>T>>N>>C;

	for(int i=0;i<C;++i) {
		scanf("%d",&a[i]);
	}

	cum_dist[0]=0;
	for(int i=0;i<N;++i) {
		dist[i] = a[i%C];
		cum_dist[i+1] = 2*dist[i] + cum_dist[i];
	}
	LL ans = cum_dist[N];
	vector<LL> gain;
	for(int i=0;i<N;++i)
		gain.push_back(get_gain(i));
	sort(gain.rbegin(),gain.rend());
	for(int i=0;i<L;++i)
		ans -= gain[i];
	cout<<ans<<"\n";
}

int main() {
	int tc;
	scanf("%d",&tc);
	for(int t=1;t<=tc;++t) {
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}

