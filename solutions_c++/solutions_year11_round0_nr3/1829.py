#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

//#define debug

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long lint;

const int inf = 0x7fffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 20000;

char buffer[Size];

int solution(int nTest) {
	int n;
	scanf("%d", &n);
	lint sum = 0;
	int r = inf;
	lint res = 0;
	For(i, 0, n) {
		int t;
		scanf("%d", &t);
		r = min(t, r);
		sum += t;
		res ^= t;
	}

	printf("Case #%d: ", nTest + 1);

	if(res) {
		printf("NO\n");
	}
	else {
		printf("%d\n", (int)(sum - r));
	}
		


	return 1;
}


int main() {
	freopen("input.txt", "r", stdin);
#ifndef debug
	freopen("output.txt", "w", stdout);
#endif

	int i = 0, n = 999999;

	scanf("%d", &n);
	
	while(i < n && solution(i))
		i++;

	return 0;
}

