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

int v[11000], t[11000], c[11000];
int cnt[11000][2];

int pmin(int a, int b) {
	if (a < 0) return b;
	if (b < 0) return a;
	return a<b?a:b;
}

int main()
{
	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	long long nc, m, tv;

	fin >> nc;

	for (int tc = 1; tc <= nc; ++tc)
	{
		fin >> m >> tv;

		REP(i,(m-1)/2) {
			fin >> t[i] >> c[i];
		}

		REP(i,(m+1)/2) {
			fin >> v[(m-1)/2+i];
			cnt[(m-1)/2+i][v[(m-1)/2+i]] = 0;
			cnt[(m-1)/2+i][1-v[(m-1)/2+i]] = -1;
		}

		for (int i = (m-1)/2-1; i >= 0; --i) {
			int c1 = 2*i+1, c2 = 2*i+2;
			if (t[i] == 1) {
				if (cnt[c1][1] < 0 || cnt[c2][1] < 0) cnt[i][1] = -1;
				else cnt[i][1] = cnt[c1][1] + cnt[c2][1];
				if (cnt[c1][0] < 0 && cnt[c2][0] < 0) cnt[i][0] = -1;
				else cnt[i][0] = pmin(cnt[c1][0], cnt[c2][0]);
			} else {
				if (cnt[c1][1] < 0 && cnt[c2][1] < 0) cnt[i][1] = -1;
				else cnt[i][1] = pmin(cnt[c1][1], cnt[c2][1]);
				if (cnt[c1][0] < 0 || cnt[c2][0] < 0) cnt[i][0] = -1;
				else cnt[i][0] = cnt[c1][0] + cnt[c2][0];
			}
			if (c[i]) {
				int a, b;
				if (t[i] != 1) {
					if (cnt[c1][1] < 0 || cnt[c2][1] < 0) a = -1;
					else a = cnt[c1][1] + cnt[c2][1];
					if (cnt[c1][0] < 0 && cnt[c2][0] < 0) b = -1;
					else b = pmin(cnt[c1][0], cnt[c2][0]);
				} else {
					if (cnt[c1][1] < 0 && cnt[c2][1] < 0) a = -1;
					else a = pmin(cnt[c1][1], cnt[c2][1]);
					if (cnt[c1][0] < 0 || cnt[c2][0] < 0) b = -1;
					else b = cnt[c1][0] + cnt[c2][0];
				}

				if ( (cnt[i][1] < 0 && a >= 0) ) {
					cnt[i][1] = a + 1;
				} else if (cnt[i][1] >= 0 && a >= 0 && a+1 < cnt[i][1])
					cnt[i][1] = a + 1;

				if ( (cnt[i][0] < 0 && b >= 0) ) {
					cnt[i][0] = b + 1;
				} else if (cnt[i][0] >= 0 && b >= 0 && b+1 < cnt[i][0])
					cnt[i][0] = b + 1;
			}
			
		}

		fout <<"Case #"<<tc<<": ";

		if (cnt[0][tv] < 0) fout << "IMPOSSIBLE" << endl;
		else fout << cnt[0][tv] << endl;

	}


	fin.close();
	fout.close();

	return 0;
}

