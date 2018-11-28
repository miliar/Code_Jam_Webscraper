#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		int n;
		cin >> n;
		vector<pair<int,string> > O;
		for (int i=0;i<n;++i) {
			string p;
			int at;
			cin >> p >> at;
			O.push_back(make_pair(at,p));

		}

		int curtime = 0;
		int atO = 1, timeO = 0, atB = 1, timeB = 0;
		for (int i=0;i<O.size();++i) {
			if (O[i].second == "O") {
				int press = timeO + abs(atO - O[i].first) + 1;
				atO = O[i].first;
				curtime = timeO = max(press, curtime + 1);
			}
			else {
				int press = timeB + abs(atB - O[i].first) + 1;
				atB = O[i].first;
				curtime = timeB = max(press, curtime + 1);
			}
		}
		printf("Case #%d: %d\n", z, curtime);
	}
}
