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
#include <algorithm>
#include <iomanip>

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

struct Interval {
	int st;
	int fin;
	int v;

	Interval(int _st, int _fin, int _v) : st(_st), fin(_fin), v(_v) {}
};

struct Comparator {
public:
	bool operator()(const Interval& i1, const Interval& i2) {
		return i1.v < i2.v;
	}
};

inline void ProblemSolver::SolveOneTest() 
{
	int n;
	int R, S, X, T;
	ist >> X >> S >> R >> T >> n;
	vector<Interval> a;
	int lastX = 0;
	for( int i = 0; i < n; i++ ) {
		int st, fin, v;
		ist >> st >> fin >> v;
		a.push_back(Interval(lastX, st, 0));
		a.push_back(Interval(st, fin, v));
		lastX = fin;
	}
	a.push_back(Interval(lastX, X, 0));
	std::sort(a.begin(), a.end(), Comparator());
	double tLeft = T;
	double res = 0;
	for( int i = 0; i < a.size(); i++ ) {
		if( 1.0 * (a[i].fin - a[i].st) / (a[i].v + R) < tLeft ) {
			double dt = 1.0 * (a[i].fin - a[i].st) / (a[i].v + R);
			tLeft -= dt;
			res += dt;
		} else {
			double tmpLen = a[i].fin - a[i].st - (a[i].v + R) * tLeft;
			res += tLeft;
			res += tmpLen / (a[i].v + S);
			tLeft = 0;
		}
	}
	ost << std::setprecision(10) << res << std::endl;
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}

