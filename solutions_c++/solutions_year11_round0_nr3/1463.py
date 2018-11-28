#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define MAX_P 1000

int solve(int test)
{
	long min;
	long xor;
	long elem;
	long sum;
	int count;
	int i;

	cout << "Case #" << test << ": ";

	cin >> count;

	min = LONG_MAX;
	sum = 0;
	xor = 0;

	FOR(i, count) {
		cin >> elem;
		
		xor = xor ^ elem;

		if (elem < min)
			min = elem;

		sum += elem;
	}

	if (xor)
		cout << "NO" << endl;
	else
		cout << (sum - min) << endl;

	return 0;
}

int main()
{
	int cases = 0;
	int i;

	freopen("C_small_1.in", "r", stdin);
	freopen("C_small_1.out", "w", stdout);
	
	cin >> cases;

	FOR(i, cases) {
		solve(i + 1);
	}
	
	return 0;
}
