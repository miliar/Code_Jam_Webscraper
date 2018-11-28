#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
const int NMAX = 10000;

int T, N;
int A[NMAX], B[NMAX], C[NMAX], O[NMAX];

int compare(int a, int b) {
	if ( A[a] > A[b] ) return 0;
	return 1;
}

int main() {
	cin >> T;
	for (int c=0; c<T; ++c) {
		cin >> N;
		for (int i=0; i<N; ++i) {
			O[i] = i;
			cin >> A[i] >> B[i];
			C[i] = B[i];
		}
		sort(C, C+N);
		sort(O, O+N, compare);

		int answer = 0;

		for (int i=0; i<N; ++i) {
			int x = 0;
			for (int j=i+1; j<N; ++j)
				if ( B[O[j]] < B[O[i]] ) ++ x;
			answer += x;
		}
		cout << "Case #" << (c+1) <<  ": " << answer << endl;
	}
	return 0;
}
