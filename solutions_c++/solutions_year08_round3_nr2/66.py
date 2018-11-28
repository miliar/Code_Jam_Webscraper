#define _CRT_SECURE_NO_DEPRECATE

#include<iostream>

#include<cstdlib>

#include<cstdio>

#include<algorithm>

using namespace std;

int testcases;

int digit[100], len;

int ugly;

void solve(int ,long long, long long, int);

int main() {

    FILE *fin = fopen("b11.in", "r");

	FILE *fout = fopen("b11.out", "w");

	fscanf(fin, "%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++) {

		char tmpstr[100];

		fscanf(fin, "%s", tmpstr);

		len = strlen(tmpstr);

		for (int i = 0; i < len; i++) digit[i] = tmpstr[i] - '0';


		ugly = 0;

		solve(1, 0, digit[0], 1);

		fprintf(fout, "Case #%d: %d\n", cases, ugly);
	}

	return 0;
}

void solve(int depth, long long sum, long long now, int op) {

	if (depth == len) {

		if (op == 1) sum += now; else sum -= now;

		if (sum % 2 == 0 || sum % 3 == 0 || sum % 5 == 0 || sum % 7 == 0) ++ugly;

		return;
	}

	long long tmp = now * 10 + digit[depth];

	solve(depth + 1, sum, tmp, op);

	if (op == 1) tmp = sum + now; else tmp = sum - now;

	solve(depth + 1, tmp, digit[depth], -1);

	solve(depth + 1, tmp, digit[depth], 1);
}
