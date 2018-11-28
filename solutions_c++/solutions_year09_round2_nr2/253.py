#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <fstream>
using namespace std;

#ifdef WIN32
//ifstream in("B-small.in");
ifstream in("B-large.in");
#define cin in
//ofstream out("B-small.out");
ofstream out("B-large.out");
#define cout out
#endif

int main()
{
	int t, ca = 0;
	for (cin >> t; t; --t) {
		string num;
		cin >> num;
		string res = "";
		if (num.size() == 1) res = num + "0";
		else {
			int i, j;
			for (i = num.size() - 2; i >= 0 && num[i] >= num[i + 1]; --i);
			if (i < 0) {
				sort(num.begin(), num.end());
				for (i = 0; i < num.size() && num[i] == '0'; ++i);
				res += num[i];
				res += "0";
				res += num.substr(0, i);
				if (i + 1 < num.size()) {
					res += num.substr(i + 1);
				}
			} else {
				for (j = num.size() - 1; num[i] >= num[j]; --j);
				swap(num[i], num[j]);
				res = num.substr(i + 1);
				sort(res.begin(), res.end());
				res = num.substr(0, i + 1) + res;
			}
		}

		cout << "Case #" << ++ca << ": " << res << endl;
	}
	return 0;
}
