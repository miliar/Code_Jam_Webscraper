#include <iostream>
#include <algorithm>
#include <utility>
#include <climits>
#include <vector>
#include <list>
#include <set>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forall(it, X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
typedef vector<int> vint;
typedef vector<vint> vvint;

int main() {
	int T,n,k;
	cin >> T;
	forn(t,T) {
		cin >> n >> k;
		bool res = (1<<n)-1 == k % (1<<n);
		cout << "Case #" << t+1 << ": " << (res ? "ON" : "OFF") << endl;
	}
	return 0;
}
