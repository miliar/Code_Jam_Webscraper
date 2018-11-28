#define _CRT_SECURE_NO_DEPRECATE

#include<cstdio>

#include<iostream>

#include<fstream>

using namespace std;

int testcases;

const int MAXN = 1000;

int N;

int X[MAXN], Y[MAXN];

long long cost[MAXN][MAXN];

long long MIN, MAX;

long long lx[MAXN], ly[MAXN];

int link[MAXN];

bool x[MAXN], y[MAXN];

bool Find(int);

int main() {

	FILE *fin = fopen("a.in", "r");

	ofstream cout = ofstream("a.out");

	fscanf(fin, "%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++) {

		fscanf(fin, "%d", &N);

		for (int  i = 0; i < N; i++) fscanf(fin, "%d", &X[i]);

		for (int  i = 0; i < N; i++) fscanf(fin, "%d", &Y[i]);

		
		for (int i = 0; i < N; i++)

			for (int k = 0; k < N; k++) cost[i][k] = X[i] * Y[k];

		MIN = cost[0][0];

		MAX = cost[0][0];

		for (int i = 0; i < N; i++) {

			for (int k = 0; k < N; k++) {

				if (cost[i][k] < MIN) MIN = cost[i][k];

				if (cost[i][k] > MAX) MAX = cost[i][k];
			}
		}

		MIN = -MIN;

		MAX += MIN;

	//	cout << MIN << " " << MAX << endl;

		for (int i = 0; i < N; i++)

			for (int k = 0; k < N; k++) cost[i][k] = MAX - MIN - cost[i][k];

	/*	for (int i = 0; i < N; i++)

			for (int k = 0; k < N; k++) cout << i << " " << k << " " << cost[i][k] << endl;
    */
		fill(lx, lx + N, -1);

		fill(ly, ly + N, 0);

		fill(link, link + N, -1);

		for (int i = 0; i < N; i++)

			for (int k = 0; k < N; k++) 

				if (cost[i][k] > lx[i]) lx[i] = cost[i][k];

		for (int i = 0; i < N; i++) {

			while (1) {

				fill(x, x + N, false);

				fill(y, y + N, false);

				if (Find(i)) break;

				long long d = (long long)1e18;

			//	cout << d<< endl;

				for (int j = 0; j < N; j++) if (x[j])

					for (int k = 0; k < N; k++) if (!y[k])

						if (lx[j] + ly[k] - cost[j][k] < d) d = lx[j] + ly[k] - cost[j][k];

				for (int j = 0; j < N; j++) {

					if (x[j]) lx[j] -= d;

					if (y[j]) ly[j] += d;
				}
			}
		}

		long long ans = 0;

	//	for (int i = 0; i < N; i++) cout << " Test " << i << " " << link[i] << endl;

		for (int i = 0; i < N; i++) ans += cost[link[i]][i];

	//	cout << "ans is " << ans << endl;

		ans = MAX * N - ans;

		ans = ans - MIN * N;

		cout << "Case #" << cases << ": " << ans << endl;
	}

	return 0;
}

bool Find(int v) {

	x[v] = true;

	for (int t = 0; t < N; t++) if (!y[t] && lx[v] + ly[t] == cost[v][t]) {

		y[t] = true;

		int tmp = link[t];

		link[t] = v;

		if (tmp == -1 || Find(tmp)) return true;

		link[t] = tmp;
	}

	return false;
}
