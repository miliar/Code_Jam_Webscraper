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

		vector<int> input;
		vector<int> counts;
		vector<int> output, slope;
		int N; scanf("%d",&N);

		counts = vector<int>(N);
		for (int i = 0; i < N-1; i++) {
			int x; scanf("%d",&x);
			input.push_back(x-1);
			counts[x-1]++;
		}
		bool failcheck=0;
		for (int i = 0; i < N-1; i++) {
		for (int j = i+1; j < N-1; j++) {
			if (input[j] > input[i] && input[i] > j) failcheck = 1;
		}
		}
		if (failcheck) {
			printf("Case #%d: Impossible\n",test);
			continue;
		}
		output = vector<int>(N);
		slope = vector<int>(N);
		int minseen = 0;

		for (int i = N-2; i >= 0; i--) {
			counts[input[i]]--;
			slope[i] = slope[input[i]] + counts[input[i]];
			output[i] = output[input[i]] - slope[i]*(input[i]-i);

			if (output[i] < minseen) minseen = output[i];
		}

		
		
		printf("Case #%d:",test);
		for (int i = 0; i < N; i++) printf(" %d",output[i]-minseen);
		printf("\n");
	}
}
