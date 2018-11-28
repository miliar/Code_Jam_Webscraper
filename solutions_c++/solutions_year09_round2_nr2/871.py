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

int func()
{
	return 0;
}

int main()
{
//	fstream fs("test1.txt", ios_base::in);
//	fstream fs("B-small-attempt0.in", ios_base::in);
	fstream fs("B-large.in", ios_base::in);
	string line;
	string v;
	vector<string> v_list;
	stringstream ss;

	getline(fs, line);
	while (getline(fs, line)) {
		ss.str("");  ss.clear();
		ss.str(line);
		ss >> v;
		v_list.push_back(v);
		v.clear();
	}

	int cnt = 0;
	for (vector<string>::iterator p = v_list.begin(); p != v_list.end(); ++p) {
		string first = *p;
		sort(first.begin(), first.end());
		string current = *p;
		int numzero = count(current.begin(), current.end(), '0');
		string nonzero;
		for (string::iterator q = p->begin(); q != p->end(); ++q)
			if (*q != '0') nonzero += *q;
		sort(nonzero.begin(), nonzero.end());
//		cerr << current << endl; /////
		next_permutation(current.begin(), current.end());
//		cerr << current << endl; /////
		string next;
		if (current == first) {
			next += nonzero[0];
			for (int i = 0; i < numzero + 1; i++) next += '0';
			for (int i = 1; i < nonzero.size(); i++) next += nonzero[i];
		} else {
			next = current;
		}
		cout << "Case #" << ++cnt << ": " << next << endl;
	}

	return 0;
}
