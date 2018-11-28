#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i,a,b) for(int i=(a); i<(b); ++i)

int main() {
	int T;
	scanf("%d", &T);
	rep(t,0,T) {
		int N;
		scanf("%d", &N);
		vector<int> nums;
		rep(n,0,N) {
			int E;
			scanf("%d", &E);
			nums.push_back(E);
		}
		vector<int> sorted(nums);
		sort(sorted.begin(), sorted.end());
		int count = 0;
		rep(i,0,N)
			if(nums[i]!=sorted[i]) count++;
		printf("Case #%d: %d.000000\n", t+1, count);
	}
	return 0;
}