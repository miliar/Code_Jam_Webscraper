#include <stdlib.h>
#include <stdio.h>
#include <memory.h>

const char inFileName[] = "B-large.in";
const char outFileName[] = "B-large.out";

const int MaxP = 12;
const int MaxN = 10000;

struct Tree {
	int c, num, h;
};

int n, T, sol, p;
int m[MaxN];
Tree t[MaxN];
int d[MaxN][MaxP];

int max(int a, int b) {
	return (a > b ? a : b);
}

int min(int a, int b) {
	return (a < b ? a : b);
}

int solve(int node, int val) {
	if (d[node][val] == - 1) {
		if (node >= n) 
			return (d[node][val] = 0);
		if (t[node].num <= val)
			return (d[node][val] = 0);

		if (t[node].num - val == t[node].h)
			d[node][val] = t[node].c + solve(2 * node, val + 1) + solve(2 * node + 1, val + 1);
		else
			d[node][val] = min(t[node].c + solve(2 * node, val + 1) + solve(2 * node + 1, val + 1),
							   solve(2 * node, val) + solve(2 * node + 1, val));
	}
	
	return d[node][val];
}

int main() {

	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int i = 0; i < T; i++) {

		fscanf(inFile, "%d", &p);
		n = 1 << p;
		for (int i = 0; i < n; i++) {
			fscanf(inFile, "%d",&m[i]);
			m[i] = p - m[i];
		}
		for (int i = 1; i <= n - 1; i++)
			fscanf(inFile, "%d", &t[n - i].c);
		for (int i = n; i <= 2 * n - 1; i++) {
			t[i].num = m[2 * n - i - 1];
			t[i].h = 0;
		}

		for (int i = n - 1; i > 0; i--) {
			t[i].num = max(t[2 * i].num, t[2 * i + 1].num);
			t[i].h = 1 + t[2 * i].h;
		}
		
		for (int i = 0; i < MaxN; i++)
			for (int j = 0; j < MaxP; j++)
				d[i][j] = -1;

		fprintf(outFile, "Case #%d: %d\n", i + 1, solve(1, 0));
	}

	fclose(inFile);
	fclose(outFile);

	return 0;
}
