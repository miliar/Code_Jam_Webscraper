#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <stack>
#include <set>
#include <list>
#include <sstream>
#include <map>
#include <limits>

using namespace std;

int main() {
	int T;
	cin>>T;
	for(int t=1; t<=T; t++) {
		int N, D;
		cin>>N;
		pair< pair<int, int>, int > p;
		vector< pair< pair<int, int>, int > > v;
		vector<int> dp;
		for(int i=0; i<N; i++) {
			cin>>p.first.first>>p.first.second;
			p.second = i;
			v.push_back(p);
			dp.push_back(-1);
		}
		cin>>D;
		dp[0] = min(v[0].first.first, v[0].first.second);
		for(int i=1; i<N; i++) {
			for(int j=0; j<i; j++) {
				if(dp[j] == -1) continue;
				if(v[i].first.first - v[j].first.first > dp[j]) continue;
				dp[i] = max(dp[i], min(v[i].first.first - v[j].first.first, v[i].first.second));
			}
		}
		bool possible = false;
		for(int i=0; i<N; i++) {
			if(dp[i] == -1) continue;
			if(dp[i] + v[i].first.first >= D) possible = true;
		}
		if(possible) cout<<"Case #"<<t<<": YES\n";
		else cout<<"Case #"<<t<<": NO\n";
	}
	return 0;
}