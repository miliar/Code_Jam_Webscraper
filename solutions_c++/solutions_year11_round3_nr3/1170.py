#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <exception>
using namespace std;

int main(int argc, char** argv) {
	try {
		ifstream ifs;
		ifs.exceptions(ifstream::failbit | ifstream::badbit);
		ifs.open(argv[1]);

		size_t T;
		ifs >> T;
		cerr << "T=" << T << endl;

		for (size_t t = 0; t < T; ++t) {

			size_t N;
			unsigned long long L, H;

			ifs >> N >> L >> H;
			vector<unsigned long long> a(N);

			for (size_t n = 0; n < N; ++n) {
				ifs >> a[n];
			}

			cout << "Case #" << (t+1) << ": ";

			bool flag = true;
			for (unsigned long long note = L; note <= H; ++note) {
				flag = true;
				for (size_t n = 0; n < N; ++n) {
					if (note > a[n]) {
						if (note % a[n] != 0) {
							flag = false;
							break;
						}
					}
					else {
						if (a[n] % note != 0) {
							flag = false;
							break;
						}
					}
				}
				if (flag) {
					cout << note << endl;
					break;
				}
			}
			if (!flag) cout << "NO" << endl;
		}

	} catch (exception& ex) {
		cerr << "Exception: " << ex.what() << endl;
	}
}
