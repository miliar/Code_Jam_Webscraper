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
const int inf = 0x3fffffff;

struct painter {
	painter(int a, int b, int cc) { s = a; e = b; c = cc; }
	int s, e, c;
};

bool operator<(painter &a, painter &b) {
	if (a.s != b.s) return a.s<b.s;
	return a.e > b.e;
}

int best;
int nclr;
vi colors;
vector <painter> p;

void validate()
{
	//REP(i,colors.size()) cout << colors[i] << " ";
	//cout << endl;
	int next = 1, npaint = p.size();
	int cnt = 0, far;
	int i = 0;
	while (i < npaint) {
		far = next - 1;
		while (i < npaint && p[i].s <= next) {
			bool can = false;
			REP(j,colors.size()) can = can || (p[i].c == colors[j]);
			if (can) {
				far = max(far, p[i].e);
			}
			++i;
		}
		if (far < next) return;
		next = far + 1;
		++cnt;
		if (next > 10000) break;
	}

	if (next > 10000)
		best = min(best, cnt);
}

void generate(int pos, int cnt) {
	if (cnt > 3) return;
	if (pos == nclr) {
		if (cnt > 0)
			validate();
		return;
	}
	generate(pos+1, cnt);
	colors.push_back(pos);
	generate(pos+1, cnt+1);
	colors.pop_back();
}

int main()
{
	//ifstream fin("B-small.in");
	//ofstream fout("B-small.out");
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	long long nc;

	map <string, int> m;

	fin >> nc;

	for (int tc = 1; tc <= nc; ++tc)
	{
		fout <<"Case #"<<tc<<": ";
		int n, s, e;
		string str;
		nclr = 0;

		p.clear();
		m.clear();

		fin >> n;

		REP(i,n) {
			fin >> str >> s >> e;
			int id = -1;
			if (m.find(str) == m.end())
				m[str] = nclr++;
			id = m[str];
			p.push_back(painter(s, e, id));
		}

		sort(p.begin(), p.end());

		colors.clear();
		best = inf;
		generate(0, 0);

		if (best == inf)
			fout << "IMPOSSIBLE" << endl;
		else
			fout << best << endl;

		//cout << "@@" << endl;

	}

	fin.close();
	fout.close();

	return 0;
}

