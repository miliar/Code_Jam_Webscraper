#include <iostream>
#include <math.h>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

int main() {

	int test,x,y,z;;
	cin >> test;

	for(int h = 1; h <= test; h++) {

		int ret;
		cin >> ret;

		int a = 1, b = 1;
		int t1 = 0, t2 = 0;
		for(int i = 0; i < ret; i++) { 
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

		cout << "Case #" << h << ": " << max(t1,t2) << endl;
	}

	return 0;
}
