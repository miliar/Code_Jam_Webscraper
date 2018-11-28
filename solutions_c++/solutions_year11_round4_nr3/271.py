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

vector<long long> primes;

bool IsPrime(int x) {
	for( int i = 2; i * i <= x; i++ ) {
		if( x % i == 0 ) return false;
	}
	return true;
}

inline void ProblemSolver::Run()
{
	int tn;
	ist >> tn;
	for( int i = 2; i <= 1000007; i++ ) {
		if( IsPrime(i) ) {
			primes.push_back(i);
		}
	}
	for( int i = 0; i < tn; i++ ) {
		ost << "Case #" << (i+1) << ": ";
		SolveOneTest();
	}
}

inline void ProblemSolver::SolveOneTest() 
{
	long long x;
	ist >> x;
	long long res = x == 1 ? 0 : 1;
	for( int i = 0; i < primes.size(); i++ ) {
		if( primes[i] > x ) {
			break;
		}
		long long cur = x;
		res--;
		while( cur >= primes[i] ) {
			res++;
			cur = cur / primes[i];
		}
	}
	ost << res << std::endl;
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}

