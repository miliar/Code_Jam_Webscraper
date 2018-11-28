#include <iostream>
#include <cstdio>
#include <cmath>

char S[200];
long long a[200];

void search(int p, int n)
{
	if (p == n) {
		long long q = 0;
		for (int i = 0; i < n; i++) {
			q *= 2;
			q += a[i];
		}
		double g = sqrtl(q);
		long long t = (long long) floorl(g);
		if (t * t == q) {
			for (int i = 0; i < n; i++)
				std::cout << a[i];
		}
		return;
	}
	if (S[p] == '?') {
		a[p] = 0;
		search(p + 1, n);
		a[p] = 1;
		search(p + 1, n);
	} else {
		a[p] = S[p] - '0';
		search(p + 1, n);
	}
}

int main() 
{
	freopen("p4.in", "r", stdin);
	freopen("p4.out", "w", stdout);
	int T;
	std::cin >> T;
	
	for (int t = 0; t < T; t++) {
		std::cin >> S;
	    std::cout << "Case #" << t + 1 << ": ";
		search(0, strlen(S));
		std::cout << std::endl;
	}
	return 0;
}