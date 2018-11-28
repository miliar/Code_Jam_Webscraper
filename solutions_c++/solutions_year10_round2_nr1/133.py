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
	int n, m;

	set<string> was;

	ifs >> n >> m;
	REP(i, n) {
		string s;
		ifs >> s;
		was.insert(s);
	}
	
	int res = 0;

	REP(i, m) {

		string s;
		ifs >> s;
		
		string curs = "";
		REP(j, s.sz) {
			if (j > 0 && s[j] == '/') {
				if (was.find(curs) == was.end()) {
					res++;
					was.insert(curs);
				}
			}
			curs += s[j];
		}
		if (was.find(curs) == was.end()) {
			res++;
			was.insert(curs);
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
