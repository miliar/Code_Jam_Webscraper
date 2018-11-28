#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>

#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <vector>

#include <cmath>
#include <time.h>
#include <cassert>
using namespace  std;
#pragma comment(linker, "/STACK:32108864")

#define lint long long
template<typename T> T abs(T a){ if ( a < 0 ) return -a; return a; }
template<typename T> T sqr(T a) { return (a) * (a); }
template<typename T> int size(T& a) { return (int)((a).size()); }
#define all(a) (a).begin(),(a).end()


void initf(){
#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}
int A[1100];
int sum = 0;

void rec(int left, int right){

	int c1 = 0;
	for(int i = left; i <= right; ++i){
		if (A[i] == 0) c1 = 1;
	}
	if (c1) {
		++sum;
	} else {
		for(int i = left; i <= right; ++i){
			A[i] -- ;
		}
	}
		
}
int main(){


	initf();
	int test;
	scanf("%d", &test);
	
	for(int t = 0; t < test; ++t){
		int P;
		int tt = 0;
		scanf("%d", &P);
		for(int i = 0; i < (1 << P); ++i){
			scanf("%d", &A[i]);
			tt += A[i];
		}
		sum = 0;
		int x;
		for(int i = 0; i < (1 << P) - 1; ++i)
			scanf("%d", &x);
		for(int i = 1; i <= P; ++i)
			for(int j = 0; j + (1 << i) - 1 <= (1 << P) - 1; j += (1 << i))
				rec(j, j + (1 << i) - 1);
		printf("Case #%d: %d\n", t + 1, sum);
	}


	return 0;
}