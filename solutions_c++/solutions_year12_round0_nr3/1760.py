#include <cstdio>
#include <vector>
#include <memory.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>

using namespace std;

bool mark[2222222];
int A, B;

int get(int *a, int n) {
	int ret = 0;
	for (int i = 0; i < n; i++) {
		ret = 10 * ret + a[i];
	}
	return ret;
}

int len(int n) {
	if (n == 0) return 0;
	else return 1 + len(n / 10);
}

void nextCycle(int *a, int n) {
	int p = a[0];
	for (int i = 0; i < n - 1; i++) {
		a[i] = a[i + 1];
	}
	a[n - 1] = p;
}

long long f(int n) {
	long long ret = 1;
	mark[n] = true;

	int a[10];
	int k = len(n);
	int tmp = n;

	for (int i = k - 1; i >= 0; i--) {
		a[i] = tmp % 10;
		tmp /= 10;
	}

	nextCycle(a, k);
	int num = get(a, k);
	while (num != n) {
		if (A <= num && num <= B) {
			mark[num] = true;
			ret++;
		}
		nextCycle(a, k);
		num = get(a, k);
	}

	return ret;
}

int main(){
	FILE *fin = fopen("C.in", "r");
	FILE *fout = fopen("C.out", "w");

	int t;
	fscanf(fin, "%d", &t);

	for (int test = 1; test <= t; test++) {

		fscanf(fin, "%d%d", &A, &B);
		memset(mark, false, sizeof(mark));
		vector <long long> v;
		v.clear();
		
		for (int i = A; i <= B; i++) {
			if (!mark[i]) v.push_back( f(i) );
		}

		long long sol = 0;
		for (int i = 0; i < v.size(); i++) {
			sol += v[i] * (v[i] - 1) / 2;
		}
		
		fprintf(fout, "Case #%d: %lld\n", test, sol);
	}
}