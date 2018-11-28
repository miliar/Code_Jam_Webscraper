#include <iostream>

using namespace std;

int main() {
	int T; // # of test case
	cin >> T;
	
	for (int i = 1; i <= T; i++) {
		int N;	// # of wires you see
		int res = 0;
		
		cin >> N; 
		int *A, *B;
		
		A = new int[N];
		B = new int[N];
		
		for (int j = 0; j < N; j++) {
			cin >> A[j];
			cin >> B[j];
		}
		
		for (int j = 0; j < N; j++) {
			for (int k = j + 1; k < N; k++) {
				if ((A[j] - A[k]) * (B[j] - B[k]) < 0)
					res++;
			}
		}
		
		delete[] A;
		delete[] B;
		
		cout << "Case #" << i << ": " << res << endl;	
	}
	
	return 0;	
}
