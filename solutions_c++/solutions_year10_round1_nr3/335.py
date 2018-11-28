#include <iostream>
#include <fstream>

using namespace std;

int GCD(int a, int b);

int main() {
	ofstream out("c.out");
	int T;
	cin >> T;
	for (int nth = 1; nth <= T; nth++) {
		int a1, a2, b1, b2;
		int ret = 0;
		cin >> a1 >> a2 >> b1 >> b2;
		for (int a = min(a1, a2); a <= max(a1, a2); a++) {
			for (int b = min(b1,b2); b <= max(b1,b2); b++) {
/*				int gcd = GCD(a, b);
				int ta = max(a, b), tb = min(a, b);
				int tmp;
				while (tb) {
					tmp = ta;
					ta = tb;
					tb = tmp%tb;
					if (tb == gcd) {
						break;
					}
				}
				if (ta%2) ret++;*/
				bool turn = true;
				int maxval = max(a, b), minval = min(a, b);
				int tmp;
				if (minval == maxval) continue;
				while (maxval / minval == 1) {
					minval;
					maxval = maxval - minval;
					tmp = maxval;
					maxval = max(maxval, minval);
					minval = min(tmp, minval);
					turn = !turn;
				}
				if (turn) ret++;
			}
		}
		out << "Case #" << nth << ": "<< ret << endl;
	}
	out.close();
}
/*
int GCD(int a, int b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}*/
