#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;

	#define cin fin
	#define cout fout
	ifstream fin("A-large.in");
	ofstream fout("A.out");

int main() {
	int cs; cin >> cs;
	for (int cn=1; cn<=cs; ++cn) {
        cout << "Case #" << cn << ": ";

		long long N = 0, D = 0, G = 0;
		cin >> N >> D >> G;
		long long d = __gcd(D, (long long)100);

		if (N >= 100/d && !(G == 100 && D < 100) && !(G == 0 && D > 0)) cout << "Possible\n";
		else cout << "Broken\n";
	}
	system("pause");
	return 0;
}
