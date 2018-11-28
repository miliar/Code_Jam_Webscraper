
#include <iostream>
#include <stdint.h>

using namespace std;

void DoCase ()
{
	int64_t R, k;
	cin >> R;
	cin >> k;

	int64_t totalRiders = 0;

	int N;
	cin >> N;
	int64_t groupSize [1000];
	for (int i = 0; i < N; ++i) {
		cin >> groupSize [i];
		totalRiders += groupSize [i];
	}

	if (totalRiders <= k)
		cout << totalRiders * R;
	else {

		int64_t revenueMade [1000];
		int nextGroup [1000];

		for (int i = 0; i < N; ++i) {
			int next = i;
			int64_t riders = 0;
			while (riders + groupSize [next] <= k) {
				riders += groupSize [next];
				++next;
				if (next == N)
					next = 0;
			}
			revenueMade [i] = riders;
			nextGroup [i] = next;
		}

		int64_t runs = 0;
		int64_t totalRevenue = 0;
		int currentGroup = 0;
		do {
			totalRevenue += revenueMade [currentGroup];
			currentGroup = nextGroup [currentGroup];
			++runs;
		} while (runs < R && currentGroup != 0);
		totalRevenue *= R / runs;
		runs *= R / runs;
		while (runs < R) {
			totalRevenue += revenueMade [currentGroup];
			currentGroup = nextGroup [currentGroup];
			++runs;
		}
	
		cout << totalRevenue;
	}
}

main ()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		cout << "Case #" << i << ": ";
		DoCase ();
		cout << endl;
	}
}
