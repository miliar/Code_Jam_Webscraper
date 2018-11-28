#include<iostream>

#include<cstdio>

#include<fstream>

using namespace std;

int testcases;

const int base = 1000000007;

int N, M, X, Y, Z;

int A[10000];

int speed[10000];

int sum[10000];

int main() {

	FILE *fin = fopen("c1.in", "r");

	FILE *fout = fopen("c1.out", "w");

	fscanf(fin, "%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++) {

		fscanf(fin, "%d %d %d %d %d", &N, &M, &X, &Y, &Z);

		for (int i = 0; i < M; i++) fscanf(fin, "%d", &A[i]);


		for (int i = 0; i < N; i++) {

			speed[i] = A[i % M];

			A[i % M] = ((long long)X * A[i % M] + (long long)Y * (i + 1)) % Z;
		}

        int ans = 0;

		for (int i = 0; i < N; i++) {

			sum[i] = 1;

			for (int k = 0; k < i; k++) if (speed[k] < speed[i]) 

				sum[i] = (sum[i] + sum[k]) % base;

			ans = (ans + sum[i]) % base;
		}

		fprintf(fout, "Case #%d: %d\n", cases, ans);
	}

	return 0;
}
