#include "stdafx.h"
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
#include "gmp.h"
using namespace std;

void loadData();
void doProcess(int k);

long X[1000];
long Y[1000];
int T; 
int n;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	loadData();
	exit(0);
}

void loadData(){
	int i,j;
	scanf("%d",&T);
	for(i = 0;i<T;i++){
		scanf("%d",&n);
		for(j=0;j<n;j++)
			scanf("%Ld",&X[j]);
		for(j=0;j<n;j++)
			scanf("%Ld",&Y[j]);
		doProcess(i+1);
	}
}

#define swap(a,b,c) { c=a; a=b; b=c; }

void doProcess(int k){
	int i, j;
	long tmp;
	__int64 prod;
	for(i=0;i<n-1;i++){
		for(j = i+1;j<n;j++){
			if(X[i]<X[j])swap(X[i],X[j],tmp)
			if(Y[i]>Y[j])swap(Y[i],Y[j],tmp)
		}
	}
	prod = 0;
	for(i=0;i<n;i++){
		prod += ((__int64)X[i])*Y[i];
	}
	printf("Case #%d: %I64d\n",k,prod);
}