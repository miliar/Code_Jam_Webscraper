#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(long long a=0;a<(b);++a)
#define FOR(a,c,b) for(long long  a=c;a<(b);++a)

string ch[100];
int m[1<<11][20];
int nr, nc;

int count(int msk, int r);

void generate(int pos, bool last, int cmsk, int cr, int nmsk) {
	if (pos == nc) {
		int cnt = count(nmsk, cr+1);
		int bits = 0;
		REP(i,nc) {
			if (nmsk&(1<<i)) ++ bits;
		}
		if (m[cmsk][cr] < bits + cnt) m[cmsk][cr] = bits + cnt;
	} else {
		if (ch[cr-1][pos] == 'x') generate(pos+1, false, cmsk, cr, nmsk);
		else if (last) generate(pos+1, false, cmsk, cr, nmsk);
		else {
			bool can = true;
			if (pos > 0 && (cmsk&(1<<(pos-1))) ) can = false;
			if (pos < nc-1 && (cmsk&(1<<(pos+1))) ) can = false;
			if (can) {
				generate(pos+1, true, cmsk, cr, nmsk|(1<<pos));
			}
			generate(pos+1, false, cmsk, cr, nmsk);			
		}
	}
}

int count(int msk, int r)
{
	if (r > nr) return 0;
	if (m[msk][r] < 0) {
		m[msk][r] = 0;
		generate(0, false, msk, r, 0);
	}

	return m[msk][r];
}

int main()
{
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	//ifstream fin("C-large.in");
	//ofstream fout("C-large.out");

	long long ncc, mm, n;

	fin >> ncc;

	for (int tc = 1; tc <= ncc; ++tc)
	{
		fout <<"Case #"<<tc<<": ";	
		fin >> mm >> n;
		REP(i,mm) fin >> ch[i];
		nr = mm; nc = n;
		memset(m, -1, sizeof(m));
		fout << count(0,1) << endl;

	}

	fin.close();
	fout.close();

	return 0;
}

