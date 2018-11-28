#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)


int solve_case(size_t N, vector<int> & A, vector<int> & B)
{
	vector< pair<int,int> > AB(N);
	FOR(i,N)
		AB[i] = make_pair(A[i],B[i]);
	sort(AB.begin(), AB.end());
	int result = 0;
	FOR(i,N)
		for(size_t j = i+1; j < N; ++j)
			if (AB[i].second > AB[j].second)
				++result;
	return result;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		size_t N;
		in >> N;
		vector<int> A(N),B(N);
		FOR(i,N)
			in >> A[i] >> B[i];
		int result = solve_case(N,A,B);
		out << "Case #" << t << ": " << result << "\n";
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