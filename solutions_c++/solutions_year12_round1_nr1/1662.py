#include <utility>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
using namespace std;

int A, B, num;
double G[100005], P[100005];

double gao(){
	double p, t, minP = B + 2;
	for(int back = 0;back < A;back++){
		p = 0.0;
		for(int i = 0;i < num;i++){
			t = P[i];
			if(back >= i){
				p += (back * 2 + B - A + 1) * t;
			}
			else{
				p += (back * 2 + B - A + 1 + B + 1) * t;
			}
		}
		if(p < minP) minP = p;
	}
	return minP;
}

void init(){
	double p, t;
	num = 1;
	for(int i = 0;i < A;i++) num *= 2;
	for(int i = 0;i < num;i++){
		p = 1.0;
		for(int b = A - 1;b >= 0;b--){
			t = G[A - 1 - b];
			if(((num - 1 - i) >> b) & 1 == 1)  p *= t;
			else p *= 1 - t;
		}
		P[i] = p;
	}
}

int main(){
	int repeat;
	scanf("%d", &repeat);
	for(int re = 1;re <= repeat;re++){
		scanf("%d %d", &A, &B);
		for(int i = 0;i < A;i++){
			scanf("%lf", &G[i]);
		}
		init();
		printf("Case #%d: %.6lf\n", re, gao());
	}
	return 0;
}

