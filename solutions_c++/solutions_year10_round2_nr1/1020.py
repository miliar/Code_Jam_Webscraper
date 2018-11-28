#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)




int solve_case(int N, int M, const vector<string> & existing, const vector<string> & tocreate)
{
	map<string, set<string> > children;
	FOR(i,N) {
		const string & path = existing[i];
		assert(path[0] == '/' && path.size() > 1);
		size_t prevslash = 0;
		string parent = "/";
		while (prevslash != string::npos) {
			size_t p = path.find('/',prevslash+1);
			string name = path.substr(0,p);
			children[parent].insert(name);
			parent = name;
			prevslash = p;
		}
	}
	int result = 0;
	FOR(i,M) {
		const string & path = tocreate[i];
		assert(path[0] == '/' && path.size() > 1);
		size_t prevslash = 0;
		string parent = "/";
		while (prevslash != string::npos) {
			size_t p = path.find('/',prevslash+1);
			string name = path.substr(0,p);
			set<string> &ss = children[parent];
			if (ss.find(name) == ss.end()) {
				++result;
				ss.insert(name);
			}
			parent = name;
			prevslash = p;
		}
	}
	return result;
}

void solve(istream & in, ostream & out)
{
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t)
	{
		int N, M;
		in >> N >> M;
		vector<string> existing(N), tocreate(M);
		FOR(i,N) {
			in >> existing[i];
		}
		FOR(i,M) {
			in >> tocreate[i];
		}
		int result = solve_case(N,M,existing,tocreate);
		out << "Case #" << t << ": " << result << "\n";
		//out << N << "\n";
		//FOR(i,N) {
		//	out << existing[i] << "\n";
		//}
		//out << M << "\n";
		//FOR(i,M) {
		//	out << tocreate[i] << "\n";
		//}
		//out << "\n";

	}
}


int main()
{
	//ifstream in("A-sample.in");
	//ofstream out("A-sample.txt");

	//ifstream in("A-small-attempt1.in");
	//ofstream out("A-small-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);

	return 0;
}