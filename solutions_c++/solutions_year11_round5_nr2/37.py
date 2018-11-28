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

struct Straight {
	int last;
	int len;

	Straight(int l, int ll) : last(l), len(ll) {}
};

inline void ProblemSolver::SolveOneTest() 
{
	int n;
	ist >> n;
	vector<int> a(n);
	for( int i = 0; i < a.size(); i++ ) {
		ist >> a[i];
	}
	sort(a.begin(), a.end());
	vector<Straight> str;
	for( int i = 0; i < a.size(); i++ ) {
		int index = -1;
		for( int j = 0; j < str.size(); j++ ) {
			if( str[j].last == a[i] - 1 ) {
				if( index == -1 || str[j].len < str[index].len ) {
					index = j;
				}
			}
		}
		if( index == -1 ) {
			str.push_back(Straight(a[i], 1));
		} else {
			str[index].last = a[i];
			str[index].len++;
		}
	}
	for( int i = 0; i < str.size(); i++ ) {
		cout << str[i].len << " " << str[i].last << endl;
	}
	int res = n + 1;
	for( int i = 0; i < str.size(); i++ ) {
		if( str[i].len < res ) {
			res = str[i].len;
		}
	}
	if( n == 0 ) {
		res = 0;
	}
	ost << res << endl;
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

