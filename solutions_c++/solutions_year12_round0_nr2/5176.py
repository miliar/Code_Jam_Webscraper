#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

// n + n + n
int threeN(int total) {
	if ( total % 3 != 0)
		return -1;
	return (total / 3);
}

// n + n + (n + 1)
int threeNPlusOne(int total) {
	if ( total - 1 < 0 )
		return -1;
	if ( (total - 1) % 3 != 0)
		return -1;
	return ((total - 1) / 3) + 1;
}

// n + (n + 1) + (n + 1)
int threeNPlusTwo(int total) {
	if ( total - 2 < 0 ) 
		return -1;
	if ( (total - 2) % 3 != 0 )
		return -1;
	return ((total - 2)/3) + 1;
}

// n + n + (n + 2)
int threeNPlusTwoSpecial(int total) {
	if ( total - 2 < 0 ) 
		return -1;
	if ( (total - 2) % 3 != 0 )
		return -1;
	return ((total - 2)/3) + 2;
}

// n + (n + 1) + (n + 2) 
int threeNPlusThreeSpecial(int total) {
	if ( total - 3 < 0)
		return -1;
	if ( (total - 3) %3 != 0 ) 
		return -1;
	return ((total - 3)/3 + 2);
}

// n + (n + 2) + (n + 2)
int threeNPlusFourSpecial(int total) {
	if ( total - 4 < 0)
		return - 1;
	if ( (total - 4) %3 != 0 )
		return -1;
	return ((total - 4)/3 + 2);
}


int main(int argc, char *argv[]) {
//	// tests
//	int item;
//	item = threeNPlusTwo(29);
//	cout << item << " should be 10" << endl;
//	item = threeNPlusTwoSpecial(20);
//	cout << item << " should be 8" << endl;
//	item = threeNPlusTwo(8);
//	cout << item << " should be 3" << endl;
//	item = threeN(18);
//	cout << item << " should be 6" << endl;
//	item = threeNPlusThreeSpecial(21);
//	cout << item << " should be 8" << endl;
	
	
	
	
	
	int caseTotal;
	cin >> caseTotal;
	
	for (int caseIndex = 0; caseIndex < caseTotal; caseIndex++) {
		int contestantsCount;
		cin >> contestantsCount;
		
		int totalSurprises;
		cin >> totalSurprises;
		
		int p;
		cin >> p;
		
		vector<int> contestants;
		contestants.resize(contestantsCount);
		
		for (int i = 0; i < contestantsCount; i++) {
			int combinedValue;
			cin >> combinedValue;
			contestants[i] = combinedValue;
		}
		
		int surprises = 0;
		int casesAboveP = 0;
		
		for (int i = 0; i < contestants.size(); i++) {
			int total = contestants[i];
			// try without surprise first
			
			if ( total == 0 ) {
				// only valid is threeN
				if ( p == 0 )
					++casesAboveP;
				
				continue;
			}
			
			int max = threeNPlusTwo(total);
			if ( max == -1 )
				max = threeNPlusOne(total);
			if ( max == -1 )
				max = threeN(total);
			
			bool wasValidWhenNotSpecial = (max != 1);
			if ( max >= p ) {
				++casesAboveP;
				continue;
			} else if ( max >= 0 ) {
				// max is less than p but not -1
				if ( surprises == totalSurprises ) {
					// can't use a surprise
					continue;
				}
			}
		
//			cout << surprises << endl;
//			cout << max << endl;
				
			// try with surprise then
			++surprises;
			assert(surprises <= totalSurprises);
			
			max = threeNPlusFourSpecial(total);
			if ( max == -1)
				max = threeNPlusThreeSpecial(total);
			if ( max == -1 )
				max = threeNPlusTwoSpecial(total);
			
			if ( max == -1) {
				cout << i << endl;
			}
			assert(max != -1);
			
			if ( max >= p ) {
				++casesAboveP;
			} else {
				if ( wasValidWhenNotSpecial ) {
					// means was still less than p when not special, why waste a special?
					--surprises;
				}
			}
		}
		
//		cout << "Case #" << caseIndex + 1 << ": " << contestantsCount << " " << totalSurprises << " " << p << endl;
	
		cout << "Case #" << caseIndex + 1 << ": " << casesAboveP << endl;
		
	}
	
	
	
	
	
}