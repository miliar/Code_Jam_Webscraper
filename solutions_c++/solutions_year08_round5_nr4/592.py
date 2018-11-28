#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <list>
#include <map>
using namespace std;

typedef long long lint;
typedef long long ulint;

static const int PRIME = 10007;

map<pair<unsigned, unsigned>, unsigned> table;
set<pair<unsigned, unsigned> > rocks;

unsigned countPaths(unsigned x, unsigned y, unsigned W, unsigned H) {
	if (x > W || y > H) return 0;
	if (x == W && y == H) return 1;

	//cerr << "(x, y) = (" << x << ", " << y << ")" << endl;

	// if (rocks.find(spot) != rocks.end()) {
	// 	return 0;
	// }
	// 
	// unsigned width = W - x + 1;
	// 	unsigned height = H - y + 1;
	// 	pair<unsigned, unsigned> spot(width, height);	

	pair<unsigned, unsigned> spot(x, y);
	if (table.find(spot) == table.end()) {
		unsigned result = countPaths(x + 2, y + 1, W, H) + countPaths(x + 1, y + 2, W, H);
		result %= PRIME;
	 	table.insert(make_pair(spot, result));
	}
	return table[spot];
}

int main(int argc, char const *argv[]) {
	unsigned nCases;
	cin >> nCases;
	for (unsigned N = 1; N <= nCases; N++) {
		unsigned H, W, R;
		cin >> H >> W >> R;
		
		table.clear();
		//vector<pair<unsigned, unsigned> > rocks;
		for (unsigned i = 0; i < R; i++) {
			unsigned x, y;
			cin >> x >> y;
			//rocks.insert(make_pair(x, y));
			table.insert(make_pair(make_pair(x, y), 0));
		}
		
		unsigned nPaths = countPaths(1, 1, H, W);
		// for (unsigned i = 0; i < R; i++) {
		// 	unsigned x = rocks[i].first;
		// 	unsigned y = rocks[i].second;
		// 	nPaths -= countPaths(x, y) * countPaths(W - x + 1, H - y + 1);
		// }
		
		cout << "Case #" << N << ": "
		     << nPaths << endl;
	}
	
	return 0;
}