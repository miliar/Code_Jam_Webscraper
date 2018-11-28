#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>

using namespace std;

int t, a, b;
double p[100001];

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		scanf("%d %d", &a, &b);
		double resp = b+2;
		double correto = 1.0;
		for(int i = 0; i < a; ++i){
			 scanf("%lf", p+i);
			 correto *= p[i];
		}
		double resp2 = 0;
		resp2 = (b-a+1);
		resp2 += (1.0-correto)*(b+1);
		resp = min(resp, resp2);
		for(int i = a-1; i >= 0; --i){
			correto /= p[i];
			resp2 = b-i+1 + (a-i);
			resp2 += (1.0-correto)*(b+1);
			resp = min(resp, resp2);
		}
		printf("Case #%d: %lf\n", _, resp);
	}
	return 0;
}
