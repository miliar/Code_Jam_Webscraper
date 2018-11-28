#define _CRT_SECURE_NO_DEPRECATE

#include<algorithm>

#include<cstdio>

#include<cstdlib>

#include<iostream>

#include<sstream>

#include<fstream>

#include<map>

#include<vector>

#include<cmath>

using namespace std;

const int maxN = 300;


int testcases;

int NA, NB, T;

int leave_fromA[maxN], arrive_fromA[maxN];

int leave_fromB[maxN], arrive_fromB[maxN];

bool nec_fromA[maxN], nec_fromB[maxN];

bool used[maxN];

int main() {

	FILE *fin = fopen("B.in", "r");

	FILE *fout = fopen("B.out", "w");

	fscanf(fin, "%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++) {

		fscanf(fin, "%d", &T);

		fscanf(fin, "%d %d", &NA, &NB);

		for (int i = 0; i < NA; i++) {

			int a, b;

			fscanf(fin, "%d:%d", &a, &b);

			leave_fromA[i] = a * 60 + b;

			fscanf(fin, "%d:%d", &a, &b);

			arrive_fromA[i] = a * 60 + b;
		}

		for (int i = 0; i < NB; i++) {

			int a, b;

			fscanf(fin, "%d:%d", &a, &b);

			leave_fromB[i] = a * 60 + b;

			fscanf(fin, "%d:%d", &a, &b);

			arrive_fromB[i] = a * 60 + b;
		}

		memset(nec_fromA, 1, sizeof nec_fromA);

		memset(nec_fromB, 1, sizeof nec_fromB);

		memset(used, 0, sizeof used);

		for (int i = 0; i < NA; i++) {

			int min = -1; 

			int id = -1;

			for (int k = 0; k < NB; k++) if (arrive_fromB[k] + T <= leave_fromA[i] && !used[k] && arrive_fromB[k] > min) {

				min = arrive_fromB[k];

				id = k;
			}

			if (id == -1) continue;

			nec_fromA[i] = false;

			used[id] = true;
		}

		memset(used, 0, sizeof used);

		for (int i = 0; i < NB; i++) {

			int min = -1;

			int id = -1;

			for (int k = 0; k < NA; k++) if (arrive_fromA[k] + T <= leave_fromB[i] && !used[k] && arrive_fromA[k] > min) {

				min = arrive_fromA[k];

				id = k;
			}

			if (id == -1) continue;

			nec_fromB[i] = false;

			used[id] = true;
		}

		int ansA = 0;

		int ansB = 0;

		for (int i = 0; i < NA; i++) if (nec_fromA[i]) ++ansA;

		for (int i = 0; i < NB; i++) if (nec_fromB[i]) ++ansB;

		fprintf(fout, "Case #%d: %d %d\n", cases, ansA, ansB);
	}

	return 0;
}
