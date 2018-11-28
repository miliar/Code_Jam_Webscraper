#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;

	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		int X, s1, s2, _maxt, N;

		scanf("%d %d %d %d %d", &X, &s1, &s2, &_maxt, &N);

		vector <pair <pair <int, int>, int> > rws;

		for (int i = 0; i < N; i++) {
			int st, end, sp;
			scanf("%d %d %d", &st, &end, &sp);
			rws.push_back(make_pair(make_pair(st, end), sp));
		}

		sort(rws.begin(), rws.end());

		vector <pair <double, double> > segs;

		int last = 0;
		for (int i = 0; i < N; i++) {
			int st = rws[i].first.first, end = rws[i].first.second;
			int sp = rws[i].second;
			if (st > last) {
				segs.push_back(make_pair(1.0*s1, 1.0*st-last));
			}
			segs.push_back(make_pair(1.0*s1+sp, end-st));
			last = end;
		}
		if (X > last)
			segs.push_back(make_pair(1.0*s1, X-last));
		
		sort(segs.begin(), segs.end());

		double ret = 0.0;
		double maxt = _maxt;
		double up = s2-s1;

		for (int i = 0; i < (int)segs.size(); i++) {
			double v = segs[i].first, dist = segs[i].second;

			double runt = min(maxt, dist/(v+up));
			double dist1 = runt * (v+up), dist2 = dist - dist1;

			maxt -= runt;

			ret += runt + dist2/v;
		}

		printf("Case #%d: %.7f\n", t+1, ret);
	}

	return 0;
}
