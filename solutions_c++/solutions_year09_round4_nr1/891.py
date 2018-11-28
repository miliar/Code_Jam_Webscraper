#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int doit(int X, vector <string> rows)
{
	if (rows.size() == 0) {
		return 0;
	}
	int ret = 1 << 30;
	for (int i = 0; i < rows.size(); i++) {
		if (rows[i].substr(X).find('1') == string::npos) {
			vector <string> newrows;
			for (int j = 0; j < rows.size(); j++) {
				if (j != i) {
					newrows.push_back(rows[j]);
				}
			}
			ret = min(ret, i + doit(X + 1, newrows));
		}
	}
	return ret;
}


int CrazyRows(int N, vector <string> rows)
{
	return doit(1, rows);
}

int main()
{
	string line;

	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N;
		cin >> N;
		vector <string> rows(N);
		for (int i = 0; i < N; i++) {
			cin >> rows[i];
		}

		int ret = CrazyRows(N, rows);

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
