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

int p[30];
int k;
string s;
int res;

void check() {

	string sn = s;

	REP(i, s.sz / k) {

		int sj = i*k;

		for (int j = sj; j < sj + k; j++)
			sn[j] = s[sj+p[j-sj]];
	}

	int cnt = 0;
	REP(i, sn.sz) {
		if (i == 0 || sn[i] != sn[i-1])
			cnt++;
	}
	res = min(res, cnt);

}

void go(int v) {

	if (v == k) { check(); return; }

	REP(i, k) {

		bool found = false;
		
		REP(j, v)
			if (p[j] == i) { found = true; break; }

		p[v] = i;
		if (!found) go(v+1);

	}


}

void testcase(int tst)
{

	ifs >> k;
	ifs >> s;

	res = s.sz;

	go(0);


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
