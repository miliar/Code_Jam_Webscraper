#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;

int a1, a2, b1, b2;

bool win(int a, int b) {
	if (a < b) {
		return win(b, a);
	}
	if (2 * b <= a) return true;
	if (3 * b >= 2 * a) return false;
	return win(a - b, 2 * b - a);
}

void go(int t) {
	cin>>a1>>a2>>b1>>b2;
	int sum = 0;
	for (int a = a1; a <= a2; a++) {
		for (int b = b1; b <= b2; b++) {
			if (win(a, b)) sum++;
		}
	}
	cout << "Case #" << t << ": " << sum << endl;
}

int main() {
	int t;
	cin>>t;
	for (int i = 1; i <= t; i++) {
		go(i);
	}
	return 0;
}
