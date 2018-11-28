#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <strstream>
#include <map>
using namespace std;

int N;

vector<map<string, int> > mas;
vector<double> res;
string com;


double solve(int id, int &pos) {
	double res = 1;
	while (com[pos] == ' ') ++pos;

	++pos;

	while (com[pos] == ' ') ++pos;
	
	string str;

	while (com[pos] == '.' || (com[pos] >= '0' && com[pos] <= '9')) {
		str += com[pos++];
	}

	istrstream is(str.c_str());
	double p;
	is >> p;

	res *= p;

	while (com[pos] == ' ') ++pos;

	if (com[pos] == ')') {
		++pos;
		return res;
	}

	str = "";
	while (com[pos] >= 'a' && com[pos] <= 'z')
		str += com[pos++];

	while (com[pos] == ' ') ++pos;
	if (mas[id][str] != 0) {
		res *= solve(id, pos);
		while (com[pos] == ' ') ++pos;
		solve(id, pos);
	}
	else {
		solve(id, pos);
		while (com[pos] == ' ') ++pos;
		res *= solve(id, pos);
	}
	while (com[pos] == ' ') ++pos;
	++pos;

	return res;
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> N;
	for (int i = 0; i < N; ++i) {
		int m;
		string str;

		cin >> m;
		getline(cin, str);
		com = "";
		for (int j = 0; j < m; ++j) {
			getline(cin, str);
			com += " " + str;
		}
		cin >> m;

		mas.clear();
		for (int j = 0; j < m; ++j) {
			int L;
			cin >> str >> L;
			mas.push_back(map<string, int>());
			for (int k = 0; k < L; ++k) {
				cin >> str;
				mas[j][str] = 1;
			}
			res.push_back(1);
		}		
		
		cout << "Case #" << i + 1 << ":\n";

		for (int j = 0; j < m; ++j) {
			int pos = 0;
			double res = solve(j, pos);
			printf("%10.8f\n", res);
		}
	}



	return 0;
}