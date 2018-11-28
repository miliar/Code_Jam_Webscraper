#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)


void solve_case(vector< string > & pict, int R, int C, ostream & out)
{
	FOR(i,R) {
		FOR(j,C) {
			if (pict[i][j] == '#')
				if (j+1 < C && pict[i][j+1] == '#' && i+1 < R && pict[i+1][j] == '#' && pict[i+1][j+1] == '#')
				{
					pict[i][j] = pict[i+1][j+1] = '/';
					pict[i][j+1] = pict[i+1][j] = '\\';
				}
				else
				{
					out << "Impossible\n";
					//FOR(i,R) {
					//	cerr << pict[i] << '\n';
					//}
					return;
				}
		}
	}
	FOR(i,R) {
		out << pict[i] << '\n';
	}
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int R, C;
		in >> R >> C;
		vector< string > pict;
		FOR(i,R) {
			string s;
			in >> s;
			assert(s.size() == C);
			pict.push_back(s);
		}
		out << "Case #" << t << ":\n";
		solve_case(pict, R, C, out);
	}
}


int main()
{
	//ifstream in("A-sample.in");
	//ofstream out("A-sample.txt");

	//ifstream in("A-small-attempt0.in");
	//ofstream out("A-small-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);

	return 0;
}