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

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)


string solve_case(const vector<string> & combinations, const vector<string> & oppositions, const string & invokation)
{
	string result;
	vector< vector<char> > comb(256, vector<char>(256, '\0'));
	vector< vector<bool> > opp(256, vector<bool>(256, false));

	FOR(i,combinations.size()) {
		assert(comb[combinations[i][0]][combinations[i][1]] == 0);
		assert(comb[combinations[i][1]][combinations[i][0]] == 0);
		comb[combinations[i][0]][combinations[i][1]] = combinations[i][2];
		comb[combinations[i][1]][combinations[i][0]] = combinations[i][2];
		//falta assert() que sean base elements
	}
	FOR(i,oppositions.size())
	{
		assert(oppositions[i][0] != oppositions[i][1]);
		assert(!opp[oppositions[i][0]][oppositions[i][1]]);
		assert(!opp[oppositions[i][1]][oppositions[i][0]]);
		opp[oppositions[i][0]][oppositions[i][1]] = true;
		opp[oppositions[i][1]][oppositions[i][0]] = true;
		//falta assert() que sean base elements
	}

	FOR(i,invokation.size())
	{
		result += invokation[i];
		if (result.size() > 1) {
			size_t a = result.size()-2, b = result.size()-1;
			char c = comb[result[a]][result[b]];
			if (c != 0)
				result = result.substr(0,result.size()-2) + c;
			FOR(j,result.size()-1)
				if (opp[result[j]][result[result.size()-1]]) {
					result.clear();
					break;
				}
		}
	}

	if (result.empty()) return "[]";
	else {
		string s("[");
		s += result[0];
		for (size_t i = 1; i < result.size(); ++i) {
			s += ", ";
			s += result[i];
		}
		s += ']';
		return s;
	}
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int C;
		in >> C;
		vector<string> combinations;
		for (int c = 0; c < C; ++c)
		{
			string s;
			in >> s;
			assert(s.size() == 3);
			combinations.push_back(s);
		}
		int	D;
		in >> D;
		vector<string> oppositions;
		for (int d = 0; d < D; ++d)
		{
			string s;
			in >> s;
			assert(s.size() == 2);
			oppositions.push_back(s);
		}
		int N;
		in >> N;
		string invokation;
		in >> invokation;
		assert(invokation.size() == N);
		string result = solve_case(combinations,oppositions,invokation);
		out << "Case #" << t << ": " << result << "\n";
	}
}


int main()
{
	//ifstream in("B-sample.in");
	//ofstream out("B-sample.txt");

	//ifstream in("B-small-attempt0.in");
	//ofstream out("B-small-out.txt");

	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}