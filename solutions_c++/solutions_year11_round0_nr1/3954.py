#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
	int i, j, k, n, t, mov, turn, d, mo, mb, lo, lb;
	char c;
	
	cin >> t;
	for (k=0; k<t; k++) {
		mb=1;
		mo=1;
		lb=0;
		lo=0;
		mov=0;
		cin >> n;
		for (i=0; i<n; i++) {
			cin >> c >> d;
			if (c=='O') {
				turn=max(abs(mo-d)-lo,0)+1;
				mo=d;
				lo=0;
				lb+=turn;
				mov+=turn;
			}
			if (c=='B') {
				turn=max(abs(mb-d)-lb,0)+1;
				mb=d;
				lb=0;
				lo+=turn;
				mov+=turn;
			}
		}
		cout << "Case #" << k+1 << ": " << mov << endl;
	}
	return 0;
}
