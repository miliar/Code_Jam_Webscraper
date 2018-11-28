#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int main()
{
	long long int inps, i, mers, opps, ok, ok2, j, k, l, noth;
	vector <string> mer;
	vector <string> opp;
	string str, res, buf;

	cin >> inps;
	
	for (i = 0; i < inps; i++) {
		res = "";
		cin >> mers;
		mer.clear();
		for (; mers > 0; mers--) {
			cin >> buf;
			mer.push_back(buf);
		}
		cin >> opps;
		opp.clear();
		for (; opps > 0; opps--) {
			cin >> buf;
			opp.push_back(buf);
		}
		cin >> noth;
		cin >> str;
		res.push_back(str[0]);
		for (j = 1; j < str.size(); j++) {
			ok = 1;
			for (k = 0; k < mer.size(); k++) {
				if ((str[j] == mer[k][0] && res[res.size() - 1] == mer[k][1]) || (str[j] == mer[k][1] && res[res.size() - 1] == mer[k][0])) {
					res[res.size() - 1] = mer[k][2];
					ok = 0;
					break;
				}
			}
			if (!ok)
				continue;
			ok2 = 1;
			for (k = 0; k < opp.size(); k++) {
				if (!ok2)
					break;
				if (str[j] == opp[k][0] || str[j] == opp[k][1]) {
					for (l = 0; l < res.size(); l++) {
						if (str[j] == opp[k][0])
							if (res[l] == opp[k][1]) {
								res = "";
								ok2 = 0;
								break;
							}
						if (str[j] == opp[k][1])
							if (res[l] == opp[k][0]) {
								res = "";
								ok2 = 0;
								break;
							}
					}
				}
			}
			if (!ok2)
				continue;
			res.push_back(str[j]);
		}
		cout << "Case #" << i + 1 << ": [";
		for (j = 0; j < res.size(); j++) {
			cout << res[j];
			if (j < res.size() - 1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
