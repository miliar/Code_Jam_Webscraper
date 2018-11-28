#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#include <string>
#include <iostream>
#include <istream>
#include <sstream>
#include <cmath>
#include <set>

using namespace std;

unsigned long recycledPairs(unsigned long n, unsigned long B, unsigned short front, unsigned short back) {
	unsigned long m, y;
	set<int> mSet;
	
	y = 0;
	
	while (front >= 10) {
		m = (n % back)*front + n/back;		
		
		if (m > n && m <= B && mSet.find(m)==mSet.end()) {			
			mSet.insert(m);
			y++;
		}
	
		back*=10;
		front/=10;
	}
	
	return y;
}

unsigned short numLength(unsigned long A) {
	unsigned short length = 0;
	
	while (A) {
		length++;
		A /= 10;
	}
	
	return length;
}

int main() {
	unsigned short T;
	unsigned long A, B, y;
	
	cin >> T;
	
	for (unsigned short t = 1; t <= T; t++) {
		cin >> A >> B;
		
		y = 0;
		
		unsigned short length = numLength(A);
		
		unsigned short back, front;
	
		back = 10;
		front = ((unsigned short) pow(10, length)) / 10;
		
		for (unsigned long n = A; n < B; n++) {
			// Recycle pairs for n
			y += recycledPairs(n, B, front, back);
			
		}
		
		// Solution:	
		cout << "Case #" << t << ": " << y << endl;
	}
	
	return 0;

}
