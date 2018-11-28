
#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int r[1000000];

int main(){
	
	int t; scanf("%d", &t);
	int X, S, R, T, N;
	int a, b, w;
	double left, pass;
	
	for(int x=1; x<=t; ++x){
		scanf("%d %d %d %d %d", &X, &S, &R, &T, &N);
		for(int i=0; i<X; ++i){
			r[i] = S;
		}
		for(int i=0; i<N; ++i){
			scanf("%d %d %d", &a, &b, &w);
			for(int j=a; j<b; ++j){
				r[j] += w;
			}
		}
		sort(r, r+X);
		R -= S;
		left = T;
		pass = 0;
		for(int i=0; i<X; ++i){
			if(left < 0.00000001){
				pass += 1.0/r[i];
			}else{
				if(1.0/(r[i]+R) <= left){
					left -= 1.0/(r[i]+R);
					pass += 1.0/(r[i]+R);
				}else{
					pass += left + (1.0-left*(r[i]+R))/r[i];
					left = 0;
				}
			}
		}
		printf("Case #%d: %.7lf\n", x, pass);
	}
	return 0;
}
