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
	lint N, M, A;
	cin >> N >> M >> A;
	printf("Case #%d: ", num);
	for (lint x1 = 0; x1 <= N; ++x1)
	for (lint x2 = 0; x2 <= N; ++x2)
	for (lint y1 = 0; y1 <= M; ++y1)
	for (lint y2 = 0; y2 <= M; ++y2)
	//ForU (x1, 0, N) ForU (x2, 0, N) ForU (y1, 0, M) ForU (y2, 0, M) 
	{
		lint t = x1 * y2 - x2 * y1;
		if (t < 0) t = -t;
		if (t == A) {
			printf("0 0 %lld %lld %lld %lld\n", x1, y1, x2, y2);		
			return;
		}
	}	
	printf("IMPOSSIBLE\n");
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

