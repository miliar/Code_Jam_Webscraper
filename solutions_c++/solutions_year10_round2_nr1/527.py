#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int _t, n, m, r;
string str;
set <string> A;
vector <string> D;

vector <string> split(string tmp) {
	vector <string> ret;
	tmp = tmp.substr(1);
	while (tmp.size() > 0) {
		if (tmp.find_first_of('/') == string::npos) {
			ret.push_back(tmp);
			break;
		} else {
 			ret.push_back(tmp.substr(0, tmp.find_first_of('/'))); 
			tmp = tmp.substr(tmp.find_first_of('/') + 1);
		}
	}
	return ret;
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	cin >> _t;
	for (int cas = 1; cas <= _t; cas++) {
		cin >> n >> m;
		A.clear();
		for (int i = 0; i < n; i++) {
			string tmp;
			cin >> tmp;
			D = split(tmp);
			tmp = "";
			for (int j = 0; j < D.size(); j++) {
				tmp += '/' + D[j];
				A.insert(tmp);
			}
		}
		r = 0;
		for (int i = 0; i < m; i++) {
			string tmp;
			cin >> tmp;
			D = split(tmp);
			tmp = "";
			for (int j = 0; j < D.size(); j++) {
				tmp += '/' + D[j];
				r += A.insert(tmp).second;
			}
		}
		cout << "Case #" << cas << ": " << r << endl;
	}
	return 0;
}