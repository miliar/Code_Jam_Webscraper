#include <string>
#include <vector>
#include <iterator>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <algorithm>
#include <fstream>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;


int main() {
	string fname = "C:\\B-large.in";
	string outname = "C:\\B.out";
	ifstream in;
	ofstream out;
	in.open(fname);
	out.open(outname);

	int N;
	in >> N;
	for (int i=0; i < N; ++i) {
		int c;
		in >> c;
		map< pair<char, char>, char> r;
		for (int j = 0; j < c; ++j) {
			string t;
			in >> t;
			r[make_pair(t[0], t[1])] = t[2];
			r[make_pair(t[1], t[0])] = t[2];
		}
		int d;
		in >> d;
		map<char, vector<char> > o;
		for (int j = 0; j < d; ++j) {
			string temp;
			in >> temp;
			if (o.find(temp[0]) == o.end()) o[temp[0]] == vector<char>();
			if (o.find(temp[1]) == o.end()) o[temp[1]] == vector<char>();
			o[temp[0]].push_back(temp[1]);
			o[temp[1]].push_back(temp[0]);
		}

		int m;
		in >> m;
		string el;
		in >> el;

		map<char, int> has;
		vector<char> res;
		for (int j = 0; j < m; ++j) {
			if (res.size() > 0) {
				map<pair<char,char>, char>::iterator it = r.find(make_pair(el[j], res.back()));
				if (it != r.end()) {
					has[res.back()]--;
					res.pop_back();
					res.push_back(it->second);
					has[res.back()]++;
				}
				else
				{
					res.push_back(el[j]);
					has[res.back()]++;
				}
			}
			else
			{
				res.push_back(el[j]);
				has[res.back()]++;
			}
			for (int l = 0; l < o[res.back()].size(); ++l) {
				if (has[o[res.back()][l]] > 0)
				{
					has.clear();
					res.clear();
					break;
				}
			}
		}

		out << "Case #" << i + 1 << ": [";
		for (int p = 0; p < res.size(); ++p) {
			if (p != 0) out << ", ";
			out << res[p];
		}
		out << "]" << endl;
	}
	in.close();
	out.close();
	return 0;
}