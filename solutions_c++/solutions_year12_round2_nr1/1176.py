#include <cstdlib>
#include <cstdio>

#define MAXN 300
const double EPS = 1e-10;

int n, total;
int val[MAXN];
double ans[MAXN];

// Da ?
bool tt(int i, int j, double r, double obj) {
	if(r < 0.0) return false;
	if(i == j) return tt(i + 1, j, r, obj);
	if(i == n) return true;
	
	double y = (obj - val[i]);
	if(y <= 0.0) return tt(i + 1, j, r, obj);
	double f = y / total + EPS;
	return tt(i + 1, j, r - f, obj);
}

bool test(int ind, double x) {
	double resto = 1.0;
	double v = val[ind] + (total * x);
	return !tt(0, ind, resto - x, v);
}

int main() {
	int t, caso = 0;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) scanf("%d", &val[i]);

		total = 0;
		for(int i = 0; i < n; ++i) total += val[i];
		
		for(int i = 0; i < n; ++i) {
			if(test(i, 0.0)) { ans[i] = 0.0; continue; }
			double ini = 0.0, fim = 1.0, meio;
			for(int k = 0; k < 120; ++k) {
				meio = (ini + fim) / 2.0;
				if(test(i, meio)) fim = meio;
				else ini = meio;
			}
			
			ans[i] = (ini + fim) / 2.0;
		}
		
		printf("Case #%d:", ++caso);
		for(int i = 0; i < n; ++i)
			printf(" %.7lf", ans[i] * 100);
		printf("\n");
	}
	
	
	return 0;
}

