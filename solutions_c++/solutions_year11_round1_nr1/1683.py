#include <stdio.h>
#include <iostream>
#include <fstream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>
#include <climits>

using namespace std;

int main(int argc, char* argv[]) {
	fstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}
	string ln; 
	inf >> ln;
	int caseNum = atoi(ln.c_str());
	for (int cn = 0; cn<caseNum; cn++) {
		/*
		if (cn == 94)
			printf("houzhe");
		*/

		inf >> ln;
		int N = atoi(ln.c_str());
		inf >> ln;
		int PD = atoi(ln.c_str());
		inf >> ln;
		int PG = atoi(ln.c_str());
		bool possible = false;
		int RY, RYW, RX;
		for (int x=1; x<=N; x++) {
			int YW = 0; 
			int xx = PD * x / 100 * 100;
			int yy = PD * x; 
			if (PD * x / 100 * 100 != PD * x) 
				continue;
			RX = x;
			while ((100*YW + (PD - PG)*x) < 0) {
				YW++;
			}
			if (PG == 0) {
				if (PD == 0)
					possible = true;
				else 
					possible = false;
			}
			for (int i=0; (!possible) && (i<PG); i++) {
				int TYW = YW + i;
				for (int Y=TYW; PG*Y <= 100*TYW + (PD - PG)*x; Y++) {
					if (PG*Y == 100*TYW + (PD -PG)*x) {
						possible = true;
						RY = Y;
						RYW = TYW;
						break;
					}
				}
				if (possible) break;
			}
			if (possible) break;
		}
		if (possible)
			// cout << "Case #" << cn+1 << ": Possible " << RY << " " << RYW << " " << RX << endl;
			cout << "Case #" << cn+1 << ": Possible " << endl;
		else
			cout << "Case #" << cn+1 << ": Broken" << endl;
	}
	return 0; 
}