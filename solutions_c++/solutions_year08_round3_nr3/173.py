#include <iostream>
#include <vector>
#include <string>
#include <map>

typedef long long ll;
using namespace std;
	
int main() {
	int numberOfTests;
	cin >> numberOfTests;
	for (int test = 1; test <= numberOfTests; test++) {
		ll sum = 0;
		ll n, m, X, Y, Z;
		cin >> n >> m >> X >> Y >> Z;
		vector <ll> A(m);
		for (int i = 0; i < m; i++) cin >> A[i];
		vector <ll> S(n);
		vector <ll> R(n);
		for (int i = 0; i < n; i++) R[i] = 1;
		for (int i = 0; i <= n-1; i++) {
			S[i] = A[i % m];
			A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < i; j++) {
				if (S[j] < S[i]) R[i] = (R[i] + R[j]) % 1000000007;
			}
		}
		for (int i = 0; i < n; i++) {
			sum = (sum + R[i]) % 1000000007;
		}
		printf("Case #%d: %d\n", test, sum);
	}
	return 0;
}
