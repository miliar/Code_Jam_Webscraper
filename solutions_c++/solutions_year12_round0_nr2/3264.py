#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#include <string>
#include <iostream>
#include <istream>
#include <sstream>

using namespace std;


bool best(unsigned short N, unsigned short p) {
	return ( N/3 + ((N%3) != 0) ) >= p;
}

bool bestS(unsigned short N, unsigned short p) {
	if (N < 2) return false;
	return ( N/3 + 1 + ((N%3) == 2) ) >= p;
}

int main() {
	unsigned short T, N, S, p, y;
	unsigned short total[100];

	cin >> T;
	
	for (unsigned short t = 1; t <= T; t++) {
		cin >> N >> S >> p;
		
		y = 0;
		
		for (int i = 0; i < N; i++) {
			cin >> total[i];
			
			if (best(total[i], p)) {
				y++;
			} else if (bestS(total[i], p) && S) {
				y++;
				S--;
			}
			
		}
				
		cout << "Case #" << t << ": " << y << endl;
	}
	
	return 0;

}
