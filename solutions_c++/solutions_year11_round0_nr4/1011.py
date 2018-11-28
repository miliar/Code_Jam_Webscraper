#define _CRT_SECURE_NO_WARNINGS

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

using namespace std;

int main() {
	freopen("input.txt.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;

	for (int e=1; e<=t; e++) {
		int n; cin >> n;
		int s[1111];
		double sum = 0;

		for (int i=1; i<=n; i++) {
			cin >> s[i];
			if (s[i] != i)
				sum ++;
		}

		printf("Case #%d: %0.8lf\n", e, sum);
	}

	return 0;
}