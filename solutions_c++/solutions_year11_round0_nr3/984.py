#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

void main() {
	int n, m;
	int i,j;

	cin >> n;
	REP(i,n) {
		int mins = 10000000;
		int val = 0;
		int sums = 0;
		int tmp;
		cin >> m;
		REP(j,m) {
			cin >> tmp;
			val ^= tmp;
			mins = min(mins,tmp);
			sums += tmp;
		}

		if (val != 0)
			cout << "Case #" << i + 1 << ": NO" << endl;
		else
			cout << "Case #" << i + 1 << ": " << sums - mins << endl;
	}
}
