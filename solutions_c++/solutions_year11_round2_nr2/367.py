#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cmath>
#define MAX 1000005

using namespace std;

typedef long long ll;

vector <long double> p;
long double tmp[MAX];
double D;

bool deu(long double dist){
//	printf ("%lf\n", dist);
	tmp[0] = (long double)p[0] - dist;
	for (int i = 1; i < (int)p.size(); i++){
		long double distl = p[i] - tmp[i-1];
		if (distl < D){
			if (distl + dist < D){
//				printf ("%lf\n", dist);
				return false;
			}
			tmp[i] = tmp[i-1] + D;
		}
		else{
			if (distl - dist > D)
				tmp[i] = p[i]-dist;
			else
				tmp[i] = tmp[i-1] + D;
		}
	}
	return true;
}

int main(){
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++){
		int C;
		scanf ("%d%lf", &C, &D);
		p.clear();
		for (int i = 0; i < C; i++){
			double x;
			int y;
			scanf ("%lf%d", &x, &y);
			for (int j = 0; j < y; j++)
				p.push_back(x);
		}
		sort(p.begin(), p.end());

		long double b, e;
		b = 0.0;
		e = (long double)((long double)p.size() * D) + 1000.0;
		while (fabs(b-e) > 1e-7){
			long double meio = (b+e)/2.0;
			if (deu(meio))
				e = meio;
			else
				b = meio;
		}
		printf ("Case #%d: ", t);
		printf ("%.6Lf\n", b);
	}
	return 0;
}
