//should be knapsack for large
#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <vector>
#include <deque>
using namespace std;

#define db(x) cout << #x << " = " << x << endl;
#define rep(i,n) for (int i=0, j=n; i < j; i++)

const int MAX_VALUES_POSSIBLE = (int) (10e6 + 10);

int main () {
	ifstream fin ("C.in");
	ofstream fout ("output.txt");
	
	int nCases;
	fin >> nCases;
	rep (ij, nCases) {
		int nCandies;
		fin >> nCandies;
		
		vector <int> values;
		rep (i, nCandies) {
			int v1;
			fin >> v1;
			values.push_back (v1);
		}
		int ans = -1;
		//brute force time (nonempty)
		for (int i=1; i < ((1 << nCandies) - 1 ); i++) {
			int oneNum = 0;
			int zeroNum = 0;
			
			int oneSum = 0;
			int zeroSum = 0;
			
			for (int j = 0; j < nCandies; j++) {
				int v1 = values [j];
				if ( (1 << j) & i ) {
					oneNum = (oneNum | v1) - (oneNum & v1);
					oneSum += v1;
				} else {
					zeroNum = (zeroNum | v1) - (zeroNum & v1);
					zeroSum += v1;
				}
			}
			if (oneNum == zeroNum) {
				ans = max (ans, max (oneSum, zeroSum));
			}
		}
		fout << "Case #" << ij + 1 << ": ";
		if (ans == -1) fout << "NO";
		else fout << ans;
		fout << endl;
	}
	cout << "Done" << endl;
	int z;
	cin >> z;
	return 0;
}
