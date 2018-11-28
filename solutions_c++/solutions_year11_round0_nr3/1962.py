#include <iostream>
#include <functional>
#include <cstdlib>
#include <vector>
#include <list>
#include <set>

using namespace std;

typedef multiset<unsigned long long int> mset;

int main() {
	int nCases;
	cin >> nCases;
	for (int thisCase = 1; thisCase <= nCases; thisCase++) {
	
		int nCandies;
		cin >> nCandies;
		
		mset candies;
		
		unsigned long long int xorv = 0;
		
		unsigned long long int value;
		for (int i = 0; i < nCandies; i++) {
			cin >> value;
			xorv ^= value;
			candies.insert(value);
		}
		
		if (xorv == 0) {
			
			value = 0;
			mset::iterator it = candies.begin();
			for (++it; it != candies.end(); ++it) {
				value += *it;
			}

			cout << "Case #" << thisCase << ": " << value << endl;
		} else {
			cout << "Case #" << thisCase << ": NO" << endl;
		}
	
		
	}	
}
