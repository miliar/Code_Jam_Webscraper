#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);

		int N;
		scanf("%d",&N);
		if (N == 0) {
			printf("Case #%d: 0\n",test);
			continue;
		}
		vector<int> freq = vector<int>(10010,0);
	
		for (int i = 0; i < N; i++) {
			int tmp;
			scanf("%d",&tmp);
			freq[tmp]++;
		}

		vector<int> rises;
		vector<int> falls;
		for (int i = 1; i <= 10001; i++) {
			if (freq[i] > freq[i-1])
			for (int j = 0; freq[i-1]+j < freq[i]; j++) rises.push_back(i);
			for (int j = 0; freq[i]+j < freq[i-1]; j++) falls.push_back(i);
		}

		int ans = 999999;
		for (int i = 0; i < rises.size(); i++) {
			ans = min(ans,falls[i]-rises[i]);
		}
		
		
		printf("Case #%d: %d\n",test,ans);
	}
}
