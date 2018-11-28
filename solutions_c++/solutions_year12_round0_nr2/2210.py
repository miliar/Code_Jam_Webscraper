#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <map>
using namespace std;

#define REP(i,n) for(int i=0; i < (n); i++)
#define REP2(i,s,n) for(int i=(s); i < (n); i++)

int main()
{
	int TESTCASES; cin >> TESTCASES;
	for (int CASE = 1; CASE <= TESTCASES; CASE++)
	{
		int N, S, p; cin >> N >> S >> p;
		int r = 0;
		
		REP(i, N) {
			int k; cin >> k;
			if (p == 0) { r++; }
			else if (p == 1) { 
				if (k >= 1) r++;
			} else {
				if (k >= p*3 - 2) r++;
				else if (k >= p*3 - 4 && S > 0) { S--; r++; }
			}
		}
		
		cout << "Case #" << CASE << ": " << r << endl;
	}

	return 0;
}