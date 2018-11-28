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
		vector<int> vals(n);
		int x = 0;
		for (int i=0;i<n;++i) {
			cin >> vals[i];
			x ^= vals[i];
		}
		if (x != 0) {
			printf("Case #%d: NO\n", z);
			continue;
		}
		printf("Case #%d: %d\n", z, accumulate(vals.begin(),vals.end(), 0) - *min_element(vals.begin(),vals.end()));
	}
}
