#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std; 

#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define forit(it,S) for(typeof(S.begin()) it = S.begin(); it != S.end(); ++it)

int a, b;
int c[10], cn;
set <pair <int, int> > S;

int calc(int n) {
	int res = 0;
	cn = 0;
	int nn = n;
	while (nn > 0) {
		c[cn++] = nn % 10;
		nn /= 10;
	}
	S.clear();
	reverse(c, c + cn);
	for (int i = 1; i < cn; ++i) if (c[i] > 0) {
		int m = 0;
		int j = i;
		for (int k = 0; k < cn; ++k) {
			m = m * 10 + c[j];
			++j;
			if (j == cn) j = 0;
		}
		if (m > n && m <= b && m >= a) {
			S.insert(mp(n, m));
		}
	}
	return (int)S.size();
}

int main() {
	int tests;
	scanf("%d", &tests);
	for (int casenum = 1; casenum <= tests; ++casenum) {
		cin >> a >> b;
		printf("Case #%d: ", casenum);
		int res = 0;
		for (int i = a; i < b; ++i) {
			res += calc(i);
		}
		cout << res << endl;
	}
	return 0;		
}

