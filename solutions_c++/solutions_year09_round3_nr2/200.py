#include <stdio.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <string>

using namespace std;

double sum[3];
double vel[3];
double square (double arg) {
	return arg * arg;
}

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 0; c < numCases; c++) {
		for (int i = 0; i < 3; i++) {
			sum[i] = vel[i] = 0;
		}
		int numFlies;
		scanf("%d", &numFlies);
		for (int i = 0; i < numFlies; i++) {
			for (int j = 0; j < 3; j++) {
				double tmp;
				scanf("%lf", &tmp);
				sum[j] += tmp;
			}
			for (int j = 0; j < 3; j++) {
				double tmp;
				scanf("%lf", &tmp);
				vel[j] += tmp;
			}
		}

		double zaehler = 0;
		for (int j = 0; j < 3; j++) {
			zaehler += (sum[j] * vel[j]);
		}
		double nenner = 0;
		// FIXME nennner bleibt 0?
		for (int j = 0; j < 3; j++) {
			nenner += (vel[j] * vel[j]);
		}

		double minTime = 0;
		if (nenner != 0.0) {
			minTime = zaehler / nenner;
		}
		minTime = -minTime;
		if (minTime <= 0.0) {
			minTime = 0.0;
		}

		double dist = sqrt(square(sum[0] + vel[0] * minTime) / (numFlies * numFlies) +
				square(sum[1] + vel[1] * minTime) / (numFlies * numFlies) +
				square(sum[2] + vel[2] * minTime) / (numFlies * numFlies));

		printf("Case #%d: %12.12lf %12.12lf\n", c + 1, dist, minTime);
	}

	return 0;
}
