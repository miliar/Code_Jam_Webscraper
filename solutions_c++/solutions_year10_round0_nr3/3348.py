#include <iostream>

using namespace std;

unsigned long long int groups[1000];
bool used[1000];
unsigned long long int whenUsed[1000];
unsigned long long int profitUsed[1000];
unsigned long long int afterPeriod[1000];

int main() {
	unsigned long long int t;
	cin >> t;
	for (unsigned long long int i=1; i<=t; i++) {
		unsigned long long int r, k, n;
		//r = rounds
		//k = places
		//n = groups
		cin >> r >> k >> n;

		for (unsigned long long int ni=0; ni<n; ni++) {
			cin >> groups[ni];
			used[ni] = 0;
		}
		unsigned long long int profit = 0;
		unsigned long long int pos = 0;
		bool cycleUsed = false;
		for (unsigned long long int ri=0; ri<r; ri++) {
			if (used[pos] && cycleUsed == false && false) {
				unsigned long long int periodLength = ri-whenUsed[pos];
				unsigned long long int periodProfit = profit - profitUsed[pos];
				unsigned long long int periodsTowalk = ((r-ri)/periodLength);
				cycleUsed = true;
				if (periodsTowalk > 0) {
					profit += periodProfit*periodsTowalk;
					ri += periodsTowalk*periodLength;
				}
				//pos = afterPeriod[pos];
			} else {
				unsigned long long int groupsIn = 0;
				unsigned long long int placesUsed = 0;
				used[pos] = true;
				profitUsed[pos] = profit;
				whenUsed[pos] = ri;
				//unsigned long long int periodStartPos = pos;
				//afterPeriod[periodStartPos] = pos;
				while (placesUsed + groups[pos] <= k && groupsIn < n) {
					placesUsed += groups[pos];
					profit += groups[pos];
					groupsIn++;
					if (pos + 1 == n)
						pos = 0;
					else
						++pos;
				}
				
			}
		}
		cout << "Case #" << i << ": " << profit << '\n';
	}
}