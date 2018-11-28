#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

pair<int, int> PV[210];
int dd[420];
ll ww[420];
ll ee[420];
ll ff[420];

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int C, Din;
		scanf("%d %d", &C, &Din);
		ll D = Din;
		for (int j = 0; j < C; j++)
			scanf("%d %d", &PV[j].first, &PV[j].second);
		//sort(PV, PV+C);
		int n = 0;
		for (int j = 0; j < C; j++)
			n += PV[j].second;
		int INF = 1 << 29;
		int l = 1;
		dd[0] = INF;
		ww[0] = 0;
		if (PV[0].second >= 2) {
			dd[l] = 0;
			ww[l] = (PV[0].second - 1)*D*2;
			l++;
		}
		for (int j = 1; j < C; j++) {
			dd[l] = (PV[j].first - PV[j-1].first)*2;
			ww[l] = D*2;
			l++;
			if (PV[j].second >= 2) {
				dd[l] = 0;
				ww[l] = (PV[j].second - 1)*D*2;
				l++;
			}
		}
		dd[l] = INF;
		ww[l] = 0;
		l++;
/*
		for (int j = 0; j < l; j++)
			printf("%d ", dd[j]);
		printf("\n");
		for (int j = 0; j < l; j++)
			printf("%lld ", ww[j]);
		printf("\n");
*/

		double ans = -1.0;
		for (int j = 0; j < 400100; j++) {
			ee[0] = dd[0];
			for (int k = 1; k < l; k++) {
				ee[k] = dd[k];
				if (ee[k-1] - ww[k-1] > 0) {
					ll x = min((ll)j, ee[k-1] - ww[k-1]);
					ee[k-1] = ee[k-1] - x;
					ee[k] = dd[k] + x;
				}
			}
			//for (int q = 0; q < l; q++)
			//printf("%lld ", ee[q]);
			//printf("\n");
			ff[l-1] = ee[l-1];
			for (int k = l-1; k >= 1; k--) {
				ff[k-1] = ee[k-1];
				if (ff[k] - ww[k] > 0) {
					ll x = min((ll)j, ff[k] - ww[k]);
					//printf("k=%d x=%lld\n", k, x);
					ff[k] = ff[k] - x;
					ff[k-1] = ee[k-1] + x;
				}
			}
			ff[0] = ee[0];
			//for (int q = 0; q < l; q++)
			//printf("%lld ", ff[q]);
			//printf("\n");
			for (int k = 1; k < l-1; k++) {
				if (ff[k] < ww[k])
					goto NEXT;
			}
			ans = j/2.0;
			break;
		NEXT:
			;
		}
		printf("Case #%d: %f\n", i+1, ans);
	}
}
