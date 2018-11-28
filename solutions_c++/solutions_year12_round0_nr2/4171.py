#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_N = 100;

int n;
int t[MAX_N];

int s;

int p;

int solve() {
	int limA = p + 2 * max(0, p-2);
	int limB = p + 2 * max(0, p-1);
	
	int count = 0;
	int lower = 0;
	
	for (int i = 0; i < n; i++)
		if (t[i] >= limB)
			count++;
		else if (t[i] >= limA)
			lower++;
	return count + min(lower, s);
}

int main() {
	int tests;
	cin >> tests;

	for (int tNr= 0; tNr < tests; tNr++) {
		cin >>  n >> s >> p;
		for (int i = 0; i < n; i++)
			cin >> t[i];
		printf("Case #%d: %d\n", tNr+1, solve());
	}

	return 0;
}
