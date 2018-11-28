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

const string w = "welcome to code jam";
void testcase(int tst)
{
	string s;
	getline(ifs, s);
	
	VI count(w.sz, 0);

	REP(i, s.sz) {
		VI newcount(count);
		REP(j, w.sz) {
			if (s[i] == w[j]) {
				if (j)
					newcount[j] += count[j-1];
				else
					newcount[j] += 1;
				newcount[j] %= 10000;
			}
		}
		count = newcount;
	}

	char buf[50];
	sprintf(buf, "%d", count[w.sz-1]);

	string result = buf;
	while (result.sz < 4) {
		result = "0" + result;
	}

	ofs << "Case #" << tst+1 << ": " << result << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;

	string s;
	getline(ifs, s);
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
