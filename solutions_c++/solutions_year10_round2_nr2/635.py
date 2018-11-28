#include <iostream>

#define MAXNUM 100
#define MAXINT 1000000

using std::cin;
using std::cout;
using std::endl;

typedef struct {
	int pos, vel;
} chicken;

chicken chicks[MAXNUM];

// Number of cases
int c = 0, num = 1;
// n => number of chics
// k => chics that need to arrive at the barn
// b => distance to the barn
// t => minimum time to the chics arrive at the barn
int n = 0, k = 0 , t = 0;
long long b = 0;

void swap (int i, int j)
{
	chicken c = chicks[j];
	for (int a = j; a < i; a++)
		chicks[a] = chicks[a+1];

	chicks[i] = c;
}

int main()
{
	cin >> c;

	while (num <= c) {
		cin >> n >> k >> b >> t;

		for (int i = 0; i < n; i++) {
			cin >> chicks[i].pos;
//			cout << chicks[i].pos << endl;
		}
//		cout << endl << endl;

		for (int i = 0; i < n; i++) {
			cin >> chicks[i].vel;
//			cout << chicks[i].vel << endl;
		}
//		cout << endl << endl;

		long long final[MAXNUM];
		for (int i = 0; i < n; i++) {
			final[i] = chicks[i].pos + (chicks[i].vel * t);
//			cout << final[i] << endl;
		}
//		cout << endl << endl;

		// To calculate the number of swaps
		int total = 0;
		for (int i = n-k; i < n; i++) {
			total += i;
		}

		for (int i = (n-1); (k > 0 && i >= 0); i--) {
			// This chick arrived at the barn on time
			if (final[i] >= b) {
				k--;
				total -= i;
//				cout << i << endl;
			}
			if (i == 0 && k != 0)
				total = MAXINT;
		}

		cout << "Case #" << num << ": ";
		if (total != MAXINT)
			cout << total << endl;
		else
			cout << "IMPOSSIBLE" << endl;

		num ++;
	}

	return 0;
}
