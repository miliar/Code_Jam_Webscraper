#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <list>

#define MAX 64
#define MAXA 1000000000

using namespace std;

int n;
double data[MAX][3], ans;

void reset_data() {
}

void find_ans() {
	int i, j, k;
	double tmp;

	reset_data();

	scanf("%d", &n);
	for(i = 0; i < n; i++)
		scanf("%lf %lf %lf", &data[i][0], &data[i][1], &data[i][2]);

	if(n == 1) {
		printf("%lf", data[0][2]);
	} else if(n == 2) {
		printf("%lf", max(data[0][2], data[1][2]));
	} else {
		ans = MAXA;
		for(i = 0; i < n; i++) {
			for(j = 0; j < n; j++) {
				if(i == j)continue;
				tmp = (data[i][2] + data[j][2] + sqrt((data[i][0] - data[j][0]) * (data[i][0] - data[j][0]) + (data[i][1] - data[j][1]) * (data[i][1] - data[j][1]))) / 2;
				for(k = 0; k < n; k++) {
					if(i == k || j == k)continue;
					ans = min(ans, max(tmp, data[k][2]));
				}
			}
		}
		printf("%lf", ans);
	}
}

int main(int argc, char *argv[])
{
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
