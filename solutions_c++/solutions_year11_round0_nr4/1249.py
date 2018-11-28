/*
ID: ahaigh1
PROG: 
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <memory>
#include <set>
#include <stack>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <limits>
#include <map>
#include <bitset>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
#define eps (1e-10)
#define inf (1<<30)
#define ll long long
#define MP make_pair

int t, n, x[1005], y[1005];
double r[1005], nCr[1005][1005];

double P(int n, int k) { return r[n-k] * nCr[n][k]; }
double expec(int x) { 
	//must memoize!!!!
	if (!x) return 0;
	
	double sum = 1;
	REP(i, x+1) if (i) sum += P(x, i) * expec(x - i);
	sum /= (1 - P(x, 0));
	
	//cout << x << " " << sum << endl;
	return sum;
}

int main() { 
	r[0] = 1; r[1] = 0;
	for(int i = 2; i < 1005; i++) r[i] = (double)(i-1)*(r[i-1] + r[i-2]);	
	
	nCr[0][0] = 1;
	for(int i = 1; i < 1005; i++)
		for (int j = 0; j <= i; j++) nCr[i][j] = (double)( ((j<i)?nCr[i-1][j]:0) + ((j>0)?nCr[i-1][j-1]:0) ) / i;
	
	//cout << P(2,0) << " " << P(2, 1) << " " << P(2, 2) << endl;	
	//cout << P(3,0) << " " << P(3, 1) << " " << P(3, 2) << " " << P(3, 3) << endl;

	cin >> t;
	REP(i, t) { 
		int unfix = 0;
		cin >> n;
		REP(j, n) { cin >> x[j]; if (x[j] != j+1) unfix++; }
		cout << "Case #" << (i+1) << ": " << expec(unfix) << endl;
	}
}