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


void solve_case(const vector< string > & games, ostream & out)
{
	size_t N = games.size();
	vector< vector< int > > WP(N, vector< int >(N, 0) ); //WP del team i es en i,i
	vector< vector< int > > P(N, vector< int >(N, 0) ); //WP del team i es en i,i, games played
	FOR(i,N)
	FOR(j,N)
	{
		if (games[i][j] == '1') { ++WP[i][i]; }
		if (games[i][j] != '.') { ++P[i][i]; }
	}
	FOR(i,N)
	FOR(j,N)
	{
		if (i != j) {
			if (games[i][j] == '1') { WP[i][j] = WP[i][i]-1; }
			else { WP[i][j] = WP[i][i]; }
			if (games[i][j] != '.') { P[i][j] = P[i][i]-1; }
			else { P[i][j] = P[i][i]; }
		}
		else assert(games[i][j] == '.');
	}
#if 0
	FOR(i,N) {
		FOR(j,N)
			cerr << WP[i][j] << ' ';
		cerr << '\n';
	}
	FOR(i,N) {
		FOR(j,N)
			cerr << P[i][j] << ' ';
		cerr << '\n';
	}
#endif
	vector< double > OWP(N, 0.0);
	vector< int > op(N, 0);
	FOR(i,N) {
		FOR(j,N)
			if (games[i][j] != '.') {
				OWP[i] += static_cast<double>(WP[j][i])/P[j][i];
				++op[i];
			}
		OWP[i] /= op[i];
	}
	vector< double > OOWP(N, 0.0);
	FOR(i,N) {
		FOR(j,N)
			if (games[i][j] != '.')
				OOWP[i] += OWP[j];
		OOWP[i] /= op[i];
	}
	out.precision(12);
	FOR(i,N) {
		double RPI = 0.25 * static_cast<double>(WP[i][i])/P[i][i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		out << RPI << '\n';
	}
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int N;
		in >> N;
		vector< string > games;
		FOR(i,N) {
			string s;
			in >> s;
			assert(s.size() == N);
			games.push_back(s);
		}
		out << "Case #" << t << ":\n";
		solve_case(games, out);
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