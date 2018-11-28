#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

	#define cin fin
	#define cout fout
	ifstream fin("B-large.in");
	ofstream fout("B.out");

	int C, O, N;
	struct Wiz {char a, b, c;} c[36], o[28];
	char s[200];

bool combine(vector<char>& v) {
	if (v.size() < 2) return false;
	int k = v.size() - 1;
	for (int i=0; i<C; ++i)
		if (v[k-1] == c[i].a && v[k] == c[i].b ||
			v[k-1] == c[i].b && v[k] == c[i].a) {
			v.pop_back();
			v.pop_back();
			v.push_back(c[i].c);
			return true;
		}
	return false;
}

bool opposed(vector<char>& v) {
	if (v.size() < 2) return false;
	for (int i=0; i<O; ++i)
		for (int k=0; k<v.size()-1; ++k)
			if (v[k] == o[i].a && v.back() == o[i].b ||
				v[k] == o[i].b && v.back() == o[i].a) {
				v.clear();
				return true;
			}
	return false;
}

int main() {
	int cs; cin >> cs;
	for (int cn=1; cn<=cs; ++cn) {
		cin >> C;
		for (int i=0; i<C; ++i)
		    cin >> c[i].a >> c[i].b >> c[i].c;

		cin >> O;
		for (int i=0; i<O; ++i)
		    cin >> o[i].a >> o[i].b;

		cin >> N;
		for (int i=0; i<N; ++i)
		    cin >> s[i];

		vector<char> v;
		for (int i=0; i<N; ++i) {
			v.push_back(s[i]);
			while (combine(v) || opposed(v)) ;
		}

		cout << "Case #" << cn << ": [";
		if (v.size() > 0) cout << v[0];
		for (int i=1; i<v.size(); ++i) cout << ", " << v[i];
		cout << "]\n";
	}
	system("pause");
	return 0;
}
