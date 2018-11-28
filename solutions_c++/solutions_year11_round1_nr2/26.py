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

static long long calcHash(const vector<bool>& vis, const string& word)
{
	long long value = 1;
	for( int t = 0; t < word.size(); t++ ) {
		if( !vis[word[t]] ) {
			value = value * 30;
		} else {
			value = value * 30 + word[t] - 'a' + 1;
		}
	}
	return value;
}

inline void ProblemSolver::SolveOneTest() 
{
	int n,m;
	ist >> n >> m;
	vector<string> dict(n);
	for( int i = 0; i < n; i++ ) {
		ist >> dict[i];
	}
	for( int i = 0; i < m; i++ ) {
		vector<bool> vis(256, false);
		string order;
		ist >> order;
		vector<int> ans(n, 0);
		for( int j = 0; j < order.size(); j++ ) {
			unordered_map<long long, int> hash;
			unordered_map<long long, bool> hash2;
			for( int k = 0; k < n; k++ ) {
				long long value = calcHash(vis, dict[k]);
				for( int t = 0; t < dict[k].size(); t++ ) {
					if( dict[k][t] == order[j] ) {
						hash2[value] = true;
					}
				}
				hash[value]++;
			}
			for( int k = 0; k < n; k++ ) {
				long long value = calcHash(vis, dict[k]);
				if( hash[value] > 1 ) {
					if( dict[k].find(order[j]) == string::npos && hash2[value] ) {
						ans[k]++;
					}
				}
			}
			vis[order[j]] = true;
		}
		int best = 0;
		for( int j = 0; j < n; j++ ) {
			if( ans[j] > ans[best] ) {
				best = j;
			}
		}
		ost << dict[best];
		if( i != m - 1 ) {
			ost << " ";
		}
	}
	ost << "\n";
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}
