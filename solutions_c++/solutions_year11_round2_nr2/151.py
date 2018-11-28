#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 1; c <= numCases; c++) {
		int numPoints;
		double distance;
		scanf("%d%lf", &numPoints, &distance);

		vector<double> locs;
		for (int i = 0; i < numPoints; i++) {
			int loc, cnt;
			scanf("%d%d", &loc, &cnt);
			for (int j = 0; j < cnt; j++) {
				locs.push_back(loc);
			}
		}
		sort(locs.begin(), locs.end());
		int sz = locs.size();
		// FIXME: sz = 1!!!
		if (sz == 1) {
			printf("Case #%d: %12.12lf\n", c, 0.);
			continue;
		}

		double l = 0., r = 1000000000000000.;
		int cnt = 0;
		while (l <= r && cnt < 200) {
			cnt++;
			double m = (l + r) / 2.;
			bool poss = true;
			double cur = locs[0] - m;
			int i;
			for (i = 1; i < sz - 1; i++) {
				double dist = locs[i] - cur;
				double newcur;
				if (dist < distance) {
					dist = locs[i] + m - cur;
					if (dist < distance) {
						poss = false;
						break;
					}
					double mini = min(m, distance - (locs[i] - cur));
					newcur = locs[i] + mini;
				} else {
					newcur = locs[i] - m;
					dist = newcur - cur;
					if (dist < distance) {
						newcur = cur + distance;
					}
				}
				cur = newcur;
			}
			double dist = locs[sz - 1] - cur + m;
			if (dist < distance) {
				poss = false;
			}
//			printf("m = %3.3lf -> %s\n", m, poss ? "YES" : "!");
			if (poss) {
				r = m;
			} else {
				l = m;
			}
		}
		printf("Case #%d: %12.12lf\n", c, l);
	}

	return 0;
}
