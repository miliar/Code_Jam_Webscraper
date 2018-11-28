#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

int main() {
	ifstream fin("B-large.in");
	ofstream fout("file.out");
	fin.sync_with_stdio(false);
	fout.sync_with_stdio(false);
	int t;
	string s;
	fin >> t;
	for (int k=0;k<t;k++) {
		fin >> s;
		fout << "Case #" << k+1 << ": ";
		string l = s;
		bool t = next_permutation(l.begin(), l.end());
		if (t)
			fout << l << endl;
		else {
			int sz = count(s.begin(), s.end(), '0')+1;
			sort(s.begin(), s.end());
			string r;
			r += s[sz-1];
			for (int i=0;i<sz;i++)
				r += '0';
			for (int i=sz;i<s.size();i++)
				r += s[i];
			fout << r << endl;
		}
	}
	return 0;
}