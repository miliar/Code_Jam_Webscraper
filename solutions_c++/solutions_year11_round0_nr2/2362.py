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
	int c, r, n;
	ifs >> c;

	VS comb(c);
	REP(i, c)
		ifs >> comb[i];

	ifs >> r;

	VS opp(r);
	REP(i, r)
		ifs >> opp[i];

	ifs >> n;
	string s;
	ifs >> s;

	string cur = "";
	REP(i, n) {
		
		cur += s[i];

		if (cur.sz > 1) {
			char c1 = cur[cur.sz-1];
			char c2 = cur[cur.sz-2];
			bool combined = false;
			REP(j, c)
				if ((comb[j][0] == c1 && comb[j][1] == c2) ||
					(comb[j][0] == c2 && comb[j][1] == c1)) {
						combined = true;
						cur = cur.substr(0, cur.sz-2);
						cur += comb[j][2];
						break;
					}
			if (combined) continue;
		}

		REP(j, cur.sz-1) {

			char c1 = cur[cur.sz-1];
			char c2 = cur[j];
			bool opposed = false;
			REP(k, r)
				if ((opp[k][0] == c1 && opp[k][1] == c2) ||
					(opp[k][0] == c2 && opp[k][1] == c1)) {
						opposed = true;
				}
			if (opposed) {
				cur = "";
				break;
			}
		}

	}

	ofs << "Case #" << tst+1 << ": ";

	ofs << "[";
	if (cur.sz > 0) ofs << cur[0];

	for (int i = 1; i < cur.sz; i++) {
		ofs << ", " << cur[i];
	}
		
	ofs << "]";
	ofs << endl;
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
