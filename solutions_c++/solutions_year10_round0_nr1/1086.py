/*
 * A.cpp
 *
 *  Created on: May 8, 2010
 *      Author: Qiang Zeng
 */
#include <stdio.h>
#include <string.h>
#include<iostream.h>
#include <math.h>


int main(int argc, char **argv) {
	//	cout<<c(1,1);
	int caseNum;
	FILE *fp = fopen("A-small-attempt3.in", "r");
	FILE *w = fopen("A-small-practice.out", "w");
	fscanf(fp, "%i", &caseNum);
	//	caseNum=1;
	int caseN = 1;
	int N = 0;
	long long K = 0;
	while (caseNum-- > 0) {
		fscanf(fp, "%i %I64d", &N, &K);

		bool snapper[N];
		bool power[N + 1];
		int i;

		power[0] = true;
		snapper[0] = false;
		power[N] = false;
		for (i = 1; i < N; i++) {
			snapper[i] = false;
			power[i] = false;
		}

		while (K-- > 0) {
			power[N]=false;
			for (i = 0; i < N; ++i) {
				if(power[i]){
					snapper[i]=!snapper[i];
					if(i!=0)
						power[i]=false;
				}
			}
			for (i = 0; i < N; ++i) {
				if(power[i]&&snapper[i]){
					power[i+1]=true;
				}
			}
		}

		if (power[N]) {
			fprintf(w, "Case #%d: ON\n", caseN);
		} else {
			fprintf(w, "Case #%d: OFF\n", caseN);
		}
		caseN++;
	}
}
