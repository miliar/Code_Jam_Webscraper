#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
ifstream in ("input.in");
ofstream out ("output.out");
int gcd (int a, int b) {
	if (b == 0)
		return a;
	else
		return gcd (b, a % b);
}
int gcd3 (int a, int b, int c) {
	return gcd (gcd (a, b), c);
}
const int inf = 200;
int main() {
	int C;
	in >> C;
	for (int i=0; i<C; i++) {
		int N, tmp;
		in >> N;
		if (N==2) {
			int a, b;
			in >> a >> b;
			int T = max (a, b) - min (a, b);
			out << "Case #" << i+1 << ": " << (a%T==0? 0: T-a%T) << "\n";
		}
		else {
			int a, b, c;
			in >> a >> b >> c;
			if (a<b) swap (a, b);
			if (b<c) swap (b, c);
			if (a<b) swap (a, b);
			int T = gcd3 (a-b, b-c, a-c);
			out << "Case #" << i+1 << ": " << (a%T==0? 0: T-a%T) << "\n";
		}
	}
	return 0;
}