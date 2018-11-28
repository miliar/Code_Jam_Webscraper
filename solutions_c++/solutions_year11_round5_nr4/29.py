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

char str[1024];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {

		scanf("%s", str);
		int l = strlen(str);

		int64 x = 0;
		vector<int64> arr;

		for (int i = 0; i < l; i++) {
			int p = l-1-i;
			if (str[i] == '?') arr.push_back(1LL << p);
			if (str[i] == '1') x += (1LL << p);
		}

		int64 ans = -1;
		int k = arr.size();
		for (int m = 0; m<1<<k; m++) {
			int64 tt = x;
			for (int j = 0; j<k; j++) if (m & (1<<j)) tt += arr[j];
			int64 xx = int64(sqrt(tt+0.0) + 0.5);
			if (xx * xx == tt) ans = tt;
		}

		printf("Case #%d: ", tt);

		bool pr = false;
		for (int i = 62; i>=0; i--) {
			if (ans & (1LL << i)) pr = true;
			if (pr) printf("%d", int((ans>>i)&1));
		}
		printf("\n");
			
		fflush(stdout);
	}
	return 0;
}
