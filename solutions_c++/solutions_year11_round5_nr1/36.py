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

struct Point {
	double X;
	double Y;
};

istream& operator>> (istream& ist, Point& p) {
	return ist >> p.X >> p.Y;
}

inline void ProblemSolver::SolveOneTest() 
{
	int W, L, U, G;
	ist >> W >> L >> U >> G;
	vector<Point> a(L);
	vector<Point> b(U);
	for( int i = 0; i < L; i++ ) {
		ist >> a[i];
	}
	for( int i = 0; i < U; i++ ) {
		ist >> b[i];
	}
	double sq0 = 0.0;
	for( int i = 1; i < L; i++ ) {
		sq0 -= (a[i].Y + a[i-1].Y) * (a[i].X - a[i-1].X) / 2.0;
	}
	for( int i = 1; i < U; i++ ) {
		sq0 += (b[i].Y + b[i-1].Y) * (b[i].X - b[i-1].X) / 2.0;
	}
	
//	cout << sq0 << endl;
	ost << endl;
	for( int j = 1; j < G; j++ ) {
		double max = W;
		double min = 0;
		while( max - min > 1e-7 ) {
			double med = (max + min) / 2.0;
//			cout << med << endl;
			double sq = 0;
			for( int i = 1; i < L; i++ ) {
				if( med > a[i].X ) {
					sq -= (a[i].Y + a[i-1].Y) * (a[i].X - a[i-1].X) / 2.0;
				} else {
					sq -= (2 * a[i-1].Y + (a[i].Y - a[i-1].Y) * (med - a[i-1].X) / (a[i].X - a[i-1].X)) * (med - a[i-1].X) / 2.0;
					break;
				}
			}
//			cout << sq << endl;
			for( int i = 1; i < U; i++ ) {
				if( med > b[i].X ) {
					sq += (b[i].Y + b[i-1].Y) * (b[i].X - b[i-1].X) / 2.0;
				} else {
					sq += (2 * b[i-1].Y + (b[i].Y - b[i-1].Y) * (med - b[i-1].X) / (b[i].X - b[i-1].X)) * (med - b[i-1].X) / 2.0;
					break;
				}
			}
//			cout << sq << endl;
			if( sq0 * j / G < sq ) max = med; else min = med;
		}
		ost << setprecision(8) << (max + min) / 2.0 << endl;
	}
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

