#include <iostream>
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

#define MAX_BITS 21
#define MAX_CANDIES 1005

bool candyComp(pair<int, bitset<MAX_BITS> > a, pair<int, bitset<MAX_BITS> > b) {
	return a.first > b.first;
}

bool chosen[MAX_CANDIES];
int maxCandidate;
bool solved;
unsigned long solution;
vector<pair<int, bitset<MAX_BITS> > > candies;

bitset<MAX_BITS> crapSum(bitset<MAX_BITS> a, bitset<MAX_BITS> b) {
	bitset<MAX_BITS> res;
	for (int i = 0; i < MAX_BITS; ++i) {
		res[i] = a[i] ^ b[i];
	}
	return res;
}

bitset<MAX_BITS> sumPile1() {
	bitset<MAX_BITS> sum(0);
	for (int i = 0; i < maxCandidate; ++i) {
		if (chosen[i]) {
			sum = crapSum(sum, candies[i].second);
		}
	}
	return sum;
}

bitset<MAX_BITS> sumPile2() {
	bitset<MAX_BITS> sum(0);
	for (int i = 0; i < maxCandidate; ++i) {
		if (!chosen[i]) {
			sum = crapSum(sum, candies[i].second);
		}
	}
	return sum;
}

unsigned long realSumPile1() {
	unsigned long sum = 0;
	for (int i = 0; i < maxCandidate; ++i) {
		if (chosen[i]) {
			sum += candies[i].second.to_ulong();
		}
	}
	return sum;
}

//void printChosen() {
//	for (int i = 0; i < maxCandidate; ++i) {
//		if (chosen[i]) {
//			cerr << candies[i].first << "\n";
//		}
//	}
//}

void candySolve(int currentCandidate) {
	if (!solved) {
		if (currentCandidate < maxCandidate) {
			chosen[currentCandidate] = 1;
			candySolve(currentCandidate + 1);

			if (!solved) {
				chosen[currentCandidate] = 0;
				candySolve(currentCandidate + 1);
			}
		} else {
			bitset<MAX_BITS> pile1 = sumPile1();
			bitset<MAX_BITS> pile2 = sumPile2();
			if (pile1 == pile2 && pile1.any() && pile2.any()) {
				solved = true;
				solution = realSumPile1();
				return;
			}
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	int testCases;
	cin >> testCases;

	for (int testCase = 1; testCase <= testCases; ++testCase) {
		int candySz;
		cin >> candySz;

		memset(chosen, 0, sizeof(bool) * MAX_CANDIES);
		maxCandidate = candySz;
		solved = false;
		solution = 0;
		candies.clear();

		for (int i = 0; i < candySz; ++i) {
			int c;
			cin >> c;
			bitset<MAX_BITS> cBits(c);
			candies.push_back(make_pair(c, cBits));
		}
		
		sort(candies.begin(), candies.end(), candyComp);
				
		candySolve(0);
		
		cout << "Case #" << testCase << ": ";
		if (solved)
			cout << solution;
		else 
			cout << "NO";
		cout << "\n";
	}
	return 0;
}