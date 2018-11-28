#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int P, Q;
vector <int> released;
vector <int> markers;
map <pair<int,int>, int> memo;

int solve(int a, int b){
	if (b-a < 0) return 0;
	map <pair<int,int>, int>::iterator itr = memo.find(make_pair(a,b));
	if (itr != memo.end()) return itr->second;

	int sol = 0x3f3f3f3f;
	int t = 0;
	for (vector<int>::iterator itr = lower_bound(released.begin(), released.end(), a); itr < released.end() && (*itr) <= b; ++itr){
		sol = min(sol, solve(a, *itr-1)+solve(*itr+1, b)+(b-a));
		t = 0x3f3f3f3f;
	}

	sol = min(sol, t);

	memo[make_pair(a,b)] = sol;
	return sol;
}

int main(){
	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; ++tt){
		scanf("%d%d", &P, &Q);
		released.resize(Q);
		for (int i = 0; i < Q; ++i){
			scanf("%d", &released[i]);
		}
		memo.clear();
		printf("Case #%d: %d\n", tt, solve(1, P));
	}

	return 0;
}
