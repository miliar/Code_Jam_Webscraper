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
//typedef Int<50> number;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)

bool isHorzSim(size_t k, vector< vector<int> > & diam, size_t extra)
{
	FOR(i,2*k-1) {
		size_t jj = i < k ? i+1 : 2*k-i-1;
		assert(jj == diam[i].size());
		for (size_t j = 0; extra+j < jj-1-j; ++j)
			if (diam[i][extra+j] != diam[i][jj-1-j])
				return false;
	}
	return true;
}

bool isVertSim(size_t k, vector< vector<int> > & diam, size_t extra)
{
	for (size_t i = 0; i + extra < 2*k-2-i; ++i) {
		size_t jj = i + extra < k ? i + extra+1 : 2*k-(i + extra)-1;
		assert(jj == diam[i + extra].size());
		size_t jj2 = 2*k-2-i < k ? 2*k-2-i+1 : 2*k-(2*k-2-i)-1;
		assert(jj2 == diam[2*k-2-i].size());
		assert(jj2 <= jj && (jj-jj2)%2 == 0);
		size_t j0 = (jj-jj2)/2;
		for (size_t j = 0; j < jj2; ++j)
			if (diam[2*k-2-i][j] != diam[i + extra][j+j0])
				return false;
	}
	return true;
}

__int64 solve_case_onesimetry(size_t k, vector< vector<int> > & diam)
{
	__int64 result = 0;
	__int64 e = 0, f = 0;
	FOR(extra, k)
		if (isHorzSim(k,diam,extra)) {
			e = extra;
			break;
		}
	for (size_t extra = 0; extra < 2*k; extra+=2)
		if (isVertSim(k,diam,extra)) {
			f = extra/2;
			break;
		}
	result = (e+f+k)*(e+f+k) - k*k;
	return result;
}

__int64 solve_case(size_t k, vector< vector<int> > & diam)
{
	__int64 result1 = solve_case_onesimetry(k,diam);
	FOR(i,diam.size())
		reverse(diam[i].begin(), diam[i].end());
	__int64 result2 = solve_case_onesimetry(k,diam);
	__int64 result = (min)(result1,result2);
	reverse(diam.begin(), diam.end());
	__int64 result3 = solve_case_onesimetry(k,diam);
	result = (min)(result,result3);
	FOR(i,diam.size())
		reverse(diam[i].begin(), diam[i].end());
	__int64 result4 = solve_case_onesimetry(k,diam);
	result = (min)(result,result4);
	return result;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		size_t k;
		in >> k;
		vector< vector<int> > diam(2*k-1);
		FOR(i,2*k-1) {
			size_t jj = i < k ? i+1 : 2*k-i-1;
			diam[i].resize(jj);
			FOR(j,jj)
				if (!(in >> diam[i][j]))
					assert(false);
		}
		__int64 result = solve_case(k,diam);
		out << "Case #" << t << ": " << result << "\n";
	}
}


int main()
{
	//ifstream in("A-sample.in");
	//ofstream out("A-sample.txt");

	//ifstream in("A-small-attempt2.in");
	//ofstream out("A-small-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);

	return 0;
}