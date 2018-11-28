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
	int t, n, tc;
	double x[5], y[5], r[5];

	ifstream fin("D-small.in");
	ofstream fout("D-small.out");
	//ifstream fin("D-large.in");
	//ofstream fout("D-large.out");

	fin >> t;

	REP(tc,t) {
		fout <<"Case #"<<tc+1<<": ";

		fin >> n;

		REP(i,n) {
			fin >> x[i] >> y[i] >> r[i];
		}

		
		if (n == 1) {
			printf("%.12lf\n", r[0]);
			fout.precision(16);
			fout << r[0] << endl;
		} else if (n == 2) {
			printf("%.12lf\n", max(r[0],r[1]));
			fout.precision(16);
			fout << max(r[0],r[1]) << endl;
		} else {
			double best = 1e20;
			REP(i,3) FOR(j,i+1,3) {
				int k = 0;
				while (k == i || k == j) ++k;

				double dst = sqrt( (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) );
				best = min(best, max(dst+r[i]+r[j],r[k]));
			}

			printf("%.12lf\n", best);
			fout.precision(16);
			fout << best/2. << endl;
		}



	}

	fin.close();
	fout.close();

	return 0;
}

