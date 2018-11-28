/*
#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>
#include <sstream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	fstream fout("out.txt");
	fstream fin("in.txt");

	int T;
	fin>>T;

	for (int q=0; q < T; ++q) {
		string s;
		fin >> s;
		string t = s;
		if (next_permutation(s.begin(), s.end()) == false) {
			sort(t.begin(), t.end());
			int c = count(t.begin(), t.end(), '0');
			t.erase(remove(t.begin(), t.end(), '0'), t.end());
			t.insert(t.begin()+1, c+1, '0');
			s = t;
		}
		fout << "Case #" << q+1 << ": " << s << endl;
		cout << "Case #" << q+1 << ": " << s << endl;
	}

	fout.close();
	fin.close();

	return 0;
}
*/