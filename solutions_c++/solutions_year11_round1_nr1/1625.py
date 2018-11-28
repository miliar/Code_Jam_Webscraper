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

#define MAX_N 50

int table[MAX_N][MAX_N];

int solve(int test)
{
	int n;
	int pd;
	int pg, d, wd;
	
	cout << "Case #" << test << ": ";
	
	cin >> n >> pd >> pg;

	if (pg == 100) {
		if (pd < 100)
			cout << "Broken" << endl;
		else	
			cout << "Possible" << endl;
		return 0;
	}

	if (!pg && pd) {
		cout << "Broken" << endl;
		return 0;
	}
	
	for(d = 1; d <= n; d++) {
	
		if (((pd * d)% 100 == 0)) {
			wd =  (pd * d) / 100;
			
			cout << "Possible" << endl;
			return 0;
		}
		
	}
	
	cout << "Broken" << endl;
	
	return 0;
}

int main()
{
	int cases = 0;
	int i;

	cin >> cases;

	FOR(i, cases) {
		solve(i + 1);
	}
	
	return 0;
}

