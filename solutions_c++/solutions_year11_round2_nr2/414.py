#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

struct pos_t {
	int p, v;

	bool operator<(const pos_t &pos) const
	{
		return p < pos.p;
	}
} pos[250];

struct cluster_t {
	double time;
	double left, right;
} cluster[250];

int main()
{
	int t, c, d, i;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		scanf("%d%d", &c, &d);
		for (i = 0; i < c; i++) scanf("%d%d", &pos[i].p, &pos[i].v);
		sort(pos, pos + c);
		double time = 0;
		for (i = 0; i < c; i++) {
			//printf("%d %d\n", pos[i].p, pos[i].v);
			cluster[i].time = (double) (pos[i].v - 1) / 2 * d;
			cluster[i].left = pos[i].p - cluster[i].time;
			cluster[i].right = pos[i].p + cluster[i].time;
			time = max(time, cluster[i].time);
			//printf("cluster %d: %f %f %f\n", i, cluster[i].left, cluster[i].right, cluster[i].time);
		}
		int cc = c;
		bool change;
		do {
			change = false;
			for (i = 1; i < cc; i++) {
				double dist = cluster[i - 1].right - cluster[i].left + d;
				if (dist > 0) {
					double timediff = cluster[i - 1].time - cluster[i].time;
					double movea = dist / 2 - timediff / 2;
					if (movea < 0) movea = 0;
					if (movea > dist) movea = dist; 
					double moveb = dist - movea;
					//printf("%f %f %f\n", dist, movea, moveb);
					cluster[i - 1].left -= movea;
					cluster[i - 1].right = cluster[i].right + moveb;
					cluster[i - 1].time = max(cluster[i - 1].time + movea, cluster[i].time + moveb);
					//printf("cluster %d: %f %f %f\n", i - 1, cluster[i - 1].left, cluster[i - 1].right, cluster[i - 1].time);
					time = max(time, cluster[i - 1].time);
					for (int j = i; j < cc - 1; j++) {
						memcpy(&cluster[j], &cluster[j + 1], sizeof(cluster_t));
					}
					cc--;
					change = true;
				}
			}
		} while (change);
		//for (i = 0; i < cc; i++) printf("%d %d: %d %f\n", cluster[i].first, cluster[i].last, cluster[i].cnt, cluster[i].middle);
		/*int j = 0, cnt = 0;
		for (i = 0; i < c; i++) {
			if (cluster[j].last < i) {
				j++;
				cnt = 0;
			}
			printf("%d: %d at %d %f\n", pos[i].p, pos[i].v, cluster[j].cnt, cluster[j].middle);
			double pos1 = cluster[j].middle - ((double) (cluster[j].cnt - 1) / 2 - cnt) * dist;
			double pos2 = cluster[j].middle - ((double) (cluster[j].cnt - 1) / 2 - cnt - (pos[i].v - 1)) * dist;
			printf("%f %f\n", pos1, pos2);
			time = max(time, fabs(pos[i].p - pos1));
			time = max(time, fabs(pos[i].p - pos2));
		}*/
		printf("Case #%d: %f\n", cas, time);
	}
	return 0;
}
