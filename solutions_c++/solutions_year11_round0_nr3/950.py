#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>

#define ALL(s) (s).begin(), (s).end()
#define FOREACH(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define REP(i, a) for (int i = 0; i < a; i++)

#define SZ(x) ((int) (x).size())
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

using namespace std;

vector<int> candies;
int ncandies;

typedef struct {
	int xorsean;
	int xorpatrick;
	long actualsean;
} Sums;

Sums xorsum(int pivot) {
	int a = 0; long s = 0;
	for (int i = 0; i <= pivot; i++) {
		a ^= candies[i];
		s += candies[i];
	}
	
	int b = 0;
	for (int i = pivot + 1; i < ncandies; i++) {
		b ^= candies[i];
	}
	
	Sums the_sums;
	the_sums.xorsean = a;
	the_sums.xorpatrick = b;
	the_sums.actualsean = s;
	
	return the_sums;
}

void solve() {
	sort(ALL(candies));
	reverse(ALL(candies));
	
	list<long> possible_sums = list<long>();
	
	REP (s, ncandies - 1) {
		Sums sums = xorsum(s);
		int sean = sums.xorsean;
		int patrick = sums.xorpatrick;
		
		if (sean == patrick) {
			possible_sums.push_back(sums.actualsean);
		}
	}
	
	if (possible_sums.size() == 0) {
		printf("NO");
	} else {
		long max_sum = 0;
		FOREACH (s, possible_sums) {
			if (*s > max_sum) {
				max_sum = *s;
			}
		}
		
		printf("%ld", max_sum);
	}
}

int main(int argc, char ** argv) {
	int ncases;
	cin >> ncases;

	FOR(t, 1, ncases) {
		printf("Case #%d: ", t);
		
		cin >> ncandies;
		candies = vector<int>(ncandies);
		
		REP (i, ncandies) {
			int val;
			cin >> val;
			
			candies[i] = val;
		}
		
		solve();
		
		printf("\n");
	}
}
