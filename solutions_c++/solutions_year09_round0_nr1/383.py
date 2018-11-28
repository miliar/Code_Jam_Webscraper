#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <fstream>
using namespace std;

const int L = 16;
const int M = 30;

struct Data
{
	int pos;
	int ch;
	int num;
	Data(const int p, const int c, const int n)
		: pos(p), ch(c), num(n)
	{}
};

int main()
{
/*
	ofstream out("large.txt");
	out << "15 5000 500" << endl;
	for (int i=0; i < 5000; ++i) {
		for (int j=0; j < 15; ++j) out << "a";
		out << endl;
	}
	for (int i=0; i < 500; ++i) {
		for (int j=0; j < 15; ++j) {
			out << "(abcdefghijklmnopqrstuvwxyz)";
		}
		out << endl;
	}
	return 0;
*/

	ofstream out("out2.txt");
	ifstream fin("in.txt");
	int l, d, n;
	fin >> l >> d >> n;

	vector<string> vorg(d);
	for (int i=0; i < d; ++i) {
		fin >> vorg[i];
	}


	for (int q=0; q < n; ++q) {
		bool isBad[5000] = { 0 };
		string s;
		int sp = 0;
		fin >> s;
		vector<string> v = vorg;
		int t = v.size();

		for (int pos=0; pos < l; ++pos) {
			bool usable[30] = { 0 };
			if (s[sp]!='(') {
				usable[s[sp]-'a'] = true;
				++sp;
			}
			else {
				++sp;
				while (s[sp]!=')') {
					usable[s[sp]-'a'] = true;
					++sp;
				}
				++sp;
			}

			for (int i=0; i < v.size(); ++i) {
				if (usable[v[i][pos]-'a']==false) {
					v.erase(v.begin()+i);
					--i;
				}
			}
		}
		out << "Case #" << q+1 << ": " << v.size() << endl;
		cout << "Case #" << q+1 << ": " << v.size() << endl;
	}

	out.close();
	fin.close();

	return 0;
}
