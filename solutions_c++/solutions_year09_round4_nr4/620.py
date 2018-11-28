#include <cmath>
#include <cstdio>
#include <cstring>

#include <map>
#include <queue>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

#define ALL(x) (x).begin(),(x).end()
#define FOR(_i,n) for(int _i = 0; _i < (n); _i++)
#define FORI(_i,n) for(int _i = (n)-1; _i >= 0; _i--)
#define FORA(_i,a,n) for(int _i = (a); _i < (n); _i++)
#define FORAI(_i,a,n) for(int _i = (n)-1; _i >= (a); _i--)
#define FOREACH(_it,x) for(typeof((x).begin()) it = (x).begin(); _it != (x).end(); _it++)
#define DIST(a,b) sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

using namespace std;

double plants[40][3];
int C, N;

int main() {
	scanf("%d\n", &C);
	
	FOR(ci, C) {
		scanf("%d\n", &N);
		
		FOR(i, N) {
			scanf("%lf %lf %lf\n", &plants[i][0], &plants[i][1], &plants[i][2]);
		}
		
		double best = 1e9, tmp;
		if(N < 3) {
			best = 0;
			FOR(i, N) if(best < plants[i][2]) best = plants[i][2];
		} else if(N == 3) {
			tmp = max(plants[0][2], (DIST(plants[1], plants[2]) + plants[1][2] + plants[2][2]) / 2.0);
			if(best > tmp) best = tmp;
			
			tmp = max(plants[1][2], (DIST(plants[0], plants[2]) + plants[0][2] + plants[2][2]) / 2.0);
			if(best > tmp) best = tmp;
			
			tmp = max(plants[2][2], (DIST(plants[0], plants[1]) + plants[0][2] + plants[1][2]) / 2.0);
			if(best > tmp) best = tmp;
		}
		
		printf("Case #%d: %f\n", ci+1, best);
	}
	
	return 0;
}
