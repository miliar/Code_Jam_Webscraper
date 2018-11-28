#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int pot10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
int alreadySeenRecycledNumbers[2000001];

int getRecyclingNumber(int num, int numDigits, int recyclingDigits) {
	return pot10[numDigits - recyclingDigits] *  (num % pot10[recyclingDigits]) + (num / pot10[recyclingDigits]);
}

int countRecyclingPairs(int num, int top) {
	int digits = log10(num) + 1, count = 0;
	
	for(int i = 1; i < digits; i++) {
		int recyclingNumber = getRecyclingNumber(num, digits, i);
		
		if(recyclingNumber > num && recyclingNumber <= top && alreadySeenRecycledNumbers[recyclingNumber] != num ) {
			alreadySeenRecycledNumbers[recyclingNumber] = num;
			count++;
		}
	}
	
	return count;
}

int main(void) {
	int T, A, B;
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++) {
		cin >> A >> B;
		memset(alreadySeenRecycledNumbers, 0, sizeof(alreadySeenRecycledNumbers));
		
		int totalCount = 0;
		for(int i = A; i <= B; i++) {
			totalCount += countRecyclingPairs(i, B);
		}
		
		cout << "Case #" << numCase << ": " << totalCount << endl;
	}
}
