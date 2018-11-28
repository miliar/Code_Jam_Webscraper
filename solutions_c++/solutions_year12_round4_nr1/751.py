#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a) 

int main() 
{
	//ifstream fin("A-small-attempt2.in");
	ifstream fin("A-large.in");
	//ifstream fin("A.in");
	ofstream fout("A.out");

	int tc;
	vector <pair<int,int> > v;
	int n, d;
	int bh[10000];

	fin >> tc;

	REP(tcase,tc) {
		fin >> n;

		v.resize(n);
		REP(i,n) {
			fin >> v[i].first >> v[i].second;
		}

		fin >> d;

		int pos = 0, h = v[0].second,  nh;
		bool ok = false;

		memset(bh, 0, sizeof(bh));
		bh[0] = min(v[0].second, v[0].first);

		for (pos = 0; pos < n; ++pos) {
			int newpos = pos+1;
			h = bh[pos];
			while (newpos < n && v[newpos].first - v[pos].first <= h) {
				nh = min(v[newpos].second, v[newpos].first-v[pos].first);
				if (bh[newpos] < nh)
					bh[newpos] = nh;
				++newpos;
			}

			if (v[pos].first+h >= d) ok = true;
		}

		fout << "Case #" << tcase+1 << ": ";
		cerr << tcase << endl;
		if (ok) fout << "YES" << endl;
		else fout << "NO" << endl;
	}

	fout.close();

	return 0;
}