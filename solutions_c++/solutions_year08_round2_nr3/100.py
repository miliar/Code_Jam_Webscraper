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
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	//ifstream fin("C-large.in");
	//ofstream fout("C-large.out");

	int t, n, k;

	fin >> t;

	for (int tc = 1; tc <= t; ++tc)
	{
		fin >> k >> n;
		vi q(n);
		REP(i,n) fin >> q[i];

		vi d(k,0), res(n);
		int left = k, pos = 0;

		REP(i,k) {
			int diff = i%left;
			while (diff > 0) {
				if (d[pos] == 0) --diff;
				pos = (pos+1)%k;
			}
			while (d[pos] != 0) pos = (pos+1)%k;
			d[pos] = i+1;
		}
		
		fout << "Case #" << tc << ":";
		REP(i,n) fout << " " << d[q[i]-1];
		fout << endl;

	}



	fin.close();
	fout.close();

	return 0;
}

