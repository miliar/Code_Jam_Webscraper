#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

int r[1005];
int srt[1005], toSrt[1005];
double ansX[1005], ansY[1005];
int n, xSize, ySize;

bool cmp (int d1, int d2) {
	return r[d1] < r[d2];
}

void solve () {
	int i;

	scanf("%d%d%d", &n, &xSize, &ySize);

	for (i = 0;i < n;i++) {
		scanf("%d", &r[i]);
		srt[i] = i;
	}

	sort(srt, srt + n, cmp);
	for (i = 0;i < n;i++)
		toSrt[i] = srt[i];
	sort(r, r + n);

	int xCur = 0;
	int yCur = 0;

	bool xShifted = false;

	for (i = 0;i < n;) {
		while (i < n) {
			if (xShifted) {
				ansX[toSrt[i]] = xCur + r[i]; ansY[toSrt[i]] = yCur;
			}else
			{
				ansX[toSrt[i]] = xCur; ansY[toSrt[i]] = yCur;
			}
			
			if (i == n - 1) {
				i++;
				break;
			}

			yCur += r[i] + r[i + 1];

			i++;

			if (yCur > ySize)
				break;
		}

		if (i == n)
			break;

		yCur = 0;
		if (!xShifted)
			xCur += r[i - 1];
		else
			xCur += 2 * r[i - 1];

		xShifted = true;
	}

	for (i = 0;i < n;i++) {
		if (ansX[i] > xSize || ansY[i] > ySize)
			break;
	}

	if (i == n) {
		printf("%lf %lf", ansX[0], ansY[0]);
		for (i = 1;i < n;i++) {
			printf(" %lf %lf", ansX[i], ansY[i]);
		}
		return ;
	}

	xCur = 0;
	yCur = 0;

	xShifted = false;

	for (i = 0;i < n;) {
		while (i < n) {
			if (xShifted) {
				ansX[toSrt[i]] = xCur + r[i]; ansY[toSrt[i]] = yCur;
			}else
			{
				ansX[toSrt[i]] = xCur; ansY[toSrt[i]] = yCur;
			}

			if (i == n - 1) {
				i++;
				break;
			}

			yCur += r[i] + r[i + 1];

			i++;

			if (yCur > xSize)
				break;
		}

		if (i == n)
			break;

		yCur = 0;
		if (!xShifted)
			xCur += r[i - 1];
		else
			xCur += 2 * r[i - 1];

		xShifted = true;
	}

	printf("%lf %lf", ansY[0], ansX[0]);
	for (i = 1;i < n;i++) {
		printf(" %lf %lf", ansY[i], ansX[i]);
	}
}

int main () {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test, t;

	scanf("%d\n", &test);
	for (t = 0;t < test;t++) {
		if (t)
			printf("\n");
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}