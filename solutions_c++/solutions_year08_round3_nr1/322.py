#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

int main() {
	int T,t;
	int P,K,L;
	int i,a;

	cin >> t;
	for(T=1;t--;T++) {
		vector<int> v;

		cin >> P >> K >> L;
		for(i=0;i<L;i++) {
			cin >> a;
			v.push_back(a);
		}

		sort(v.begin(), v.end(), greater<int>());

		int res=0;
		for(i=0;i<v.size();i++) {
			res+=(i/K+1)*(v[i]);
		}

		printf("Case #%d: %d\n", T, res);
	}

	return 0;
}