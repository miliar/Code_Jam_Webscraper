#include <iostream>
#include <math.h>
using namespace std;

#define MM 100003

long long A[510][510];
long long R[510];
long long C[510][510];

int main() {
	freopen("c-large.in", "r", stdin);
	freopen("c-large.out", "w", stdout);
	long long i, j, k, spaces, to_ins, tt, ttt;
	memset(A, 0, sizeof(A));
	memset(R, 0, sizeof(R));
	memset(C, 0, sizeof(C));
	
	for(i = 0; i <= 500; i++) {
		C[i][0] = C[i][i] = 1;
		for(j = 1; j < i; j++)
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MM;
	}
	
	for(i = 2; i <= 500; i++) {
		A[i][1] = 1;
		for(j = 2; j < i; j++) {
			for(k = max(j * 2 - i, 1LL); k < j; k++) {
				spaces = i - j - 1;
				to_ins = j - k - 1;
				A[i][j] = (A[i][j] + C[spaces][to_ins] * A[j][k]) % MM;
			}
		}
		for(j = 1; j < i; j++)
			R[i] = (R[i] + A[i][j]) % MM;
	}
	cin >> tt;
	for(ttt = 1; ttt <= tt; ttt++) {
		cin >> i;
		cout << "Case #" << ttt << ": " << R[i] << endl;
	}
	return 0;
}
