#include <fstream>
#include <iostream>
using namespace std;

bool validate(long N, int pd, int pg) {
	bool find = false;
	if (N < 100) {
		for (int i = 1; i <= N; i ++)
			if (i * pd % 100 == 0) {
				find = true;
				break;
			}
		if (!find)
			return false;
	}
	if (pg == pd)
		return true;
	if (pg < pd && pg > 1) {
		int delta = pd - pg;
		for (int i = 1; i <= N; i++)
			for (int j = 1; j < pg; j++) {
				if ((i * delta) % (pg - j) == 0)
					return true;
			}
	}
	if (pg > pd && pg < 100) {
		int delta = pg - pd;
		for (int i = 1; i <= N; i++)
			for (int j = pg + 1; j <= 100; j++)
				if ((i * delta) % (j - pg) == 0)
					return true;
	}
	return false;
}

int main() {
	int T;
	long N;
	int pd, pg;
	ifstream is("H:\\temp\\A-small.in");
	is >> T;
	ofstream os("H:\\temp\\A.out");
	string result;
	for (int t = 1; t <= T; t++) {
		is >> N >> pd >> pg;
		if (validate(N, pd, pg)) {
			result = "Possible";
		} else {
			result = "Broken";
		}
		os << "Case #" << t << ": " << result.c_str() << endl;
	}
	return 0;
}