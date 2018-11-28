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

typedef long long LL;
string s;
int n;
int k;

int compress(const string& x) {
	int ret=1;
	char cur = x[0];
	for (int i=1;i<n;++i) if (x[i]!=cur) ++ret, cur = x[i];
	return ret;
}

int go(const vector<int>& perm) {
	string now(n,' ');
	for (int i=0;i<n/k;++i)
		for (int j=0;j<k;++j)
			now[k*i+j] = s[k*i + perm[j]];
	return compress(now);
}

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		cin >> k >> s;
		n = s.length();
		vector<int> perm(k,0);
		for (int i=0;i<k;++i) perm[i]=i;
		int minv = 1<<29;
		do {
			minv = min(minv,go(perm));
		} while (next_permutation(perm.begin(),perm.end()));
		printf("Case #%d: %d\n", z, minv);
	}
}
