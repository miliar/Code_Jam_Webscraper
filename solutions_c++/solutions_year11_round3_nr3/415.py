#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int n, l, h;

int fs[105];

int main() {
	
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> n >> l >> h;
		
		for0(i, n) cin >> fs[i];
		
		int freq = -1;
		
		for (int f = l; f <= h; f ++) {
			bool works = true;
			for0(i, n) {
				if (!(fs[i] % f == 0 || f % fs[i] == 0)) {
					works = false;
				}
			}
			if (works) {freq = f; break;}
		}
		
		
		cout << "Case #" << (kase+1) << ": ";
		if (freq < 0) cout << "NO" << endl;
		else cout << freq << endl;
	}
}