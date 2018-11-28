#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>

#define INF 100000000
#define MAX 1048576
#define nc (((qc % 2) == 0) ? 1 : 2)

using namespace std;

int a, l, walk, run, rt, n;
int belts[1005][3], best[1000005];
int speeds[1000005];

int main() {
    scanf("%d", &a);
    
    for (int i=0; i<a; i++) {
	scanf("%d%d%d%d%d", &l, &walk, &run, &rt, &n);
	
	double time = 0., nrt = rt;
	
	for (int j=0; j<l; ++j)
	    speeds[j] = walk;
	
	for (int j=0; j<n; j++) {
	    scanf("%d%d%d", &belts[j][0], &belts[j][1], &belts[j][2]);
	    
	    for (int k=belts[j][0]; k < belts[j][1]; ++k) {
		speeds[k] += belts[j][2];
	    }
	}
	sort(speeds, speeds + l);
	for (int j=0; j<l; ++j) {
	    
	    double dist = min((speeds[j] + run - walk) * nrt, 1.0);
	    time += (dist / (speeds[j] + run - walk)) + ((1 - dist) / speeds[j]);
	    nrt -= (dist / (speeds[j] + run - walk));
	}
	printf("Case #%d: %lf\n", i+1, time);
    }
    
   
    return 0;
}