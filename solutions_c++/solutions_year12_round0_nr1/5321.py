#include <iostream>
#include <fstream>
#include <cstring>
#include <map>

using namespace std;

int main() {
	
//#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
//#endif

	map<char, char> m;

	char s1[1000], s2[1000];

	int n;
	char x, y;
	ifstream fin("base.txt");

	fin >> n;
	for (int i = 0; i < n; ++i) {
		fin >> x >> y;
		//cout << "x = " << x << endl;
		//cout << "y = " << y << endl;
		//m[y] = x;
		m[x] = y;
	}

	m[' '] = ' ';
	
	fin.close();

	int t;
	cin >> t;
	cin.get();

	for (int i = 0; i < t; ++i) {
		cin.getline(s1, 1000);
		//cout << "s1 = " << s1 << endl;
		//cin.getline(s2, 1000);
		for (int j = 0; j < strlen(s1); ++j) {
			//if (i == 6)cout << "s1[j] = " << s1[j] << endl;
			//cout << "!s1 = " << s1[j] << endl;
			s2[j] = m[s1[j]];
			//if (i == 6)cout << "s2[j] = " << s2[j] << endl;
			//cout << "!s2 = " << s2[j] << endl;
		}
		s2[strlen(s1)] = 0;
		cout << "Case #" << i + 1 << ": " <<  s2 << endl;

	}

	return 0;
}