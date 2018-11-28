#include <fstream>
#include <iostream>

using namespace std;

bool *is_used;
int *used;

int solve(int a, int b) {
	int result = 0;
	int n_used = 0;

	int digits = 0;
	for (int x = a; x > 0; x /= 10) {
		digits++;
	}
	int pow = 1;
	for (int i = 0; i < digits; i++) {
		pow *= 10;
	}
	
	for (int i = 1, x = 10, y = pow / 10; i < digits; i++, x *= 10, y /= 10) {
		int c = (a / x) + (a % x) * y;
		if (c > a && c <= b && !is_used[c]) {
			result++;
			is_used[c] = true;
			used[n_used] = c;
			n_used++;
		}
	}
	
	for (int i = 0; i < n_used; i++) {
		is_used[used[i]] = false;
	}

	return result;
}

int main() {
    
	is_used = new bool[2000000 + 1];
	used = new int[2000000];
	fill(is_used, is_used + 2000000 + 1, false);

	ifstream fin("c.in");
	ofstream fout("c.out");
	
	int T;
	fin >> T;
	
	for (int i = 1; i <= T; i++) {
		int A, B;
		fin >> A >> B;
		long long R = 0;
		for (int a = A; a <= B; a++) {
			R += solve(a, B);
		}
		fout << "Case #" << i << ": " << R << "\n";
	}

	delete[] is_used;
	delete[] used;
	
    return 0;
}
