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
vi Primes;

bool IsPrime(int x) {
	for (int i = 2; i * i <= x; ++i)
		if (x % i == 0) return false;
	return true;
}

void Init() {
	for (int i = 2; i <= 1000; ++i)
		if (IsPrime(i)) Primes.pb(i);
}

bool Check(int a, int b, int p) {
	for (int i = 0; i < sz(Primes); ++i) {
		int t = Primes[i];
		if (t < p) continue;
		if (a % t == 0 && b % t == 0) return true;
	}
	return false;
}
int A, B, P;
vvi G;
vi Use;

void Visit(int u) {
	Use[u] = true;
	For (i, 0, sz(G[u])) {
		int v = G[u][i];
		if (Use[v]) continue;
		Visit(v);
	}
}

void Solve(int num) {
	printf("Case #%d: ", num);
	cin >> A >> B >> P;
	G.assign(B + 1, vi());

	for (int i = A; i <= B; ++i)
		for (int j = i + 1; j <= B; ++j) 
			if (Check(i, j, P)) {
				G[i].pb(j);
				G[j].pb(i);
			}
	int ans = 0;
	Use.assign(B + 1, 0);
	for (int i = A; i <= B; ++i)
		if (!Use[i]) {
			Visit(i);
			++ans;
		}

	printf("%d\n", ans);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif	
	Init();
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i)
		Solve(i);	
	return 0;
}

