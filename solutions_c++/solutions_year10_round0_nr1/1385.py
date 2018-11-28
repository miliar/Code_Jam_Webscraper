//============================================================================
// Name        : codejam11.cpp
// Author      : Jani
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
using namespace std;

typedef unsigned int uint;


int main() {

	int t;
	scanf("%d\n",&t);
	uint n,k;
	for (int i=0;i<t;++i){
		scanf("%u %u",&n,&k);
		k%=1<<n;
		if (k==((uint)1<<n)-1){
			printf("Case #%d: ON\n",i+1);
		} else {
			printf("Case #%d: OFF\n",i+1);
		}
	}

	return 0;
}
