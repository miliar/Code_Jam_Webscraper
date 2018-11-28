#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define REP(i, n) for (int i = 0; i < n; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define FORD(i, a, b) for (int i = a; i >= b; i--)

string process(long long n, long long k) {
	long long nn = (1LL << n);
//	cout << k << " " << nn << " " << k % nn << endl;
	if (k % nn != nn - 1) return "OFF";
	return "ON";
}

int main() {
	freopen("A-large.in", "r", stdin);
//	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int test;
	cin >> test;
	
	for (int i = 1; i <= test; i++) {
		long long n, k;
		cin >> n >> k;
		cout << "Case #" << i << ": " << process(n, k) << endl;
	}
	
	
	return 0;
}
