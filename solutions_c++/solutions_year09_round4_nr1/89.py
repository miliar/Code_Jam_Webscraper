#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <climits>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define clr(x) memset(x,0,sizeof(x)) 

const int N = 1000;

int mat[50][50];
int *pos[50];
int n;
int cas = 1;

bool check(int i, int k) {
	for(int j = k + 1; j < n; j++)
		if(pos[i][j])return false;
	return true;
}

void solve() {
	cin >> n;
	string inp;
	for(int i = 0; i < n; i++) {
		pos[i] = mat[i];
		cin >> inp;
		for(int j = 0; j < n; j++)
			mat[i][j] = inp[j] - '0';
	}

	int ans = 0;
	for(int i = 0; i < n; i++) {
		if(check(i, i))continue;

		for(int j = i + 1; j < n; j++) {
			if(check(j, i)) {
				ans = ans + j - i;
				for(int k = j; k > i; k--)
					swap(pos[k], pos[k-1]);
				break;
			}
		}
	}
	printf("Case #%d: %d\n", cas++, ans);
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	while(T--)solve();

	return 0;
}

/*Powered By Lynn-Beta1*/