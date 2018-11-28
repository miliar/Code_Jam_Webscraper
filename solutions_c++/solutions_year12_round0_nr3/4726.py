#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <sstream>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define ll long long

int main() {    
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;

	for (int j = 1; j <= t; j++) {
		int a, b, count = 0;
		cin >> a >> b;

		vector<int> v;
		for (int i = a; i <= b; i++) {
			v.clear();
			int temp = i;
			while (temp > 0) {
				v.push_back(temp % 10);
				temp /= 10;
			}

			reverse(v.begin(), v.end());

			int sz = v.size();
			for (int k = 0; k < sz; k++) {
				v.push_back(v[k]);
			}

			set<int> Set;
			
			for (int k = 0; k < sz; k++) {
				int newr = 0;
				for (int p = k; p < k + sz; p++) {
					newr = newr * 10 + v[p];
				}

				if (newr >= a && newr <= b && newr > i) {
					if (Set.find(newr) == Set.end()) {
						Set.insert(newr);
						count++;
					}
				}
			}
		}

		printf("Case #%d: %d\n", j, count);
	}
	

    return 0;
}