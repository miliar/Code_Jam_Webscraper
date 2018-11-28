#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <set>
using namespace std;

#define sz size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define sqr(x) ((x)*(x))

int solve(int l, int r) {
	int ans = 0;
	for(int num = l; num <= r; num++) {
		int lenNum = ceil(log(num + .0) / log(10.0)), next = num, pow = 1;
		while(next /= 10) {
			pow *= 10;
		}
		next = num;

		do {
			next = (next % 10) * pow + (next / 10);
			ans += (next > num && next <= r);
		} while(next != num);
	}

	return ans;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, a, b;
	cin >> t;
	for(int i = 1; i <= t; i++) { 
		cin >> a >> b;
		printf("Case #%d: %d\n", i, solve(a, b));
	}
	
	return 0;
}