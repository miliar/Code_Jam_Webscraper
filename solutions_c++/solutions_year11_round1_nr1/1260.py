#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<bool, bool> bb;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<bb> vbb;
typedef vector<ii> vii;
typedef vector<vector<int> > vvi;


int gcd(int a, int b)
{
	while ((a != 0) && (b != 0)) {
		if (a < b) {
			b = b % a;
		} else {
			a = a % b;
		}
	}
	if (a == 0) {
		return b;
	}
	return a;
}



bool is_possible(int N, int PD, int PG)
{
	if (PD == 0) {
		return (PG < 100);
	}
	// PD > 0
	if (PD < 100 && PG == 100) return false;
	if (PG == 0) {
		return false;
	}
	int denom = 100 / gcd(100, PD);
	return (N >= denom);
}	


int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, PD, PG;
		cin >> N >> PD >> PG;
		cout << "Case #" << t << ": " \
			<< (is_possible(N, PD, PG) ? "Possible\n" : "Broken\n");
	}
	
	return 0;
}
