#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <climits>
#include <cfloat>
#include <ctime>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
using namespace std;

typedef long long LL;
template<class T> void minimize(T& a, T b) { a = min(a, b); }
template<class T> void maximize(T& a, T b) { a = max(a, b); }
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()

bool iss[1<<16];
int dp[1<<16];
vector<int> subsets[1<<16];

int solve() {
	int n,k;
	cin>>n>>k;
	vector<vector<int> > st(n, vector<int>(k));
	for (int i=0; i<n; ++i) {
		for (int j=0; j<k; ++j) {
			cin>>st[i][j];
		}
	}
	vector<vector<int> > G(n,n);
	for (int i=0; i<n; ++i) {
		for (int j=0; j<n; ++j) {
			G[i][j]=G[j][i]=1;
			for (int t=0; t+1<k; ++t) {
				if (st[i][t]==st[j][t] || st[i][t+1]==st[j][t+1]) {
					G[i][j]=G[j][i]=0;
					break;
				}
				if ((st[i][t]-st[j][t]>0) != (st[i][t+1]-st[j][t+1]>0)) {
					G[i][j]=G[j][i]=0;
					break;
				}
			}
		}
	}
	
	memset(iss,0,sizeof iss);
	vector<int> ss;
	for (int subset=1; subset<(1<<n); ++subset) {
		bool ok=1;
		for (int i=0; ok && i<n; ++i) if (subset&(1<<i)) {
			for (int j=i+1; ok && j<n; ++j) if (subset&(1<<j)) {
				if (!G[i][j]) {
					ok=false;
				}
			}
		}
		if (ok) {
			iss[subset]=1;
			ss.push_back(subset);
		}
		subsets[subset].clear();
		for (int i=subset; i>0; i=(i-1)&subset) {
			if (iss[i]) {
				subsets[subset].push_back(i);
			}
		}
	}
	dp[0]=0;
	for (int subset=1; subset<(1<<n); ++subset) {
		dp[subset]=1000;
		for (int i=0; i<subsets[subset].size(); ++i) {
			minimize(dp[subset],1+dp[subset^subsets[subset][i]]);
		}
	}
	return dp[(1<<n)-1];
}

int main() {
	freopen("gcj.in","r",stdin);
	freopen("gcj.out","w",stdout);
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(7);

	int N;
	cin>>N;
	for (int i=1; i<=N; ++i) {
		cout<<"Case #"<<i<<": "<<solve()<<endl;
	}
	return 0;
}
