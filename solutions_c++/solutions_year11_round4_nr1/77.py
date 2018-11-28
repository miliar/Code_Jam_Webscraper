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
		
		int X, speedWalk, speedRun, timeRun, N;
		scanf("%d%d%d%d%d",&X,&speedWalk,&speedRun,&timeRun,&N);
		vector<pair<int, int> > segments;
		int normalLength=X;
		for (int i = 0; i < N; i++) {
			int B, E, w;
			scanf("%d%d%d",&B,&E,&w);
			normalLength -= E-B;
			segments.push_back(make_pair(w,E-B));
		}
		segments.push_back(make_pair(0,normalLength));
		
		double runLeft = timeRun;
		double timeTaken = 0;
		sort(segments.begin(),segments.end());
		for (int i = 0; i < segments.size(); i++) {
			double projRunTime = ((double)segments[i].second)/((double)(segments[i].first+speedRun));
			if (projRunTime > runLeft) {
				double projRunDist = ((double)(segments[i].first+speedRun))*runLeft;
				double projWalkTime = (((double)segments[i].second)-projRunDist)/((double)(segments[i].first+speedWalk));
				timeTaken += runLeft + projWalkTime;
				runLeft = 0;
			} else {
				runLeft -= projRunTime;
				timeTaken += projRunTime;
			}
		}
		
		printf("Case #%d: %.9f\n",test,timeTaken);
	}
}
