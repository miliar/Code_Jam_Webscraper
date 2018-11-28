#include<iostream>

#include<cstdio>

#include<fstream>

#include<algorithm>

using namespace std;

int testcases;

int P, K, L;

int used[2000];

int main() {

	FILE *fin = fopen("a2.in", "r");

	ofstream cout("a2.out");

	fscanf(fin, "%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++) {

		fscanf(fin, "%d %d %d", &P, &K, &L);

		for (int i = 0; i < L; i++) fscanf(fin, "%d", &used[i]);

		long long ans = 0;

		sort(used, used + L);

        for (int i = 0; i < L - 1 - i; i++) swap(used[i], used[L - 1 - i]);

		for (int i = 0; i < L; i++) ans += used[i] * (i / K + 1);

		cout << "Case #" << cases << ": " << ans << endl;
	}

	return 0;
}
