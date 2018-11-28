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

void testcase(int tst)
{
	int n;
	ifs >> n;

	vector<char> hall(n);
	VI pos(n);
	REP(i, n) {
		ifs >> hall[i] >> pos[i];
	}

	int time = 0;

	int v1 = 1;
	int v2 = 1;
	int j = 0;
	while (j < n) {
		
		int to1 = v1, to2 = v2;
		for (int k = j; k < n; k++)
			if (hall[k] == 'O') {
				to1 = pos[k];
				break;
			}
		for (int k = j; k < n; k++)
			if (hall[k] == 'B') {
				to2 = pos[k];
				break;
			}

		int d1 = abs(v1-to1);
		int d2 = abs(v2-to2);
		
		if (hall[j] == 'O') {
			time += d1 + 1;
			v1 = to1;
			if (d2 <= d1 + 1) v2 = to2; else if (v2 < to2) v2 += d1+1; else v2 -= d1+1;
		} else {
			time += d2 + 1;
			v2 = to2;
			if (d1 <= d2 + 1) v1 = to1; else if (v1 < to1) v1 += d2+1; else v1 -= d2+1;
		}

		j++;
	}

	ofs << "Case #" << tst+1 << ": " << time << endl;
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
