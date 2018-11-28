#include <iostream>

using namespace std;

//#define __TEST

bool check(int A, int B) {
	bool lose = false;	// 주도권을 A가 가지고 있으면 false, B가 가지고 있으면 true
	int a, b;
	if (A < B) {
			int t = A;
			a = B;
			b = t;	
	} else {
		a = A;
		b = B;
	}

#ifdef __TEST		
	cout << "A: " << A << " B: " << B << " ";
#endif
	while(true) {
		if (a == b) {
#ifdef __TEST		
			cout << "T" << endl;
#endif			
			return lose;
		}
		
		if (a % b == 0) {
#ifdef __TEST		
			cout << "T" << endl;
#endif
			return (!lose);
		}
			
		if (a < 2 * b) {
			lose = !lose;	// 주도권이 넘어감
		} else {
			// 현재 주도권자가 승리함
			return (!lose);
		}
			
		int t = b;	// smaller
		b = a % b;
		a = t;	
	}	
}

int main() {
	int T;
	
//	check(5,3);
//	return 0;
	
	cin >> T;
	
	for (int i = 1; i <= T; i++) {
		int res = 0;
		int A1, A2, B1, B2;
		
		cin >> A1;
		cin >> A2;
		cin >> B1;
		cin >> B2;

#ifdef __TEST		
		cout << "A1: " << A1 << " A2: " << A2 << " B1: " << B1 << " B2: " << B2 << endl;
#endif
		
		for (int j = A1; j <= A2; j++) {
			for (int k = B1; k <= B2; k++) {
				if (check(j, k) == true)
					res++;
			}
		}
		
		cout << "Case #" << i << ": " << res << endl;	
	}

	return 0;
}
