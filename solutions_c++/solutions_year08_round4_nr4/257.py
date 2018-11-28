#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#pragma comment(linker, "/STACK:10000000")
#define For(i,l,h) for (int i = (l); i < (h); ++i)
#define ForU(i,l,h) for (int i = (l); i <= (h); ++i)
#define tr(T, v, it) for (T::iterator it = v.begin(); it != v.end(); ++it) 
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs; 
typedef pair<int,int> pii; 
typedef vector<pii> vpii; 
typedef map<string, int> msi;
typedef long long lint;
const int MAXN = 100;
const double eps = 1e-8;
const double pi = acos(-1.0);

void Solve(int num) {
	printf("Case #%d: ", num);
	int k;
	string s, t;
	cin >> k >> s;
	t = s;
	int n = sz(s);
	int g = n / k;
	vi p(k);
	For (i, 0, k) p[i] = i;
	int ans = 1 << 30;
	do {
		for (int l = 0; l < g; ++l) {
			for (int i = 0; i < k; ++i) {
				t[i + l * k] = s[p[i] + l * k];
			}
		}
		int c = 1;
		for (int i = 1; i < n; ++i) {
			if (t[i] != t[i - 1]) ++c;			
		}
		ans = min(ans, c);
	} while (next_permutation(all(p)));
	printf("%d", ans);
	printf("\n");
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif	
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) Solve(i);
	return 0;
}

