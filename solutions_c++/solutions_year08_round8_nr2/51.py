#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <numeric>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define ss stringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vii vector<pii>
#define vs vector<string>
#define LD long double

using namespace std;

int C[300];
int A[300];
int B[300];
int n;

int solve(int x, int y, int z) {
	vii v;
	fr(i, n) if(C[i] == x || C[i] == y || C[i] == z) {
		v.pb(mp(A[i], B[i]));
	}
	sort(v.begin(), v.end());
	int p = 1;
	int i = 0;
	int kiek = 0;
	while(p <= 10000) {
		vi E;
		while(i < sz(v) && v[i].st <= p) {
			 if(v[i].nd >= p) E.pb(v[i].nd);
			 i++;
		}
		sort(E.begin(), E.end());
		if(!sz(E)) return beg;
		//if(E[sz(E) - 1] <= p) return beg;
		p = E[sz(E) - 1] + 1;
		kiek++;
	}
	return kiek;
}

void solveCase(int Case) {
	memset(A, -1, sizeof(A));
	memset(B, -1, sizeof(B));
	memset(C, -1, sizeof(C));
	cin >> n;
	map<string, int> M;
	int cnt = 0;
	fr(i, n) {
		string s;
		int a, b;
		cin >> s >> a >> b;
		A[i] = a;
		B[i] = b;
		if(M.find(s) == M.end()) M[s] = cnt++;
		C[i] = M[s];		
	}
	int m = cnt;
	int mn = beg;
	fr(i, m) fr(j, i + 1) fr(k, j + 1) mn <?= solve(i, j, k);
	if(mn == beg) cout << "Case #" << Case << ": IMPOSSIBLE" << endl;
	else cout << "Case #" << Case << ": " << mn << endl;
}

int main() {
	freopen("in2.in", "r", stdin);
	freopen("out2.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int i = 0; i < tests; i++) solveCase(i + 1);
	return 0;
}
