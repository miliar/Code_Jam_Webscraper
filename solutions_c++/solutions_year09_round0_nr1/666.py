#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int th(string s, char a) {
	for (int i=0;i<s.size();i++) {
		if (s[i] == a)
			return true;
	}
	return false;
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("alienlanguage.out");
	fin.sync_with_stdio(false);
	fout.sync_with_stdio(false);
	int L, D, N;
	fin >> L >> D >> N;
	vector< string > a;
	string t;
	for (int i=0;i<D;i++) {
		fin >> t;
		a.push_back(t);
	}
	for (int i=0;i<N;i++) {
		fin >> t;
		vector< string > s;
		for (int k=0,in=0;k<L;k++) {
			string add;
			if (t[in] != '(') {
				add += t[in];
				in++;
			}
			else if (t[in] == '(') {
				in++;
				for (;t[in]!=')';in++) {
					add += t[in];
				}
				in++;
			}
			s.push_back(add);
		}
		int Ret = 0;
		for (int j=0;j<D;j++) {
			bool T = true;
			for (int k=0;k<L;k++) {
				if (!th(s[k], a[j][k])) {
					T = false;
					break;
				}
			}
			if (T)
				Ret++;
		}
		fout << "Case #" << i+1 << ": " << Ret << endl;
	}
	return 0;
}