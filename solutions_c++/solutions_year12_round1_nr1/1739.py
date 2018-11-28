#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
	int Kase;
	cin >> Kase;
	for (int kase = 1; kase <= Kase; kase++) {
		cout << "Case #" << kase << ": ";
		
		int A, B;
		cin >> A >> B;
		vector< double > p (A, 0);
		for (int i = 0; i < A; i++) 
			cin >> p[i];

		vector< double > rt(A, 1); //running total
		for (int i = 0; i < A; i++) 
			for (int j = 0; j <= i; j++)
				rt[i] *= p[j];

		//for (int i = 0; i < A; i++) 
			//cerr << rt[i] << " ";
		//cerr << ": ";

		if (A == 0) {
			cout << B+1;
		} else {
			double m = 2 + (double)B; // giving up straight away
			for (int i = 0; i < A; i++) { //num backspaces
				int keys = 2*i + (B-A) + 1;
				double total = rt[A-i-1] * (double) keys;
				keys += B + 1;
				total += (1 - rt[A-i-1]) * (double) keys;

				m = min(m, total);
			}
			cout << m;
		}

		cout << endl;
	}
}
