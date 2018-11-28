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

__int64 pw(__int64 a, __int64 b)
{
	__int64 r = 1;
	FOR(i,b)
		r *= a;
	return r;
}

int solve_case(__int64 L, __int64 P, __int64 C)
{
	int q = 0; __int64 LCq = L;
	while (LCq*C < P)
	{
		LCq *= C;
		++q;
	}
//	assert(q==0 && L*C >=P || q > 0 && L*pow(static_cast<int>(C),static_cast<int>(q-1)) < P && L*pow(static_cast<int>(C),static_cast<int>(q)) >= P);
//	assert(L*pow(static_cast<int>(C),static_cast<int>(q)) < P && L*pow(static_cast<int>(C),static_cast<int>(q+1)) >= P);
	assert(L*pw(C,q) < P && L*pw(C,q+1) >= P);
	int result = 0;
	while (q != 0) {
		++result;
		q >>= 1;
	}
	return result;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int L, P; int C;
		in >> L >> P >> C;
		int result = solve_case(L,P,C);
		out << "Case #" << t << ": " << result << "\n";
	}
}


int main()
{
	//ifstream in("B-sample.in");
	//ofstream out("B-sample.txt");

	//ifstream in("B-small-attempt0.in");
	//ofstream out("B-small-out.txt");

	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}