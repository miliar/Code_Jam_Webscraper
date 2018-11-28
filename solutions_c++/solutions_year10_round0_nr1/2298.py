#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
ifstream in ("input.in");
ofstream out ("output.out");
string solve (int n, int k) {
	string s;
	do {
		if (k%2==1) s+='1';
		else s+='0';
		k/=2;
	}
	while (k!=0);
	if (n>s.size()) return "OFF\n";
	else {
		for (int i=0; i<n; i++)
			if (s[i]=='0') return "OFF\n";
		return "ON\n";
	}
}
int main() {
	int T;
	in >> T;
	for (int i=0; i<T; i++) {
		int N, K;
		in >> N >> K;
		out << "Case #" << i+1 << ": " << solve (N, K);
	}
	return 0;
}