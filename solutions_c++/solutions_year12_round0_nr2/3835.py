#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

bool sePuede(int n, int p, bool b) {
	int d = n / 3;
	int r = n % 3;
	
	if (!b) 
		return (p <= (d + (r > 0)));
	else {
		if (d == 0)
			return (p <= (d + r));
		return (p <= (d + 1 + (r > 1)));
	}
}

int main() {
	int t, n, s, p;
	cin >> t;
	vector <int> v;
	for (int k = 1; k <= t; k++) {
		cin >> n >> s >> p;
		v.resize(n);
		for (int i = 0; i < n; i++) 
			cin >> v[i];
				
		int r = 0;
		for (int i = 0; i < n; i++)
			if (sePuede(v[i], p, 0)) 
				r++;
			else if (sePuede(v[i], p, 1) && s) {
				r++;
				s--;
			}
			
		printf("Case #%d: %d\n", k, r);
	}
}
