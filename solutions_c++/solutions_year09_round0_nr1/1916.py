#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

int check_pattern(string pattern, vector<string>& lines)
{
	int pa = 0;
	string l;
	vector<string> v;
	for (string::iterator p = pattern.begin(); p != pattern.end(); ++p) {
		if (*p == '(') pa++;
		else if (*p == ')') {
			pa--;
			v.push_back(l);
			l = "";
		} else if (pa > 0) {
			l += *p;
		} else {
			l += *p;
			v.push_back(l);
			l = "";
		}
	}
	stringstream ss;
	string data;
//	for (ss.str(pattern); ss >> data; v.push_back(data));
	int cnt = 0;
	for (vector<string>::iterator p = lines.begin(); p != lines.end(); ++p) {
		string::iterator q;
		vector<string>::iterator r;
		bool is_match = true;
		for (q = p->begin(), r = v.begin(); q != p->end(); ++q, ++r) {
			if (find(r->begin(), r->end(), *q) == r->end()) {
				is_match = false;
				break;
			}
		}
		if (is_match) cnt++;
	}
	return cnt;
}

int main(int argc, char *argv[])
{
	fstream fs("A-large.in", ios_base::in);
	string line;
	stringstream ss;
	vector<string> lines, patterns;

	getline(fs, line);
	ss.str(line);
	int L, D, N;
	ss >> L >> D >> N;
	for (int i = 0; i < D; i++) {
		getline(fs, line);
		lines.push_back(line);
	}
	for (int i = 0; i < N; i++) {
		getline(fs, line);
		patterns.push_back(line);
	}
	int cnt = 0;
	for (vector<string>::iterator p = patterns.begin(); p != patterns.end(); ++p) {
		cout << "Case #" << ++cnt << ": " << check_pattern(*p, lines) << endl;
	}

	return 0;
}
