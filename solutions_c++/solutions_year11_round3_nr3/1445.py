#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <stdlib.h>

//const __int64 X = 10000000000000000;
const __int64 X = 10000;

template<typename Ty>
int is_prime(Ty n)
{
	if (n <= 1) return 0;
	if (n == 2) return 1;
	if ((n & 1) == 0) return 0;

	for(Ty i = 3; i * i <= n; i += 2) {
		if (n % i == 0) return 0;
	}
	return 1;
}

int main(int argc, char* argv[])
{
	std::fstream fin(argv[1]);
	if (!fin.is_open()) return 1;

	int T;
	fin >> T;

	for (int t=0; t<T; t++) {
		__int64 N, L, H;
		fin >> N >> L >> H;

		std::set<__int64> other;
		for (int n=0; n<N; n++) {
			int F;
			fin >> F;
			other.insert(F);
		}

		__int64 i;
		for (i=L; i<=H; i++) {
			bool ok=true;
			for (std::set<__int64>::const_iterator it=other.begin(); ok && it!=other.end(); ++it) {
				ok = *it % i == 0 || i % *it == 0;
			}
			if (ok) {
				break;
			}
		}

		std::cout << "Case #" << (t + 1) << ": ";
		if (i <= H) {
			std::cout << i;
		} else {
			std::cout << "NO";
		}
		std::cout << "\n";
	}
}
