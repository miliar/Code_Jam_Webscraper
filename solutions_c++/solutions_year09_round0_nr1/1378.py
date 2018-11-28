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

char m[20][256];

int main()
{
	int l, d, n;
	string s;
	vector <string> dic;

	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	fin >> l >> d >> n;

	REP(i,d) {
		fin >> s;
		dic.push_back(s);
	}

	REP(i,n) {
		fout <<"Case #"<<i+1<<": ";	
		fin >> s;
		memset(m, 0, sizeof(m));
		int j = 0, k = 0;
		while (j < s.size()) {
			if (s[j] == '(') {
				++j;
				while (s[j] != ')') {
					m[k][s[j]] = 1;
					++j;
				}
				++k;
			} else {
				m[k++][s[j]] = 1;
			}
			++j;
		}

		int cnt = 0;

		REP(j,d) {
			bool ok = true;
			REP (k,l) {
				ok = ok && m[k][dic[j][k]];
			}
			if (ok) ++cnt;
		}

		fout << cnt << endl;
	}

	fin.close();
	fout.close();

	return 0;
}

