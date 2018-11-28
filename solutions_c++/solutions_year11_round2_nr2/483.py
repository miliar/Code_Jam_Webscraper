#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAXN = 200+5;
const double EPS = 1e-7;

int n, d;
int P[MAXN], V[MAXN];

bool f(double res) {

	
	double start = P[0]-res;
	double end = start+(V[0]-1)*d;

	bool ok = true;

	if(fabs(end-P[0]) > res+EPS) ok =  false;

	for(int i = 1; i < n; i++) {
		start = max(P[i]-res, end+d);
		if(fabs(start-P[i]) > res+EPS) ok =  false;

		end = start+(V[i]-1)*d;		
		if(fabs(end-P[i]) > res+EPS) ok =  false;
	}


	return ok;
}

void solve(int caseNumber) {
	scanf("%d %d", &n, &d);
	for(int i = 0; i < n; i++) scanf("%d %d", &P[i], &V[i]);



	double L = 0;
	double R = 1e20;

	while(R-L > 1e-8) {
		double mid = (R+L)/2;
		if(f(mid)) R = mid;
		else L = mid;
	}

	printf("Case #%d: %.10lf\n", caseNumber, (R+L)/2);

}


int main() {
	//freopen("B-small-attempt0.in", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);
}