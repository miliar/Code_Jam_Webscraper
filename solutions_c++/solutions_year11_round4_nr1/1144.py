#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <math.h>
#include <stdlib.h>

using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define FOR(i,a,b) for (int i = (a); i < (b); i++)

struct s_walk {
	double start;
	double end;
	double speed;
};
typedef struct s_walk walk;

walk walks[15000];

int
compare(const void *p1, const void *p2)
{
	walk *w1 = (walk *) p1;
	walk *w2 = (walk *) p2;

	return (w1->speed - w2->speed);
}

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 1; c <= numCases; c++) {
		double len, speed, runSpeed, runTime;
		int numWalk;
		scanf("%lf%lf%lf%lf%d", &len, &speed, &runSpeed, &runTime, &numWalk);
		double totalLen = 0.0;
		FOR(i,0,numWalk) {
			scanf("%lf%lf%lf", &(walks[i].start), &(walks[i].end), &(walks[i].speed));
			totalLen += (walks[i].end - walks[i].start);
		}
		walks[numWalk].start = 0.;
		walks[numWalk].end = len - totalLen;
		walks[numWalk].speed = 0.;
		qsort(walks, numWalk + 1, sizeof(walk), compare);
		printf("Case #%d: ", c);
		double totalTime = 0.0;
		FOR(i,0,numWalk + 1) {
			double curLen = (walks[i].end - walks[i].start);
			double noWalkwayRunTime = curLen / (runSpeed + walks[i].speed);
			if (noWalkwayRunTime < runTime) {
				// may run all the time on no walkway
				runTime -= noWalkwayRunTime;
				totalTime += noWalkwayRunTime;
			} else {
				// may run part of the time on no walkway
				totalTime += runTime;
				double s = runTime * (runSpeed + walks[i].speed);
				s = (curLen) - s;
				double t = s/(speed + walks[i].speed);
				totalTime += t;
				runTime = 0.;
			}
		}

		printf("%12.12lf\n", totalTime);

		
	}

	return 0;
}
