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

int Query(const vector< vector<int> >& a, int x1, int y1, int x2, int y2)
{
	int res = a[x2][y2];
	if( x1 == 0 && y1 == 0 ) {
		return res;
	} else if( x1 > 0 && y1 == 0 ) {
		return res - a[x1-1][y2];
	} else if( x1 == 0 && y1 > 0 ) {
		return res - a[x2][y1-1];
	} else {
		return res - a[x1-1][y2] - a[x2][y1-1] + a[x1-1][y1-1];
	}
}

inline void ProblemSolver::SolveOneTest() 
{
	int n,m,D;
	ist >> n >> m >> D;
	vector<string> a(n);
	for( int i = 0; i < n; i++ ) {
		ist >> a[i];
	}
	
	vector<vector<int> > ss = vector<vector<int> >(n, vector<int>(m));
	for( int i = 0; i < n; i++ ) {
		for( int j = 0; j < m; j++ ) {
			ss[i][j] = a[i][j] - '0';
			if( i > 0 && j == 0 ) {
				ss[i][j] += ss[i-1][j];
			} else if( i == 0 && j > 0 ) {
				ss[i][j] += ss[i][j-1];
			} else if( i > 0 && j > 0 ){
				ss[i][j] += ss[i-1][j] + ss[i][j-1] - ss[i-1][j-1];
			}
		}
	}

	int best = 0;
	for( int i = 0; i < n; i++ ) {
		for( int j = i + 2; j < n; j++ ) {
			int len = j - i + 1;
			for( int k = 0; k < m; k++ ) {
				int sum1 = 0;
				int sum2 = 0;
				if( k + len > m ) break;
				for( int xx = 0; xx < len; xx++ ) {
					for( int yy = 0; yy < len; yy++ ) {
						if( (xx == 0 || xx == len - 1) && (yy == 0 || yy == len - 1) ) continue;
						sum1 += ((xx + 1) * 2 - len - 1) * (a[i+xx][k+yy] - '0');
						sum2 += ((yy + 1) * 2 - len - 1) * (a[i+xx][k+yy] - '0');
					}
				}
				std::cout << i << " " << k << " " << len << " " << sum1 << " " << sum2 << std::endl;
				if( sum1 == 0 && sum2 == 0 ) {
					best = std::max(best, len);
				}
			}
		}
	}
	if( best == 0 ) {
		ost << "IMPOSSIBLE\n";
	} else {
		ost << best << "\n";
	}
	std::cout << "OK" << std::endl;
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}

