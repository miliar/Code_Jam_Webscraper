/*
#include <iostream>
#include <fstream>
#include <cstring>
#include <map>

using namespace std;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	map<char, char> m;

	char s1[1000], s2[1000];

	int n;
	char x, y;
	ifstream fin("base.txt");

	fin >> n;
	for (int i = 0; i < n; ++i) {
		fin >> x >> y;
		m[x] = y;
	}

	m[' '] = ' ';
	
	fin.close();

	int t;
	cin >> t;
	cin.get();

	for (int i = 0; i < t; ++i) {
		cin.getline(s1, 1000);
		for (int j = 0; j < strlen(s1); ++j) {
			s2[j] = m[s1[j]];
		}
		s2[strlen(s1)] = 0;
		cout << "Case #" << i + 1 << ": " <<  s2 << endl;
	}

	return 0;
}
*/

#include <iostream>
#include <string>
#include <set>

using namespace std;

set<int> m_s;
set<int> temp;

int my_shift(char * s, int A, int B) {
	string x = s;
	int len = x.length();	

	temp.clear();

	string sub;
	int c;
	int p = 0;
	sscanf(x.c_str(), "%d", &c);
	if (m_s.count(c)) return 0;
	x += x;
	for (int i = 0; i < len; ++i) {		
		sub = x.substr(i, len);
		sscanf(sub.c_str(), "%d", &c);
		if (c >= A && c <= B) {
			m_s.insert(c);
			temp.insert(c);
		}
		p = temp.size();
	}

	return p > 1 ? p : 0;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int A, B;
	int n, k;
	long long p = 0;

	string x;
	char buff[20];

	cin >> n;

	for (int i = 0; i < n; ++i) {

		p = 0;
		cin >> A >> B;

		if (B < 10) {
			cout << "Case #" << i + 1 << ": 0" << endl;
			continue;
		}

		for (int h = A; h <= B; ++h) {
			sprintf(buff, "%d", h);
			k = my_shift(buff, A, B);
			p += k * (k - 1) / 2;
		}
	
		cout << "Case #" << i + 1 << ": " << p << endl;

		m_s.clear();

	}

	return 0;
}