#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define debug 0
#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define Rep(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define pb push_back
#define mp make_pair
#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define cp(a) cerr << "(" << #a << "," << a << ") "
#define cen cerr << endl

typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int inf = 0x7fffffff;

const int Size = 1000 * 1000 + 1;
char buffer[Size];

int solution(int nTest) {
	printf("Case #%d: ", nTest + 1);
	int n, s;
	scanf("%d%d", &n, &s);
	int p;
	scanf("%d", &p);
	vector<int> ar[3];
	For(i, 0, n) {
		int t;
		scanf("%d", &t);
		ar[t % 3].pb(t / 3);
	}
	int res = 0;
	For(i, 0, sz(ar[2])) {
		if(ar[2][i] + 1 >= p) {
			res++;
		}
		else {
			if(ar[2][i] + 2 >= p && s > 0) {
				res++;
				s--;
			}
		}
	}
	For(i, 0, sz(ar[1])) {
		if(ar[1][i] + 1 >= p) {
			res++;
		}
	}
	For(i, 0, sz(ar[0])) {
		if(ar[0][i] >= p) {
			res++;
		}
		else if(ar[0][i] + 1 >= p && s > 0 && ar[0][i] >= 1) {
			s--;
			res++;
		}
	}
	printf("%d\n", res);


	return 1;
}

int main() {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);


	int i = 0, n = 99999;
	scanf("%d", &n);
	while(i < n && solution(i)) {
		i++;
	}

	return 0;
}
