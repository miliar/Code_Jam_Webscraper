#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>

using namespace std;

int n, l, h;
int notes[10000];

int gcd(int a, int b) {
    for (;;) {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int lcm(int a, int b) {
    int temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}

int lcm_all() {
	int res = accumulate(notes, notes + n, 1, lcm);
	return res;
}

bool is_good(int d) {
	for (int i = 0; i < n; ++i) {
		if (notes[i] % d != 0 && d % notes[i] != 0)
			return false;
	}
	return true;
}
int calc() {
	int res = 0;
//	std::cout << "calc " << n << " " << l << " " << h  << std::endl;
//	int l = lcm_all();
//	cout << "lcm " << l << endl;
//	l = accumulate(notes, notes + n, 1, gcd);
//	cout << "gcd " << l << endl;
	for (int i = l; i <= h; ++i) {
		if (is_good(i))
			return i;
	}
	return 0;
}


int main(int argc, char **argv) {
	string ifilename = "c.in";
	string ofilename = "c.out";
	ifstream ifs(ifilename.c_str());
	ofstream ofs(ofilename.c_str());

	int t;
	ifs >> t;
	for (int i = 0; i < t; ++i) {
		ifs >> n >> l >> h;
		for (int j = 0; j < n; ++j) {
			ifs >> notes[j];
		}

		int res = calc();
		ofs << "Case #" << (i+1) << ": ";
		if (res == 0)
			ofs << "NO" << endl;
		else
			ofs << res << endl;
	}

	ifs.close();
	ofs.close();
	return 0;
}
