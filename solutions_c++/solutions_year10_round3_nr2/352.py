#include <iostream>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	
	long long t;
	cin >> t;
	for(long long idx = 1; idx <= t; idx ++) {
		long long L, P, C;
		cin >> L >> P >> C;
		long long i;
		long long now = L;
		for(i = 0; now < P; i ++) {
			now *= C;
		}
		//cout << "i = " << i << endl;
		
		long long count = 0;
		while(i != 1) {
			i = (i+1)/2;
			count ++;
		}
		//prlong longf("Case #%d: %d\n", idx, count);
		cout << "Case #" << idx << ": " << count << endl;
	}
	return 0;
}
