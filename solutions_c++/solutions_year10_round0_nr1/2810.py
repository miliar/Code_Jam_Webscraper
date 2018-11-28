//============================================================================
// Name        : 2010firstA.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
using namespace std;

int N,K;

int main() {
	freopen("A-large.in", "r", stdin);
	int cas,cnt=0;
	FILE *in;
	in = fopen("out.txt", "w");
	scanf("%d", &cas);
	while(cas--){
		scanf("%d%d", &N, &K);
		if(!K){
			fprintf(in, "Case #%d: OFF\n", ++cnt);
			continue;
		}
		while(K){
			if(!(K%2))
				break;
			if(!(--N))
				break;
			K >>= 1;
		}
		if(!N)
			fprintf(in, "Case #%d: ON\n", ++cnt);
		else
			fprintf(in, "Case #%d: OFF\n", ++cnt);
	}
	return 0;
}
