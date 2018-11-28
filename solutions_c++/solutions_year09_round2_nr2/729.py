#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
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

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

string solve(string s) {
	if (next_permutation(all(s)))
		return s;
	sort(all(s));	
	int z = 0;
	sort(all(s));
	while (s[0] == '0') {
		++z;
		s = s.substr(1);
	}	
	return s[0] + string(z + 1, '0') + s.substr(1);
}

int main () {
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	getchar();
	for (int T = 1; T <= nTests; T++) {
		char buf[1024];
		gets(buf);
		printf("Case #%d: %s\n", T, solve(string(buf)).c_str());
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
