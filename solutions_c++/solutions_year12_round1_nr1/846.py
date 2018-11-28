#include <cstdio>
#include <algorithm>
#define maxa 100000

using namespace std;

double exp, p[maxa], P;
int a, b, t;

int main(){
	scanf("%d", &t);
	
	for (int j = 0; j < t; j++){
		scanf("%d%d", &a, &b);
		P = 1;
		for (int i = 0; i < a; i++)
			scanf("%lf", &p[i]), P *= p[i];
		
		exp = 1e10;
		
		exp = min(exp, P * (b - a + 1) + (1.0 - P) * (b - a + 1 + b + 1));
		
		for (int i = a - 1; i >= 0; i--){
			P /= p[i];
			exp = min(exp, P * (b - i + 1) + (1.0 - P) * (b - i + 1 + b + 1) + a - i);
		}
		
		exp = min(exp, 1.0 + b + 1);
		
		printf("Case #%d: %lf\n", j + 1, exp);
	}
}
