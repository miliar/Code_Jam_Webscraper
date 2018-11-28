#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std; 
long long t[1001];
int T, n;
long long MaxF = 0;

long long gcd(long long a, long long b) {
	if(b == 0) return a;
	else return gcd(b, a % b);
}


int main() {

	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	scanf("%d", &T);
	int caseT = 1;

	while(T--) {
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) {
			scanf("%lld", &t[i]);
		}
		long long Ans;
		MaxF = 0;
		sort(t, t + n);
		vector<long long> ans2;
		for(int i = 0; i < n - 1; ++i) {
			ans2.push_back(t[i + 1] - t[i]);
		}
		if(ans2.size() > 1)
			MaxF = gcd(ans2[0], ans2[1]);
		else
			MaxF = ans2[0];
		Ans = 10000000000000000LL;
		for(int i = 0; i < n; ++i) {
			if(t[i] % MaxF == 0) {
				Ans = min(Ans, 0LL);
			} else {
				Ans = min(Ans, MaxF - (t[i] % MaxF));
			}
		}

		printf("Case #%d: %lld\n", caseT++, Ans);
	}
}