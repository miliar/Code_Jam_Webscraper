#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int s2i(string s) {
	istringstream iss(s);
	int i;
	iss >> i;
	return i;
} 

int getFirstEntry(vector<string> &query, string se, int off) {
	for (int i = off; i < query.size(); i++)
		if (se == query[i])	return i;

	return query.size();
} 

int main() {
	string s;
	vector<string> engines;
	vector<string> queries;

	//num cases
	getline(cin, s);
	int n = s2i(s);

	for (int c = 0; c < n; c++) {
		engines.clear();
		queries.clear();
		//num engines
		getline(cin, s);
		int e = s2i(s);
		for (int i = 0; i < e; i++) {
			getline(cin, s);
			engines.push_back(s);
		}
		//num querys
		getline(cin, s);
		int q = s2i(s);
		for (int i = 0; i < q; i++) {
			getline(cin, s);
			queries.push_back(s);
		}

		//get minimal switches
		int qi = 0;
		int tmp, swi = -1, max = 0;
		while (qi < q) {
			swi++;
			for (int i = 0; i < engines.size(); i++) {
				tmp = getFirstEntry(queries, engines[i], qi);
				if (max < tmp)
					max = tmp;
			}

			qi = max;
		}

		cout << "Case #" << c + 1 << ": " << (swi == -1 ? 0 : swi) << endl;
	}

	return 0;
}
