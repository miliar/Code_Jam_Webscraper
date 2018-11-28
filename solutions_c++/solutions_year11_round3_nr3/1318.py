#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <iomanip>
#include <algorithm>
#include <list>
#include <cmath>

using namespace std;

unsigned long long L; 
unsigned long long H; 

std::ostream& outCase(unsigned int tc) {
	std::cout << "Case #" << (tc + 1) << ": ";
	return std::cout;
}

unsigned long long gcd(unsigned long long a, unsigned long long b)
{
    for (;;)
    {
        if (a == 0) {
			return b;
		}
        b %= a;
        if (b == 0) {
			return a;
		}
        a %= b;
    }
}

unsigned long long lcm(unsigned long long a, unsigned long long b)
{
    unsigned long long temp = gcd(a, b);

	if (temp == 0) return 0;

	unsigned long long x = a / temp;
	unsigned long long r = x * b;
	if (r / b != x) { //overflow
		return 0;
	}
    return r;
}

unsigned long long testCase() {
	unsigned N; cin >> N;
	cin >> L;
	cin >> H;

	unsigned long long low;
	unsigned long long high;
	vector<unsigned long long> freqs(N);
	for (unsigned i = 0; i < N; ++i) {
		cin >> freqs[i];
	}

	if (L == 1)
		return 1;

	for (unsigned long long f = L; f <= H; ++f) {
		bool ok = true;
		for (vector<unsigned long long>::const_iterator it = freqs.begin(); it != freqs.end(); ++it) {
			if (f % *it && *it % f) {
				ok = false;
				break;
			}
		}
		if (ok)
			return f;
	}

	return 0;

}

int main() {
	unsigned int T; cin >> T;
	for (unsigned int t = 0; t < T; ++t) {		
		outCase(t);
		unsigned long long r = testCase();		
		if (r) 
			cout << r << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}
