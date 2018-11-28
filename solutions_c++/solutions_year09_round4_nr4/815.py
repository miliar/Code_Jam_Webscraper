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
#include <climits>
using namespace std;

#define SQR(x)  ((x) * (x) )

void solve(int problem_no)
{
	int n;
	cin >> n;
	vector<int> x(n), y(n), r(n);
	for (int i = 0; i < n; ++i) {
		cin >> x[i] >> y[i] >> r[i];
	}
	double minr;
	if (n == 1) minr = r[0];
	else if (n == 2) minr = max(r[0], r[1]);
	else if (n == 3) {
		minr = 10000;
		for (int i = 0; i < n; ++i) {
			for (int j = i + 1; j < n; ++j) {
				minr = min(minr, (sqrt( (double)(SQR(x[i] - x[j]) + SQR(y[i] - y[j]))) + r[i] + r[j]) / 2.0f);
			}
		}
		minr = max(minr, (double) max(max(r[0], r[1]), r[2]));
	}
	
	printf("Case #%d: %f\n", problem_no, minr);
	return;
}
		
int main()
{
	int n;
	cin >> n;
	
	for (int i = 1; i <= n; ++i) {
		if (i % 100 == 0) {
			cerr << "SOLVE " << i << "/" << n << endl;
		}
		solve(i);
	}
	
	return 0;
}

