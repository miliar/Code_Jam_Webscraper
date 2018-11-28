#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

typedef long long LL;
typedef long double LD;

#define pb push_back
#define mp make_pair
#define sz(A) int((A).size())
#define y1 Y1
#define y2 Y2

const int N = int(2e6);

int len(int a) {
	int res = 0;
	while (a) {
		res++;
		a /= 10;
	}
	return res;
}

int p[10];
set<int> nums;

void precalc() {
	p[0] = 1;
	for (int i = 1; i <= 9; i++)
		p[i] = p[i - 1] * 10;
}

int add(int i, int b) {		
	nums.clear();
	int l = len(i), cnt = 0;
	for (int j = 1; j < l; j++) {
		int deg1 = p[j], deg2 = p[l - j];
		int num = (i % deg1) * deg2 + i / deg1;
		if (num > i && num <= b) { 
			if (!nums.count(num)) {
				cnt++;
				nums.insert(num);
			}
		}
	}
	return cnt;
}

int main() {
	precalc();
	int t, a, b;
	scanf("%d", &t);

	int ans;

	for (int i = 0; i < t; i++) {
		ans = 0;
		scanf("%d%d", &a, &b);
		for (int j = a; j <= b; j++) 
			ans += add(j, b);
		printf("Case #%d: %d\n", i + 1, ans);
	}	
																									
	return 0;
}
