/*
 * c.cpp
 *
 *  Created on: May 8, 2010
 *      Author: Qiang Zeng
 */

#include <stdio.h>
#include <string.h>
#include<iostream.h>
#include <math.h>

int main(int argc, char **argv) {
	unsigned long long R;
	unsigned long long K;
	unsigned long long *g;
	int N;
	int i;
	int caseN=1;

	int caseNum;
	FILE *fp = fopen("C-large.in", "r");
	FILE *w = fopen("my-large.out", "w");
	fscanf(fp, "%i", &caseNum);

	while (caseNum-- > 0) {
		fscanf(fp, "%I64d %I64d %d", &R, &K, &N);
		g = new unsigned long long[N];
		for (i = 0; i < N; i++) {
			fscanf(fp, "%I64d", &g[i]);
		}

		unsigned long long money = 0;
		unsigned long long tmoney = 0;
		unsigned long long save[N];
		//		bool visit
		int sq[N];
		int order[N];
		for (i = 0; i < N; i++) {
			save[i] = 0;
			sq[i] = -1;
			order[i] = -1;
		}
		save[0] = 0;

		int ord = 0;
		sq[0] = 0;

		int pos = -1;
		int last = 0;
		int num = 0;
		unsigned long long round = 0;
		//	unsigned long long smoney=0;
		while (true) {
			pos = (pos + 1) % N;
			if (tmoney + g[pos] > K || num >= N) {
				round++;
				money += tmoney;
				if (round == R)
					break;

				sq[last] = pos;
				order[last] = ord++;

				if (save[pos] > 0 || pos == 0)
					break;
				save[pos] = money;
				last = pos;
				tmoney = 0;
				num=0;
			}
			tmoney += g[pos];
			num++;
		}

		if (round < R) {
			money += (R - round) / (order[last] - order[pos] + 1) * (money
					- save[pos]);
			int remain = (R - round) % (order[last] - order[pos] + 1);
			int next = pos;
			for (i = 0; i < remain; i++) {
				next = sq[next];
			}
			money += save[next] - save[pos];
		}

		fprintf(w, "Case #%d: %I64d\n", caseN, money);
		caseN++;
	}

}
