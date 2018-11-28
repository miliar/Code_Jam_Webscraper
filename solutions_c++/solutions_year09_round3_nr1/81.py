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

#define DEFLENGTH 5
#define DEFBASE 100000

void normalize(VI& a) {

	REP(i, a.sz) {
		if (a[i] >= DEFBASE) {
			if (i + 1 >= a.sz)
				a.pb(a[i]/DEFBASE);
			else
				a[i+1] += a[i]/DEFBASE;
			a[i] %= DEFBASE;
		}
	}
}

void mult(VI& a, int k) {

	REP(i, a.sz) {
		a[i] *= k;
	}

	normalize(a);
}

void add(VI& a, VI& b) {

	a.resize(max(a.sz, b.sz), 0);
	
	REP(i, b.sz)
		a[i] += b[i];

	normalize(a);
}

void testcase(int tst)
{
	string s;
	ifs >> s;

	int n = s.length();

	set<char> letters;

	REP(i, s.length())
		letters.insert(s[i]);

	int base = letters.size();
	if (base < 2) base = 2;

	map<char, int> mp;

	VI t(n, 0);
	VI was(base, 0);

	REP(i, n) {
		if (mp.find(s[i]) == mp.end()) {
			REP(j, base) {
				if (i == 0 && j == 0) continue;
				if (was[j]) continue;
				mp[s[i]] = j;
				was[j] = 1;
				break;
			}
		}
		t[i] = mp[s[i]];
	}

	reverse(ALL(t));

	VI res(1, 0);
	VI coeff(1, 1);

	REP(i, n) {
		VI b = coeff;
		mult(b, t[i]);
		add(res, b);
		mult(coeff, base);
	}

	reverse(ALL(res));

	string sres = "";
	REP(i, res.sz) {

		string cr;

		char buf[50];
		sprintf(buf, "%d", res[i]);
		cr = buf;
		
		if (i) {
			while (cr.sz < DEFLENGTH) {
				cr = "0" + cr;
			}
		}

		sres += cr;
	}
	ofs << "Case #" << tst+1 << ": " << sres << endl;

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
