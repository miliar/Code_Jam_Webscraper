//============================================================================
// Name        : CJ2012R1A.cpp
// Author      : LUU TUAN ANH
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#define  rep(i,a) for(int i=0; i < a; ++i)
using namespace std;

int A, B;
double p[1000001];

int main() {
	int test_num, test_id;
	double ans;
	double result, temp;

	ifstream ifs("A-small-attempt0.in");
	FILE* fi = fopen("A-small-attempt0.out", "w");
	ifs >> test_num;
	for(test_id = 1; test_id <= test_num; ++test_id) {
		// input
		ifs >> A >> B;
		rep(i,A){
			ifs >> p[i];
		}

		p[A] = 1;
		// processing
		ans = B + 2.0;
		temp = 1.0;
		rep(i,A) temp *= p[i];
		rep(n,A+1){
			temp /= p[A-n];
			result = temp * (2*n+B-A+1) + (1-temp) * (2*n+B-A+1+B+1);
			if (result < ans) ans = result;
		}
		// ouput
		fprintf(fi, "Case #%d: %f\n", test_id, ans);
	}
	fclose(fi);
	return 0;
}
