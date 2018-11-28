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
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a)


int main()
{
	ifstream fin("D-small.in");
	ofstream fout("D-small.out");
	//ifstream fin("D-large.in");
	//ofstream fout("D-large.out");

	long long nc;

	fin >> nc;

	for (int tc = 1; tc <= nc; ++tc)
	{
		int k, best = 999999999;
		string st;

		fin >> k >> st;

		vi p;
		REP(i,k) p.push_back(i);

		do {
			string s = st;
			REP(i,k) {
				int ix = 0;
				while (ix < s.size()) {
					s[ix+i] = st[ix+p[i]];
					ix += k;
				}
			}

			int pos = 0, cnt = 0;
			do {
				while (pos+1 < s.size() && s[pos] == s[pos+1]) ++pos;
				++pos; ++cnt;
			} while (pos < s.size());

			if (cnt < best) best = cnt;
		} while (next_permutation(p.begin(), p.end()));

		fout <<"Case #"<<tc<<": ";
		fout <<best <<endl;

	}


	fin.close();
	fout.close();

	return 0;
}

