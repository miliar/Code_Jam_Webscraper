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
#define FOR(a,c,b) for(int a=c;a<(b);++a)


int main()
{
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	//ifstream fin("B-large.in");
	//ofstream fout("B-large.out");

	long long nc, n, m, s;

	fin >> nc;

	for (int tc = 1; tc <= nc; ++tc)
	{
		fin >> n >> m >> s;

		fout <<"Case #"<<tc<<": ";

		REP(a,n+1) REP(b,m+1) FOR(c,0,n+1-a) FOR(d,-b,m+1-b) {
			long long ts = b*c - a*d;
			if (ts == s) {
				fout << "0 0 " << a << " " << b << " " << a+c << " " << b+d << endl;
				goto end;
			}
		}
		fout << "IMPOSSIBLE" << endl;

end:;

	}


	fin.close();
	fout.close();

	return 0;
}

