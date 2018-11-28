#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAXN = 1005;

inline long long gcd(long long a, long long b) {return (b == 0 ? a : gcd(b,a%b));}
inline long long myabs(long long a) {return (a < 0 ? -a : a);}
long long mem[MAXN];
int N, T;

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N;
		for(int i = 0 ; i < N ; i++) {
			cin >> mem[i];
		}
		if (N == 2) {
			long long d = myabs(mem[0] - mem[1]);
			cout << "Case #" << t << ": " << ((((mem[0] + d - 1) / d) * d) - mem[0]) << endl;
		}	else {
			long long d = myabs(mem[0] - mem[1]);
			d = gcd(d, myabs(mem[0] - mem[2]));
			d = gcd(d, myabs(mem[1] - mem[2]));
			cout << "Case #" << t << ": " << ((((mem[0] + d - 1) / d) * d) - mem[0]) << endl;
		}
	}
	return 0;
}
