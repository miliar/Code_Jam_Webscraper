#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

int zece[10] = {1, 
				10, 
				100, 
				1000, 
				10000, 
				100000, 
				1000000, 
				10000000, 
				100000000, 
				1000000000};

int solve (int A, int B) {
	
	//printf ("\n------%d %d\n", A, B);
	int rez = 0, n, m;

	set < pair <int, int> > S;

	for (int i = A; i <= B; i++) {
		n = i;
		//printf ("%d -> ", n);
		int digits = 0;
		while (n) {
			digits++;
			n = n / 10;
		}

		n = i;
		for (int j = 1; j < digits; j++) {
			m = n % zece[j];
			m = m * zece[digits - j] + n / zece[j];  
			if (A <= m && m <= B && n < m && S.find ( make_pair (n, m) ) == S.end ()) {
				rez++;
				//printf ("%d %d\n", n, m);
				S.insert ( make_pair (n, m) );
			}
		} 
		//printf ("\n");
	}

	return rez;                                                                             
}

int main () {

	freopen ("rec.in", "r", stdin);
	freopen ("rec.out", "w", stdout);
	
	int T, A, B, i;
	for (scanf ("%d", &T), i = 1; T; T--, i++) {
		scanf ("%d %d\n", &A, &B);
		printf ("Case #%d: %d\n", i, solve (A, B)); 
	}

	return 0;
}
