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
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii; 
typedef vector<pii> vpii; 
typedef long long lint;
const int MAXN = 100;
const double eps = 1e-8;
const double pi = acos(-1.0);

vector<lint> X, Y;

void Gen(lint n, lint A, lint B, lint C, lint D, lint x0, lint y0, lint M) {
	X.clear();
	Y.clear();
	lint x = x0, y = y0;
	X.pb(x);
	Y.pb(y);
	for (int i = 1; i < n; ++i) {
		x = (A * x + B) % M;
		y = (C * y + D) % M;
		X.pb(x);
		Y.pb(y);
	}
}

void Solve(int num) {
	printf("Case #%d: ", num);
	lint n, A, B, C, D, x0, y0, M;
	cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
	Gen(n, A, B, C, D, x0, y0, M);
	int cnt = 0;	
	for (int i = 0; i < n; ++i)
		for (int j = i + 1; j < n; ++j)
			for (int k = j + 1; k < n; ++k) {
				lint x = X[i] + X[j] + X[k];
				lint y = Y[i] + Y[j] + Y[k];
				if (x % 3 == 0 && y % 3 == 0) ++cnt;
			}
	printf("%d\n", cnt);
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

