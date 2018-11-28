#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		std::vector<string> pairs;
		int count = 0;
		int a, b;
		cin >> a >> b;

		for (int m = a; m <= b; m++) {
			for (int n = a; n < m; n++) {
				if (n == m)
					break;

				stringstream ssn;
				ssn << n;
				string sn = ssn.str();

				stringstream ssm;
				ssm << m;
				string sm = ssm.str();

				int l = sn.size();

				for (int i = 1; i < l; i++) {
					string x = sn.substr(l-i, i) + sn.substr(0, l-i);
					if (x == sm) {
						string c = sn + ":" + sm;
 						if (find(pairs.begin(), pairs.end(), c) == pairs.end()) {
							pairs.push_back(c);
							count++;
						}
					}
				}
			}
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}
}
