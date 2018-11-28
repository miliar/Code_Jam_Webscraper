#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <map>

using namespace std;

long long gcd(long long a, long long b) {
	if (b==0)
		return a;
	return gcd(b, a%b);
}


void spike() {
	long long n, l, h, a;
	vector<long long> values;

	cin >> n >> l >> h;
	for (long long i = 0; i < n; i++) {
		cin >> a;
		values.push_back(a);
	}

	

	long long res = 0, answer = -1;
	for (long long k = l; k <= h; k++) {
		bool good = true;
		for (long long i = 0; i < n; i++) {
			if (values[i] > k && values[i]%k != 0)
				good = false;
			
			if (values[i] <= k && k%values[i] != 0)
				good = false;

		}
		if(good && answer == -1)
			answer = k;
	}

	if(answer > 0)
		cout << answer << endl;
	else
		cout << "NO" << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);

	int z;
	cin >> z;
	for (int i = 0; i < z; i++) {
		cout << "Case #" << i+1 << ": ";
		spike();
	}
}