//============================================================================
// Name        : snapper.cpp
// Author      : Kiran
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int numCases = 0;
	scanf("%d", &numCases);
	unsigned long results[30];
	results[0] = 1;

	// f(1) = 1, f(n) = f(n-1)*2+1
	for (int i=1;i<30;i++) {
		results[i] = results[i-1]*2+1;
	}

	for (int i=0;i<numCases;i++) {
		int N, ON=0;
		unsigned long K;
		scanf("%d %uld", &N, &K);
		for (unsigned long j=results[N-1];j<=K;) {
			if (j == K) {
				ON = 1;
				break;
			} else {
				j = j + 1 + results[N-1];
			}
		}
		if (ON == 1) {
			printf("Case #%d: ON\n", i+1);
		} else {
			printf("Case #%d: OFF\n", i+1);
		}
	}
	return 0;
}
