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
const int MOD = 10007;
vvi A, Del;
int H, W;


int rec(int i, int j) {
	if (i >= H || j >= W) return 0;
	if (A[i][j] != -1) return A[i][j];
	if (Del[i][j]) return A[i][j] = 0;
	if (i == H - 1 && j == W - 1) return A[i][j] = 1;
	int t1 = rec(i + 1, j + 2);
	int t2 = rec(i + 2, j + 1);
	return A[i][j] = (t1 + t2) % MOD;
}

void Solve(int num) {
	printf("Case #%d: ", num);
	int R;
	cin >> H >> W >> R;
	A.assign(H, vi(W, -1));
	Del.assign(H, vi(W, 0));
	while (R--) {
		int i, j;
		cin >> i >> j;
		--i; --j;
		Del[i][j] = true;
	}
	int ans = rec(0, 0);
	printf("%d", ans);
	printf("\n");	
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) Solve(i);
	return 0;
}

