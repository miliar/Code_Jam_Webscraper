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


double solve_case(vector<pair<int,int> > & BE, const vector<int> & w, int X, int S, int R, int t)
{
	sort(BE.begin(), BE.end());
	const size_t N = BE.size();
	assert(N == w.size());
	vector< pair<int,int> > dists; //speeds, dist;
	int prev = 0;
	FOR(i,N) {
		if (BE[i].first > prev)
			dists.push_back(make_pair(S, BE[i].first - prev));
		dists.push_back(make_pair(w[i] + S, BE[i].second - BE[i].first));
		prev = BE[i].second;
	}
	if (X > prev)
		dists.push_back(make_pair(S, X - prev));

	double remainingtime = t;
	double total = 0;
	sort(dists.begin(), dists.end());
	FOR(i,dists.size()) {
		if (remainingtime > 0) {
			int speed = dists[i].first + (R-S);
			if (speed*remainingtime >= dists[i].second) {
				double t1 = static_cast<double>(dists[i].second)/speed;
				total += t1;
				remainingtime -= t1;
			} else {
				double d2 = dists[i].second - speed*remainingtime;
				double t1 = d2/dists[i].first;
				total += remainingtime + t1;
				remainingtime = 0;
			}
		} else {
			double t1 = static_cast<double>(dists[i].second)/dists[i].first;
			total += t1;
		}
	}

	return total;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int X, S, R, runt, N;
		in >> X >> S >> R >> runt >> N;
		vector< pair<int,int> > BE(N);
		vector< int > w(N);
		FOR(i,N) {
			in >> BE[i].first >> BE[i].second >> w[i];
		}
		double result = solve_case(BE, w, X, S, R, runt);
		out << "Case #" << t << ": " << result << endl;
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