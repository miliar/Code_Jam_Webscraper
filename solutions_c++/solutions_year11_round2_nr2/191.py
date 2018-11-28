#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int C,D;
int vendors[300];
int v_temp[300];
int position[300];

bool ok(double tempo) {
	for (int i = 0; i < C; i++) v_temp[i] = vendors[i];
	
	v_temp[0]--; // define the first
	
	double point = position[0]-tempo;
	double best;
	
	for (int k = 0; k < C; k++) {
		while (v_temp[k]) {
			v_temp[k]--;
			// move this guy
			best = point + D;
			if (position[k] + tempo < best) {
				// can't go enough
				return false;
			} else if (position[k] < best) {
				point = best;
			} else if (position[k] - tempo < best) {
				point = best;
			} else {
				point = position[k] - tempo;
			}
		}
	}
	return true;
}

double process() {
	scanf("%d %d", &C, &D);
	
	for (int i = 0; i < C; i++) {
		scanf("%d%d", &position[i], &vendors[i]);
	}
	double ini = 0;
	double fim = 1000000000001LL;
	double meio;
	
	for (int i = 0; i < 100; i++) {
		meio = (ini+fim)/2;
		if (ok(meio)) fim = meio;
		else ini = meio;
	}
	
	return ini;
}

int main() {
	
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: %.10lf\n", i+1, process());
	}
	
	return 0;
}
