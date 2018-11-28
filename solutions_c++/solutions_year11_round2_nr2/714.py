#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

const double g = 1e-8;
const int MAX = 1000008;

double pos[MAX], d;
int acc;

int check(double r) {
	double pre = pos[0] - r, tmp;
	int i;
	for (i = 1; i < acc; ++i) {
		if (pos[i] + r < pre + d)
		   return 0;
		if (pre < pos[i])
		   tmp = max(pre + d, pos[i] - r);
		else 
		   tmp = pre + d;
		   
       pre = tmp;
				
		
	}
	return 1;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int i, j, n, icas, cas;
	int c, v;
	double p, a, b, mid;
	scanf("%d", &cas);
	for (icas = 1; icas <= cas; ++icas) {
		scanf("%d%lf", &c, &d);
		acc = 0;
		for (i = 0; i < c; ++i) {
			scanf("%lf%d", &p, &v);
			for (j = 0; j < v; ++j)
				pos[acc++] = p;
		}
		sort(pos, pos + acc);
	//	for (i = 0; i < acc; ++i)
	//		printf("%.0lf ", pos[i]);
			
		a = 0.0; b = 200000000.0;
		while (a + g < b) {
            mid = (a + b) / 2;
            if (check(mid))
			   b = mid;  
		    else
		       a = mid;
       }
	//	printf("\n");
		printf("Case #%d: %.8lf\n", icas, a);
	}
	
//	system("pause");
}