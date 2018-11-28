#include <iostream>

using namespace std;

int main(){
	int t; cin >> t;
	for (int zzz = 1; zzz <= t; zzz++){
		int n, k; cin >> n >> k;
		k %= (1 << n);
		if (k == (1 << n) - 1) cout << "Case #" << zzz << ": ON" << endl;
		else cout << "Case #" << zzz << ": OFF" << endl;	
	}

	return 0;
}
