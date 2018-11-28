//============================================================================
// Name        : Snaooer.cpp
// Author      : Bernis
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <algorithm>
using namespace std;



int main() {
	long int max=100; //100000000
    string fname = "A-small-attempt0";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int T,test;
	long int K;
	double X;
	scanf("%d", &T);
	for (long int c = 1; c <= T; ++c) {
	    int N;
		scanf("%d", &N);
		scanf("%d", &K);
		X=pow(2,(double)N)-1;
		test=0;
		for(long int i=1; i<= max; i++){
			if((i*X+(i-1)) == K){
				printf("Case #%d: ON\n", c);
				test=1;
			}
		}
		
		if (test!=1)printf("Case #%d: OFF\n", c);
	}
	return 0;
}
