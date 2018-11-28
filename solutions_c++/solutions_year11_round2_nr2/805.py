#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

struct point {
	int pos;
	int count;
	bool operator<(const point& rhs) const {
		return pos < rhs.pos;
	}
};
point points[1000100];
bool f(double time, int C, int D)
{
	double least = (double)points[0].pos - time;
	double curpos = least - (double) D;
	for (int i=0; i<C; ++i) {
		for (int j=0; j<points[i].count; ++j) {
			double target = curpos + (double)D;
			if (target < (double)points[i].pos) {
				if ((double)points[i].pos - target <= time) {
					curpos += (double)D;
				}
				else {
					double reachablepos = (double)points[i].pos - time; 
					if (fabs(reachablepos - curpos) >= (double)D) {
						curpos = reachablepos;
					}
					else {
						return false;
					}
				}
			}
			else {
				if (target - (double)points[i].pos <= time) {
					curpos += (double)D;
				}
				else {
					double reachablepos = (double)points[i].pos + time;
					if (fabs(reachablepos - curpos) >= (double)D) {
						curpos = reachablepos;
					}
					else {
						return false;
					}
				}
			}
		}
	}
	return true;
}
int main()
{
	int T;
	scanf("%d",&T);
	for (int test=1; test<=T; ++test)  {
		int C, D;
		scanf("%d%d",&C,&D);
		for (int i=0; i<C; ++i) {
			scanf("%d%d",&points[i].pos,&points[i].count);
		}
		sort(points, points+C);
		double lo = 0.0;
		double hi = 1e9;
		while (fabs(lo-hi) > 1e-9) {
			double mid = (lo+hi)/2;
			if (f(mid,C,D)) {
				hi = mid;
			}
			else {
				lo = mid;
			}
		}
		printf("Case #%d: %0.7f\n", test, lo);
	}

	return 0;
}