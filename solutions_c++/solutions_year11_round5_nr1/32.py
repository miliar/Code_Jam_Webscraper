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
		printf("Case #%d: \n",test);
		
		int W,L,U,G;
		vector<double> xL, xU, yL, yU;
		vector< pair<int, pair<int, int> > > events;
		scanf("%d%d%d%d",&W,&L,&U,&G);

		double areaTot=0;

		for (int i = 0; i < L; i++) {
			double x, y;
			scanf("%lf%lf",&x,&y);
			xL.push_back(x); yL.push_back(y);
			if (i != 0) areaTot -= (xL[i]-xL[i-1])*(yL[i]+yL[i-1])/2;
			events.push_back(make_pair(xL[i],make_pair(0,i)));
		}
		for (int i = 0; i < U; i++) {
			double x, y;
			scanf("%lf%lf",&x,&y);
			xU.push_back(x); yU.push_back(y);
			if (i != 0) areaTot += (xU[i]-xU[i-1])*(yU[i]+yU[i-1])/2;
			events.push_back(make_pair(xU[i],make_pair(1,i)));
		}
		
		sort(events.begin(),events.end());
		// first two are the zero line
		int piecesMade = 0;
		double area = 0;
		int curU = 0, curL = 0;
		int lastEvent=0;
		for (int i = 2; i < events.size(); i++) {
			int evType = events[i].second.first;
			int evID = events[i].second.second;
			int evX = evType==0?xL[evID]:xU[evID];
			double gradU, gradL;
			gradL = ((double) (yL[curL+1] - yL[curL])) / ((double) (xL[curL+1] - xL[curL]));
			gradU = ((double) (yU[curU+1] - yU[curU])) / ((double) (xU[curU+1] - xU[curU]));

			double newarea = area;
			newarea -= (yL[curL]+gradL*(((double)(lastEvent+evX))*0.5 - xL[curL]))*((double)(evX-lastEvent));
			newarea += (yU[curU]+gradU*(((double)(lastEvent+evX))*0.5 - xU[curU]))*((double)(evX-lastEvent));
			// make some cuts
			while (piecesMade < G-1 && newarea > ((double)piecesMade+1)/((double)G)*areaTot) {
				double targ = ((double)piecesMade+1)/((double)G)*areaTot - area;
				double delta=-lastEvent;
				double b = ((double) yU[curU] - yL[curL] + gradU*(lastEvent-xU[curU]) - gradL*(lastEvent-xL[curL]));
				if (gradU == gradL) {
					delta = targ / b;
				} else {
					double a = (gradU-gradL)/2;
					double c = -targ;
					delta = (-b + sqrt(b*b-4*a*c))/(2*a);
				}
				printf("%.8f\n",lastEvent + delta);
				piecesMade++;
			}
			
			area = newarea;

			// update gradient
			if (evType == 0) {
				curL = evID;
				lastEvent = xL[evID];
			} else {
				curU = evID;
				lastEvent = xU[evID];
			}
			if (lastEvent == W || piecesMade == G) break;
		}

		
	}
}
