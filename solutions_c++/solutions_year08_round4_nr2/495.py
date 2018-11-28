#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

#include <cmath>

//#include "lib.hpp"

typedef unsigned long long ULL;
typedef long long LL;

using namespace std;

int main(void)
{
	int n;
	cin >> n;
	for(ULL nn = 0; nn < n; ++nn) {

		LL N,M,A;
		cin >> N >> M >> A;

		if(A > N*M) {
			cout << "Case #" << nn+1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			LL x0, y0, x1, y1;
			bool solved = false;
			for(int i = 1; i<(N+1)*(M+1); ++i) {
				for(int j = i+1; j < (N+1)*(M+1); ++j) {
					y0 = i/(N+1);
					x0 = i%(N+1);
					y1 = j/(N+1);
					x1 = j%(N+1);
					LL t = x0 * y1 - x1 * y0;
					if(t == A || t == -A) {
						solved = true;
						break;
					}
				}
				if(solved) break;
			}
			if(solved) {
				cout << "Case #" << nn+1 << ": " << 0 << ' ' << 0 << ' ' << x0 << ' ' <<  y0 << ' ' << x1 << ' ' << y1 << endl;
			} else {
				cout << "Case #" << nn+1 << ": " << "IMPOSSIBLE" << endl;
			}
		}
	}
	
	return 0;
}
