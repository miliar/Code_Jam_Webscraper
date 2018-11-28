//============================================================================
// Name        : first.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

const long MAX = 20000;
long A[MAX];
long B[MAX];

int main() {
	long t,T;
	long N,n, m;
	long count;
	cin >> T;

	//ifstream in("first.in");
	//ofstream out("first.out");
	//cin.rdbuf(in.rdbuf());
	//cout.rdbuf(out.rdbuf());

	for (t = 0; t < T; t++){
		cin >> N;
		count = 0;
		for (n = 0; n < N; n++){
			cin >> A[n];
			cin >> B[n];
		}

		for (n = 0; n < N-1; n++){
			for (m = n + 1; m < N; m++){
				if (((A[n] < A[m]) && (B[n] > B[m])) || ((A[n]>A[m])&& (B[n]<B[m])))
				  count++;
			}
		}
		cout << "Case #" << t+1 << ": " << count << endl;

	}
	return 0;
}
