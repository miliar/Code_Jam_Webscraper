#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int D, C;
vector<int> P, V;
const int MAXITER = 100;
const double eps = 1e-8;

bool eq(double x, double y){
	return abs(x - y) <= eps;
}
bool check(double x){
	double l, r, l1;
	vector<int> p(P), v(V);
	l = p[0] - x;
	--v[0];
	for (int i = 0; i < p.size(); ++i){
		for (int j = 0; j < v[i]; ++j){
			double t = abs(l - p[i] + D);
			if (t > x){
				if (l + D > p[i]) l1 = p[i] + x; else l1 = p[i] - x;
				if (abs(l - l1) < D) return false; else l = l1;
			} else {
				l += D;
			}
		}
	}
	return true;
}
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		P.clear(); V.clear();
		scanf("%d%d", &C, &D);
		for (int i = 0; i < C; ++i){
			int p, v;
			scanf("%d%d", &p, &v);
			P.push_back(p);
			V.push_back(v);
		}
		double l = 0, r = 1e15, mid;
	//	l = r = 1;
		for (int i = 0; i < MAXITER; ++i){
			mid = (l + r) / 2;
			if (check(mid)){
				r = mid;
			} else {
				l = mid;
			}
		}
		printf("Case #%d: %.9lf\n", tt + 1, mid);
	}
	return 0;
}