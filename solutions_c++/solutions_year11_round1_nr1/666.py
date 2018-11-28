#include <iostream>
#include <fstream>
using namespace std;

typedef long long ll;

bool poss(ll n, int pd, int pg) {
	if (n>100)
		n=100;
	for (int d = 1; d<=n; ++d) {
		if ((pd * d) % 100 != 0)
			continue;
		int wd = (pd * d) / 100;
		int ld = d - wd;
		if (pg == 0 && wd)
			continue;
		if (pg == 100 && ld)
			continue;
		return true;
	}
	return false;
}

int main(int argc, char*argv[]) {
	int T;
	char *fname;
	if (argc==2)
		fname = argv[1];
	else
		fname = (char*)"input.txt";
	ifstream in;
	in.open(fname, ifstream::in);
	in >> T;
	for (int i=1; i<=T; ++i) {
		ll n;
		int pd, pg;
		in >> n >> pd >> pg;
		cout << "Case #" << i << ": " << (poss(n, pd, pg) ? "Possible" : "Broken") << endl;
		// cerr << "Case #" << i << endl;
	}
	return 0;
}
