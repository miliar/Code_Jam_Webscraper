#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a) 

bool cmp(pair<int,int> a, pair <int,int> b)
{
	if (a.second == b.second) return a.first > b.first;
	return a.second < b.second;
}

int main() 
{
	ifstream fin("a.in");
	ofstream fout("a.out");

	int tc;
	int x, s, r, t, n, last;
	vector <pair<int,int> > a;

	int is, ie, iv;

	fin >> tc;

	REP(tcase,tc) {
		fin >> x >> s >> r >> t >> n;

		a.clear();

		last = 0;
		REP(i,n) {
			fin >> is >> ie >> iv;
			if (last < is) {
				a.push_back(make_pair(is-last, s));
			}
			a.push_back(make_pair(ie-is, s+iv));
			last = ie;
		}

		if (last < x) a.push_back(make_pair(x-last, s));

		sort(a.begin(), a.end(), cmp);

		double tleft = t, res = 0, tfull;

		REP (i,a.size()) {
			if (tleft < 0) {
				res += a[i].first/(double)a[i].second;
				continue;
			}
			tfull = a[i].first/(double)(a[i].second-s+r);
			if (tfull < tleft) {
				res += tfull;
				tleft -= tfull;
			} else {
				res += tleft + (a[i].first-tleft*(a[i].second-s+r))/(double)a[i].second;
				tleft = -1;
			}
		}


		fout.precision(10);
		fout << "Case #" << tcase+1 << ": " << fixed << res << endl;
		cout << t+1 << " / " << tc << endl;
	}

	fout.close();

	return 0;
}