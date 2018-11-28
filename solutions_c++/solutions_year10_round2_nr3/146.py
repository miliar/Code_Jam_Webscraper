#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

int C[512][512];

int was[512][512];

int calculate(int n, int k) {

	if (k >= n) return 0;
	if (n == 1) return 1;
	if (k == 1) return 1;

	int& res = was[n][k];
	if (res > -1) return res;
	res = 0;

	for (int l = 1; l <= k-1; l++) {
		ll cr = ((ll)C[n-k-1][k-l-1])*calculate(k,l);
		res = (cr + res) % 100003;
	}

	return res;
}

void testcase(int tst)
{
	int n;
	ifs >> n;

	int res = 0;
	for (int k = 1; k < n; k++)
		res = (res + calculate(n, k)) % 100003;

	ofs << "Case #" << tst+1 << ": " << res << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	REP(i, 512) {
		C[0][i] = 0;
		C[i][0] = 1;
	}

	for (int n = 1; n < 512; n++)
		for (int k = 1; k < 512; k++) {
			C[n][k] = (C[n-1][k-1] + C[n-1][k]) % 100003;
		}

	memset(was, -1, sizeof(was));

	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
