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


int main()
{
	int t, n;
	string m[100], s;

	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	fin >> t;

	REP(tc,t) {
		fout <<"Case #"<<tc+1<<": ";	

		fin >> n;

		REP(i,n) fin >> m[i];

		int res = 0;

		REP(i,n) FOR(j,i,n) {
			bool ok = true;
			FOR(k,i+1,n) if (m[j][k] == '1') ok = false;
			if (ok) {
				res += j-i;
				s = m[j];
				for (int k = j-1; k >= i; --k) m[k+1] = m[k];
				m[i] = s;
				break;
			}
		}

		fout << res << endl;

	}

	fin.close();
	fout.close();

	return 0;
}

