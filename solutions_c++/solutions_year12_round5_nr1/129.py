#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <stdio.h>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;
typedef pair<int, int> pii;
typedef vector<int> vint;

struct man {
	int l, p, num;
};

int N;
man F[1009];

bool comp(man a, man b) {
	if (a.l * b.p == b.l * a.p)
		return a.num < b.num;
	else
		return a.l * b.p < b.l * a.p;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int I = 1; I <= T; ++I) {
		cin >> N;
		for (int i = 0; i < N; ++i) {
			F[i].num = i;
			cin >> F[i].l;
		}
		for (int i = 0; i < N; ++i) {
			cin >> F[i].p;
		}

		sort(F, F + N, comp);

		printf("Case #%d:", I);
		for (int i = 0; i < N; ++i) {
			printf(" %d", F[i].num);
		}
		printf("\n");
	}
	return 0;
}
