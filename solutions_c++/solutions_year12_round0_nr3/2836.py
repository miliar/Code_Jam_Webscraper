#include <iostream>
#include <string>
#include <set>
#include <sstream>

using namespace std;

string itos_(int x) {
	ostringstream oss;
	oss << x;
	return oss.str();
}

int ten[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000 };

int mathM(int n, int nDigs, int i) {
	int m = n / ten[i];
	m += ten[nDigs - i] * (n % ten[i]);
	return m;
}

int findAndCountPairs(int A, int B, int n) {
	int count = 0;
	unsigned int nDigs = itos_(n).length();

	set<int> alreadyDone;
	for (unsigned int i = 1; i < nDigs; i++) {
		int m = mathM(n, nDigs, i);
		if ((A <= m) && (m <= B) && (m > n) && (alreadyDone.find(m)
				== alreadyDone.end())) {
			alreadyDone.insert(m);
			//cout << "(" << n << ", " << m << ")" << endl;
			count++;
		}
	}
	return count;
}

int countRecycledPairs(int A, int B) {
	int count = 0;
	for (int i = A; i <= B; i++) {
		count += findAndCountPairs(A, B, i);
	}
	return count;
}

int main() {
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		int A, B;
		cin >> A >> B;
		cout << "Case #" << i << ": " << countRecycledPairs(A, B) << endl;
	}

	return 0;
}
