

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <math.h>
using namespace std;

int main(int argc, const char * argv[])
{
	ifstream ifs( "input.txt" );
	int T;
	ifs >> T;
	for (int i = 0; i < T; i++) {
		int a,b;
		ifs >> a >> b;
		
		int nd = log10(a) + 1;
		int ans = 0;
		set<pair<int, int> > ansset;
		for (int p = 1; p <= nd; p++) {
			int dec = pow(10, p);
			int compdec = pow(10, nd-p);
			for (int n = a; n <= b; n++) {
				int m = n/dec + n%dec*compdec;
				if (a <= m && m <= b && m != n && n < m) {
					ans++;
					ansset.insert(pair<int, int>(n,m));
				}
			}
		}
		
		cout << "Case #" << i+1 << ": " << ansset.size() << endl;
	}
    return 0;
}

