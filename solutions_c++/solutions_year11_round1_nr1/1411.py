#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

bool solve() {
	int N, PD, PG;
	
	cin >> N >> PD >> PG;
	
	if (PD == 100 && PG == 100) return true;
	if (PD == 0 && PG == 0) return true;
	if (PD > 0 && PG == 0) return false;
	if (PD < 100 && PG == 100) return false;
	
	for (int d = 1; d <= N; ++d) {
		int dw = d * PD;
		if (dw % 100) continue;
		dw /= 100;
		for (int x = 0; ; ++x) {
			int xw = PG * x + PG * d - 100 * dw;
			//if (xw > (x - 1) * 100) break;
			//printf("(%d/%d) - (%d/%d)\n", dw, d, xw, x);
			if (xw > 9900) break;
			if (xw % 100 == 0 && xw >= 0) {
				//printf("(%d/%d) - (%d/%d)\n", dw, d, xw / 100, x);
				return true;
			}
		}
	}
	return false;
	
}
int main()
{
	int T;
	int N, PD, PG;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		if (solve() ) cout << "Possible";
		else cout << "Broken";
		cout << endl;
	}
	return 0;
}