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

	int s, q;
	
	ifs >> s;

	string si;
	getline(ifs, si);

	VS as(s);

	REP(i, s)
		getline(ifs, as[i]);

	ifs >> q;
	getline(ifs, si);
	
	VS aq(q);
	REP(i, q)
		getline(ifs, aq[i]);

	VI or(s, 0);

	VVI eq(q, VI(s, 0));
	REP(i, q)
		REP(j, s)
			eq[i][j] = aq[i] == as[j];

	REP(i, q)
	{
		VI nr(s, 2000);

		REP(j, s)
		{
			if (eq[i][j]) continue;
			REP(l, s)
				nr[j] = min(nr[j], or[l]+((j==l)?0:1));

		}

		or = nr;
	}



	ofs << "Case #" << tst+1 << ": ";

	int res = 2000;
	REP(j, s)
		res = min(res, or[j]);

	ofs << res << endl;
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
