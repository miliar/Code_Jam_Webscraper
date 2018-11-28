#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

void solve(int tc){
	double x, s, r, t, n;
	scanf("%lf%lf%lf%lf%lf", &x, &s, &r, &t, &n);
	double sum = 0.0;
	double prev_e = 0;
	map<double, double> dist;
	for(double i = 0; i < n; i++){
		double bi, ei, wi;
		scanf("%lf%lf%lf", &bi, &ei, &wi);
		//fprintf(stderr, "Adding %f to sum.\n", (double)(bi - prev_e) / s);
		sum += (bi - prev_e) / s;
		dist[0] += bi - prev_e;
		//fprintf(stderr, "Adding %f to sum.\n", (double)(ei - bi) / (s + wi));
		sum += (ei - bi) / (s + wi);
		dist[wi] += ei - bi;
		prev_e = ei;
	}
	//fprintf(stderr, "Adding %f to sum.\n", (double)(x - prev_e) / s);
	sum += (x - prev_e) / s;
	dist[0] += x - prev_e;
	//fprintf(stderr, "Walking takes %f seconds.\n", sum);
	for(map<double, double>::iterator it = dist.begin(); t && it != dist.end(); ++it){
		//fprintf(stderr, "dist[%lf] = %lf\n", it->first, it->second);
		double dt = min(t, it->second / (it->first + r));
		t -= dt;
		double ddist = dt * (it->first + r);
		//fprintf(stderr, "dt = %f, ddist = %f\n", dt, ddist);
		//double old_sum = sum;
		//fprintf(stderr, "Removing %f from sum.\n", ddist / (s + it->first));
		//fprintf(stderr, "Adding %f to sum.\n", ddist / (r + it->first));
		sum -= ddist / (s + it->first);
		sum += ddist / (r + it->first);
		//fprintf(stderr, "Saved %f seconds.\n", old_sum - sum);
	}
	printf("Case #%d: %.16f\n", tc, sum);
	//fprintf(stderr, "=============\n");
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		solve(i+1);
	}
	return 0;
}
