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

int n;
int m;
string s;

void testcase(int tst)
{
	int a, b;
	ifs >> a >> b;

	int num[10];

	int res = 0;
	for (int i = a; i <= b; i++) {
		
		int j = i;
		int n = 0;
		while (j > 0) {
			num[n] = j % 10;
			j /= 10;
			n++;
		}

		VI was;
		
		for (int j = 0; j < n-1; j++) {
			int d = 1;
			int k = 0;
			if (num[j] > 0) {
				for (int l = j+1; l < n; l++) {
					k += num[l] * d;
					d *= 10;
				}
				for (int l = 0; l <= j; l++) {
					k += num[l] * d;
					d *= 10;
				}
				if (k >= a && k <= b && k > i && find(ALL(was), k) == was.end()) {
					res++;
					was.pb(k);
				}
			}
		}
	}

	ofs << "Case #" << tst+1 << ": " << res << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
