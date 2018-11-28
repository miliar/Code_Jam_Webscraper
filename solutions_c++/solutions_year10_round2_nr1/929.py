#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>

using namespace std;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

vector<string> split(string path) {
	vector<string> res;
	int ind = 1;
	while(1) {
		int fn = path.find('/', ind);
		if (fn == string::npos) {
			if (path.substr(ind) != "") res.push_back(path.substr(ind));
			break;
		}
		res.push_back(path.substr(ind, fn - ind));
		ind = fn + 1;
	}
	return res;
}

int main() {
	ifstream in("A-large.in");
	//ifstream in("A-small-attempt0.in");
	//ifstream in("A.in");
	ofstream out("A.out");

	int T; in >> T;

	for (int x = 1; x <= T; x++) {
		int N, M; in >> N >> M;
		vector<vector<string> > dirs;
		for (int i = 0; i < N; i++) {
			string path;
			in >> path;
			vector<string> dirs_path = split(path);
			dirs.push_back(dirs_path);
		}
		int res = 0;
		for (int i = 0; i < M; i++) {
			string path;
			in >> path;
			vector<string> dirs_path = split(path);
			int toc = dirs_path.size();
			for (int j = 0; j < dirs.size(); j++) {
				int k = 0;
				for (; k < dirs_path.size() && k < dirs[j].size(); k++) {
					if (dirs_path[k] != dirs[j][k]) break;
				}
				k = dirs_path.size() - k;
				if (k < toc) {
					toc = k;
				}
			}
			dirs.push_back(dirs_path);
			res += toc;
		}
		out << "Case #" << x << ": " << res << endl;
	}

	return 0;
}
