#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <iomanip>
#include <sstream>
#include <algorithm>

using namespace std;

class ProblemSolver {
public:
	ProblemSolver() : ist("input.txt"), ost("output.txt") {}
	void Run();
	void SolveOneTest();

private:
	std::ifstream ist;
	std::ofstream ost;
};

inline long long check(long long x)
{
	long long min = 0;
	long long max = 2000000000;
	while( max - min > 1 ) {
		long long med = (max + min) / 2;
		if( med * med < x ) min = med; else max = med;
	}
	if( max * max == x ) return x;
	if( min * min == x ) return x;
	return 0;
}

inline long long rec(long long cur, const string& s, int dep) {
	if( dep == s.size() ) {
		return check(cur);
	}
	if( s[dep] == '0' ) {
		return rec(cur * 2, s, dep+1);
	} else if( s[dep] == '1' ) {
		return rec(cur * 2 + 1, s, dep+1);
	} else {
		long long t1 = rec(cur * 2, s, dep+1);
		if( t1 != 0 ) return t1;
		long long t2 = rec(cur * 2 + 1, s, dep+1);
		if( t2 != 0 ) return t2;
		return 0;
	}
}


inline void ProblemSolver::SolveOneTest() 
{
	string st;
	ist >> st;
	long long res = rec(0, st, 0);
	string ans;
	for( int i = 0; i < st.length(); i++ ) {
		if( res % 2 == 0 ) {
			ans = '0' + ans;
		} else {
			ans = '1' + ans;
		}
		res = res / 2;
	}
	ost << ans << endl;
}

inline void ProblemSolver::Run()
{
	int tn;
	ist >> tn;
	for( int i = 0; i < tn; i++ ) {
		ost << "Case #" << (i+1) << ": ";
		SolveOneTest();
	}
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}

