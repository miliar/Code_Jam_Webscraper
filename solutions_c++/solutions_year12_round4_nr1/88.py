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

		int N, D;
		bool succ=0;
		vector<pair<int,int> > vines;
		vector<int> furthest_start;
		scanf("%d",&N);
		for (int i = 0; i < N; i++) {
			int d_i, l_i;
			scanf("%d%d",&d_i,&l_i);
			vines.push_back(make_pair(d_i,l_i));
			furthest_start.push_back(d_i);
		}
		scanf("%d",&D);

		furthest_start[0] = 0;
		for (int i = 0; i < N; i++) {
			furthest_start[i] = max(furthest_start[i], vines[i].first - vines[i].second);
			int new_end = vines[i].first * 2 - furthest_start[i];
			for (int j = i+1; j < N; j++) {
				if (vines[j].first <= new_end) {
					furthest_start[j] = min(furthest_start[j],vines[i].first);
				}
			}
			if (new_end >= D) succ=1;
		}

		
		
		printf("Case #%d: %s\n",test, succ?"YES":"NO");
	}
}
