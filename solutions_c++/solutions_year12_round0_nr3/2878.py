#include <iostream>
#include <fstream>

using namespace std;

int TEN[] = {0, 1, 10, 100, 1000, 10000, 100000, 10000000};

int digit(int n) {
	int c = 0;
	while (n > 0) {
		++c;
		n /= 10;
	}
	return c;
}

int next(int n, int digit) {
	return (n % 10) * TEN[digit] + n / 10;
}

int main() {
	ifstream in = ifstream("test.txt");
	ofstream out = ofstream("answer.txt");
	int T; in >> T;
	for (int t = 1; t <= T; ++t) {
		int A, B;
		in >> A >> B;
		int ans = 0;
		for (int n = A; n <= B; ++n) {
			int d = digit(n);
			int m = n;
			while ((m = next(m, d)) != n) 
				if (m > n && m >= A && m <= B)
					ans++;
		}
		out << "Case #" << t << ": " << ans << endl;
		cout << t << endl;
	}
	in.close();
	out.close();
	return 0;
}