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

using std::string;
using std::vector;
using std::set;
using std::map;
using std::tr1::unordered_map;
using std::tr1::unordered_set;

class ProblemSolver {
public:
	ProblemSolver() : ist("input.txt"), ost("output.txt") {}
	void Run();
	void SolveOneTest();

private:
	std::ifstream ist;
	std::ofstream ost;
};

inline void ProblemSolver::Run()
{
	int tn;
	ist >> tn;
	for( int i = 0; i < tn; i++ ) {
		ost << "Case #" << (i+1) << ": ";
		SolveOneTest();
	}
}

inline long long gcd(long long a, long long b) {
	if( b == 0 ) {
		return a;
	} else {
		return gcd(b, a % b);
	}
}

inline long long lcm(long long a, long long b) {
	return a * b / gcd(a, b);
}

inline void ProblemSolver::SolveOneTest() 
{
	long long pd, pg;
	long long n;
	ist >> n >> pd >> pg;
	if( pg == 0 || pg == 100 ) {
		if( pd == 0 && pg == 0 ) {
			ost << "Possible\n";
		} else if( pd == 100 && pg == 100 ) {
			ost << "Possible\n";
		} else {
			ost << "Broken\n";
		}
		return;
	}

	for( int i = 1; i <= n && i < 200; i++ ) {
		if( i * pd % 100 == 0 ) {
			ost << "Possible\n";
			return;
		}
	}
	ost << "Broken\n";
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}
