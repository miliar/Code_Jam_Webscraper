#include <iostream>
#include <math.h>
#include <algorithm>
#include <cstring>

using namespace std;

int main() {

	int t;
	cin >> t;

	for(int k = 1; k <= t; k++) {

		int r;
		cin >> r;

		int a = 1, b = 1;
		int t1 = 0, t2 = 0;
		for(int i = 0; i < r; i++) { 
			char ch; int it;
			cin >> ch >> it;
			if(ch == 'O') { 
				t1 = max(t2,(t1 + abs(it-a)))+1;
				a = it;
			}
			if(ch == 'B') {
				t2 = max(t1,(t2 + abs(it-b))) + 1;
				b = it;
			}
		}

		cout << "Case #" << k << ": " << max(t1,t2) << endl;
	}

	return 0;
}
