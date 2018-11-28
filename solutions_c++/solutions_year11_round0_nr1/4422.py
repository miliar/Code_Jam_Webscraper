#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-out.txt", "w", stdout);
	int tests;
	cin >> tests;
	for(int test = 0; test < tests; test++) {
		int n;
		cin >> n;
		int posO = 1, posB = 1;
		int totalO = 0, totalB = 0;
		int res = n;
		char prev = 0;
		int countO = 0;
		int countB = 0;
		for(int i = 0; i < n; i++) {
			char player;
			int len;
			cin >> player >> len;
			if(player == 'O' && (prev == 0 || prev == 'O')) {
				totalO += abs(len - posO);
				posO = len;
				countO++;
			}else if (player == 'O') {
				res += totalB;
				countO++;
				int dest = abs(len - posO);
				if((totalB + countB) < dest) {
					totalO = dest - totalB - countB;
				}else {
					totalO = 0;
				}
				posO = len;
				totalB = 0;
				countB = 0;
			}
			if(player == 'B' && (prev == 0 || prev == 'B')) {
				totalB += abs(len - posB);
				posB = len;
				countB++;
			}else if (player == 'B') {
				res += totalO;
				countB++;
				int dest = abs(len - posB);
				if((totalO + countO) < dest) {
					totalB = dest - totalO - countO;
				}else {
					totalB = 0;
				}
				posB = len;
				totalO = 0;
				countO = 0;
			}
			prev = player;
		}
		res += totalB + totalO;
		cout << "Case #" << test + 1 << ": " <<  res << endl;
	}
	return 0;
}