#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define Inf 99999999


#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

#define Eps 1e-7

double dx[18] = {0, 0, 1, 0, 0, -1, -1, -1, -1, -1, 1, 1, 1, 1, 0, 0, 0, 0};//         -1,1,1,1,-1,-1};
double dy[18] = {0, 1, 0, 0, -1, 0, 1, -1, 0, 0, 1, -1, 0, 0, 1, -1, 1, -1};
double dz[18] = {1, 0, 0, -1, 0, 0, 0, 0, 1, -1, 0, 0, 1, -1, 1, -1, -1, 1};


struct NODE {
	double x, y, z;
	double p;
}node[2000];

int main() {

	freopen("C-large.in","r",stdin);
	freopen("C-large.out1","w",stdout);

	int C;
	int p;
	double ans;
	double x, y, z;
	double tx, ty, tz;
	double ansx,ansy,ansz;
	int ansi;
	int i,j;

	while (scanf("%d", &C) != EOF) {

		for (p = 1; p <= C; p ++) {

			int n;
			ans = Inf;

			scanf("%d", &n);

			x = y = z = 0;

			for (i = 0; i < n; i ++) {
				scanf("%lf%lf%lf%lf", &node[i].x, &node[i].y, &node[i].z, &node[i].p);
				x += node[i].x;
				y += node[i].y;
				z += node[i].z;
			}
			double r = 2000000;
			tx = x / n;
			ty = y / n;
			tz = z / n;
			while (true) {

				bool isM = false;

				for (i = 0; i < 18; i ++) {
					x = tx + dx[i] * r;
					y = ty + dy[i] * r;
					z = tz + dz[i] * r;

					double tans = -Inf;

					for (j = 0; j < n; j ++) {

						double tc = (fabs(x - node[j].x) + fabs(y - node[j].y) +
						             fabs(z - node[j].z)) / node[j].p;

						if (tc > tans) 
						{
							tans = tc;
						//	ansi = j;
						}

					}
					if (tans < ans) {
						ans = tans;
						isM = true;
						ansx = x;
						ansy = y;
						ansz = z;
					}
				}
				tx = ansx;
				ty = ansy;
				tz = ansz;
				if (!isM) {
					r = r / 2;
				}
				if (r < Eps) {
					break;
				}
			}
			printf("Case #%d: %lf\n", p, ans);
		}

	}
	return 0;
}
