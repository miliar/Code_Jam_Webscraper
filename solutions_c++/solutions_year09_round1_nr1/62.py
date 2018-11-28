#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

bool ok(int n, int b, set<int>& used) {
	if(!used.insert(n).second) return false;
	if(n == 1) return true;
	int next = 0;
	for(int i = n; i; i /= b) next += (i % b) * (i % b);
	return ok(next, b, used);
}

int main() {
	int N;
	cin >> N;
	string line;
	getline(cin, line);
	for(int t = 0; t < N; ++t) {
		int base[10], bs = 0;
		string line;
		getline(cin, line);
		stringstream sst(line);
		while(sst >> base[bs++]);
		--bs;
		int res = 0;
		for(int i = 2; ; ++i) {
			res = i;
			bool o = true;
			for(int j = 0; j < bs && o; ++j) {
				set<int> used;
				o = ok(i, base[j], used);
			}
			if(o) break;
		}
		printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}
