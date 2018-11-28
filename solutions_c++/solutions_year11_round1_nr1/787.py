#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>

#include <iostream>
#include <fstream>

#include <set>
#include <map>
#include <stack>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
	if (a < b) swap(a, b);
	while (a%b != 0) {
		a = a%b;
		if (a == 0) break;
		swap(a, b);
	}
	return b;
}

int main(int argc, char* argv[]) {

	ifstream fp;
	fp.open(argv[1]);
	int T;
	fp >> T;
	for (int t=0; t<T; t++) {
		long long N;
		int PD, PG;
		fp >> N >> PD >> PG;
		bool poss = true;
		if (PG == 100 && PD == 100)  { poss = true; }
		else if (PG == 100 && PD < 100) { poss = false; }
		else if (PD == 0 && PG == 0) { poss = true; }
		else if (PG == 0 && PD > 0) { poss = false; }
		else {
			int minD = 100/gcd(PD, 100);
			if (minD > N) { poss = false; }
			else poss = true;		
		}
		cout << "Case #" << t+1 << ": ";
		if (poss) cout << "Possible"; 
		else cout << "Broken";
		cout << endl; 
	}
	fp.close();
}
