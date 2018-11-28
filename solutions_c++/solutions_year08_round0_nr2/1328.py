#include <cstdio>
#include <cassert>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#define sz(x) ((int)(x.size()))
//#pragma comment(linker, "/STACK:10000000")
using namespace std;
typedef long long lint;
const int MAXN = 100;

int Calc(multiset<int> A, multiset<int> B) {
	int ret = 0;
	while (B.size() > 0 && A.size() > 0) {
		int x = *(B.begin());
		if (*(A.begin()) <= x) {
			A.erase(A.begin());
		}
		else {
			++ret;
		}
		B.erase(B.begin());
	}
	return ret + (int)B.size();
}

void Solve(int num) {
	int T, NA, NB;
	scanf("%d %d %d", &T, &NA, &NB);
	int h, m;
	multiset<int> A1, B1, A2, B2;
	for (int i = 0; i < NA; ++i) {
		scanf("%d:%d", &h, &m);
		A1.insert(h * 60 + m);
		scanf("%d:%d", &h, &m);
		A2.insert(h * 60 + m + T);
	}
	for (int i = 0; i < NB; ++i) {
		scanf("%d:%d", &h, &m);
		B1.insert(h * 60 + m);
		scanf("%d:%d", &h, &m);
		B2.insert(h * 60 + m + T);
	}
	int na = Calc(B2, A1);
	int nb = Calc(A2, B1);
	printf("Case #%d: %d %d\n", num, na, nb);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i)
		Solve(i);	
	return 0;
}
