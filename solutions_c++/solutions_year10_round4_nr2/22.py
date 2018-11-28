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
int p;
int m[1024];
int a[1024][1024];

int was[16][1024][1024];

const int MAXNUM = 1000000000;

int go(int count, int row, int col) {

	if (row == p) {
		if (p - count > m[col]) 
			return MAXNUM;
		else
			return 0;
	}

	int& res = was[count][row][col];
	if (res > -1) return res;

	res = min(go(count, row+1, 2*col) + go(count, row+1, 2*col+1), a[row][col] + go(count+1, row+1, 2*col) + go(count+1, row+1, 2*col+1));
	res = min(res, MAXNUM);
	return res;
}

void testcase(int tst)
{
	ifs >> p;

	n = (1 << p);

	REP(i, n)
		ifs >> m[i];

	REP(i, p) {
		REP(j, (1 << (p-i-1)))
			ifs >> a[p-i-1][j]; 
	}

	memset(was, -1, sizeof(was));

	ofs << "Case #" << tst+1 << ": " << go(0, 0, 0) << endl;
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
