#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

void testcase(int tst)
{
	int time;
	ifs >> time;

	int na, nb;
	ifs >> na >> nb;

	vector<pair<PII,int> > a;

	REP(i, na+nb)
	{
		string sd, sa;
		ifs >> sd >> sa;
		
		int hd, md, ha, ma;
		sscanf(sd.c_str(), "%d:%d", &hd, &md);
		sscanf(sa.c_str(), "%d:%d", &ha, &ma);

		a.pb(mp(mp(hd*60+md, ha*60+ma),(i<na)?0:1));

	}

	sort(ALL(a));

	VI res(2, 0);
	VI c(2, 0);

	priority_queue<PII, vector<PII>, greater<PII> > q;

	REP(i, a.sz)
	{
		while (!q.empty() && q.top().fs <= a[i].fs.fs)
		{
			c[q.top().sc]++;
			q.pop();
		}
		if (c[a[i].sc] == 0) { c[a[i].sc]++; res[a[i].sc]++; }
		c[a[i].sc]--;
		q.push(mp(a[i].fs.sc+time,1-a[i].sc));
	}

	ofs << "Case #" << tst+1 << ": ";

	ofs << res[0] << ' ' << res[1] << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
