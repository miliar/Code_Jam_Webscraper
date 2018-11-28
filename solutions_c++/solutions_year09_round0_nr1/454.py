#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
vector<int> f, tmp;
bool v[30];

int main() {
	ifstream fin("A-large.in");
	ofstream fout("aout.txt");

	int l, d, n;

	fin >> l >> d >> n;
	string s;
	vector<string> a;
	a.clear();

	for (int i = 0; i < d; i++) {
		fin >> s;
		a.push_back(s);
	}
	
	for (int t = 0; t < n; t++) {
		fout << "Case #" << t+1 << ": ";
		f.clear();
		for (int i = 0; i < d; i++)
			f.push_back(i);
		fin >> s;
		int now = 0;
		for (int i = 0; i < l; i++) {
			memset(v, 0, sizeof(v));
			if (s[now] == '(') {
				now++;
				while (s[now] != ')') {
					v[s[now]-'a'] = true;
					now++;
				}
			}
			else
				v[s[now]-'a'] = true;
			now++;
			tmp.clear();
			for (int j = 0; j < f.size(); j++) {
				if (v[a[f[j]][i]-'a'])
					tmp.push_back(f[j]);
			}
			f = tmp;
		}
		fout << f.size() << endl;
	}

	return 0;
}
