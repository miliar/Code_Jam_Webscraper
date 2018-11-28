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


int solve_case(const vector<int> & candy)
{
	int min = 1000000000;
	int sum = 0;
	int xo = 0;
	FOR(i,candy.size()) {
		assert(candy[i] <= 1000000);
		sum += candy[i];
		xo = xo ^ candy[i];
		if (candy[i] < min) min = candy[i];
	}
	assert(min >= 1);
	if (xo == 0)
		return sum - min;
	else 
		return -1;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int N;
		in >> N;
		vector<int> candy(N);
		FOR(i,N)
			in >> candy[i];
		int result = solve_case(candy);
		if (result < 0)
			out << "Case #" << t << ": " << "NO" << "\n";
		else
			out << "Case #" << t << ": " << result << "\n";
	}
}


int main()
{
	//ifstream in("C-sample.in");
	//ofstream out("C-sample.txt");

	//ifstream in("C-small-attempt0.in");
	//ofstream out("C-small-out.txt");

	ifstream in("C-large.in");
	ofstream out("C-large-out.txt");

	solve(in,out);

	return 0;
}