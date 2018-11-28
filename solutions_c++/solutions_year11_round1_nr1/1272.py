#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)
#define for02(i,n) for(int i = 0; i <= (n); i ++)
#define for1(i,n) for(int i = 1; i <= (n); i ++)

int n, pd, pg;

int main() {
	
	int kases; cin >> kases;
	
	for0(kase, kases) {
		
		cin >> n >> pd >> pg;
		if ((pg == 100 && pd != 100) || (pg == 0 && pd != 0)) {
			cout << "Case #" << (kase+1) << ": Broken" << endl;
		} else {
			bool broken = true;
			for (int i = 1; i <= n; i ++) for (int w = 0; w <= i; w ++) {
				if (i*pd == w * 100) {broken = false; break;}
			}
			if (broken)
			cout << "Case #" << (kase+1) << ": Broken" << endl;
			else
			cout << "Case #" << (kase+1) << ": Possible" << endl;
		}
	}
}