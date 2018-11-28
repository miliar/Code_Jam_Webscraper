#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#define Max 0x7fffffff
#define Min 0x80000000
#define Maxn 800

using namespace std;

void init(void);
void process(void);
void out(void);

int n , T;
int X[Maxn + 1];
int Y[Maxn + 1];
__int64 ans;

FILE *in = fopen("input.txt" , "r");
FILE *op = fopen("output.txt" , "w");

int main(void){
	int i;
	fscanf(in , "%d" , &T);
	for(i=1; i<=T; i++){
		init();
		process();
		fprintf(op , "Case #%d: " , i);
		out();
	}
	fclose(in);
	fclose(op);
	return 0;
}

void init(void){
	int i;
	fscanf(in , "%d" , &n);
	for(i=1; i<=n; i++){
		fscanf(in , "%d" , &X[i]);
	}
	for(i=1; i<=n; i++){
		fscanf(in , "%d" , &Y[i]);
	}
	sort(&X[1] , &X[n + 1]);
	sort(&Y[1] , &Y[n + 1]);
}

void process(void){
	ans = 0;
	int i , j;
	for(i=1,j=n; i<=n; i++,j--){
		ans += ((__int64)X[i] * (__int64)Y[j]);
	}
}

void out(void){
	fprintf(op , "%I64d\n" , ans);
}