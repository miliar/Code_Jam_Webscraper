#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

typedef long long ll;

vector<int> primes;

bool IsPrime(int x) {
	if (x < 2) return false;
	for (vector<int>::const_iterator it = primes.begin();
			it != primes.end() && x / *it >= *it; ++it)
		if (x % *it == 0)
			return false;
	return true;
}

void InitPrimes() {
	primes.push_back(2);
	for (int i = 3; primes.back() < 1000 * 1000; i += 2)
		if (IsPrime(i))
			primes.push_back(i);
}

ll solve() {
	ll N;
	cin >> N;
	ll ans = 0;
	for (vector<int>::const_iterator it = primes.begin();
			it != primes.end() && N / *it >= *it; ++it) {
		ll t = N, c = 0;
		while (t >= *it) {
			t /= *it;
			++c;
		}
		ans += c - 1;
	}
	if (N > 1)
		++ans;
	return ans;
}

int main(int argc, char* argv[]) {
	InitPrimes();
    if (argc > 1) {
        char* file_name = argv[1];
        int len = strlen(file_name);
        if (strcmp(file_name + len - 3, ".in") == 0)
            file_name[len - 3] = 0;
        else if (strcmp(file_name + len - 1, ".") == 0)
            file_name[len - 1] = 0;
        freopen((string(file_name) + ".in").c_str(), "r", stdin);
        freopen((string(file_name) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc)
            cout << "Case #" << cc + 1 << ": " << solve() << endl;
    return 0;
}
