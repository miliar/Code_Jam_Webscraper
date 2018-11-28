#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

const int SIZE = 1024;

struct Elem {
	int len;
	int prob;
	int name;
	inline bool operator< (const Elem &b) const {
		int diff = prob * b.len - b.prob * len;
		if (diff != 0) return diff > 0;
		return name < b.name;
	}
};

int n;
Elem arr[SIZE];
double res[SIZE];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d", &n);
		for (int i = 0; i<n; i++) scanf("%d", &arr[i].len);
		for (int i = 0; i<n; i++) scanf("%d", &arr[i].prob);
		for (int i = 0; i<n; i++) arr[i].name = i;

		std::sort(arr, arr+n);

		printf("Case #%d:", tt);
		for (int i = 0; i<n; i++) printf(" %d", arr[i].name);
		printf("\n");
		fflush(stdout);
	}
	return 0;
}
