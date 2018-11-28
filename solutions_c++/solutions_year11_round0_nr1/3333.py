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

inline void ProblemSolver::SolveOneTest() 
{
	vector<int> aa;
	int n;
	ist >> n;
	for( int i = 0; i < n; i++ ) {
		string st;
		int x;
		ist >> st >> x;
		if( st == "O" ) {
			aa.push_back(x);
		} else if( st == "B" ) {
			aa.push_back(-x);
		}
	}
	int time = 0;
	int timea = 0;
	int timeb = 0;
	int posa = 1;
	int posb = 1;
	for( int i = 0; i < aa.size(); i++ ) {
		if( aa[i] < 0 ) {
			int dist = abs(posa + aa[i]);
			time = std::max(timea + dist + 1, time + 1);
			timea = time;
			posa = abs(aa[i]);
		} else {
			int dist = abs(posb - aa[i]);
			time = std::max(timeb + dist + 1, time + 1);
			timeb = time;
			posb = abs(aa[i]);
		}
	}
	ost << time << "\n";
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}
