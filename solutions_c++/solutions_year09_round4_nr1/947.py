#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define foreach(i, S) \
	for (typeof((S).begin()) i = (S).begin(); i != (S).end(); i++)

#define watch(x) cout << #x " = " << x << "\n"

typedef unsigned long long llu;
typedef long long ll;
typedef unsigned nat;

#define NMAX 64

int n;
llu A[NMAX];

int make(int k) {
	int out = 0;
	if ((A[k] % (1llu<<(n-1-k))) > 0) {
		for (int i = k+1; i < n; i++) {
			if ((A[i] % (1llu<<(n-1-k))) == 0) {
				for (int j = i; j > k; j--) {
					swap(A[j], A[j-1]);
					out++;
				}
				i = n;
			}
		}
	}
	return out;
}

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		printf("Case #%d: ", test+1);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char s[NMAX];
			scanf("%s", s);
			A[i] = 0;
			for (int j = 0; j < n; j++) {
				A[i]+= (llu) (s[j]-'0')<<(n-1-j);
			}
		}
		int out = 0;
		for (int i = 0; i < n; i++) {
			out+= make(i);
		}
		printf("%d\n", out);
		/*for (int i = 0; i < n; i++) {
			printf("%llu\n", A[i]);
		}*/
	}
	return 0;
}

