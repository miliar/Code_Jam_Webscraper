//============================================================================
// Name        : B.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

long long int L,P,C,outp;

int main() {
	long long int cas,cnt=0,now;
	freopen("B-large.in", "r", stdin);
	FILE *out;
	out = fopen("output.txt", "w");
	scanf("%lld", &cas);
	while(cas--){
		scanf("%lld%lld%lld", &L, &P, &C);
		now = L*C;
		if(now >= P){
			fprintf(out, "Case #%d: 0\n", ++cnt);
			continue;
		}
		outp = 1;
		while(1){
			if(now*C >= P){
				break;
			}
			now *= C;
			C *= C;
			++outp;
		}
		fprintf(out, "Case #%lld: %lld\n", ++cnt, outp);
	}
	fclose(out);
	return 0;
}
