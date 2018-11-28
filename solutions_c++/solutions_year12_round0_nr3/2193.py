#include <fstream>

using namespace std;

ifstream in("c.in");
ofstream out("c.out");

int a, b;

int rotate(int num, int numIni) {
	if (num % 100 == num) {
		if (num % 10 == 0)
			return num;
		return (num%10)*10 + (num/10);
	}
	int mod = 10;
	int left = 1;

	while (num % mod == 0)
		mod *= 10;
	while (num % (mod*left) != num)
		left *= 10;

	if (left == 1)
		return numIni;
	return (num % mod) * left + (num / mod);
}

int solveCase() {
	int res = 0;

	for (int num = max(a, 10); num <= b; ++num) {
		int next = rotate(num, num);

		while (next != num) {
			if (next > num && next <= b)
				++res;
			next = rotate(next, num);
		}
	}

	return res;
}

int main() {
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i) {
		in >> a >> b;

		out << "Case #" << i << ": ";
		out << solveCase() << "\n";
	}

	return 0;
}
