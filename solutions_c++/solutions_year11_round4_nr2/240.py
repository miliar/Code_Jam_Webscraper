/*
 * b.cpp
 *
 *  Created on: Jun 4, 2011
 *      Author: dkorduban
 */

#include<algorithm>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<numeric>
#include<iostream>
#include<sstream>
#include<cstdio>
using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(I,S,N) for(int I=(S);I<(N);++I)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";REP(__prv,sz(X)-1)cout<<(X)[__prv]<<",";cout<<(X).back()<<"}"<<endl;}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define SS stringstream
template<typename T> string tos(T q, int w = 0) {
	SS A;
	A.flags(ios::fixed);
	A.precision(w);
	A << q;
	string s;
	A >> s;
	return s;
}
template<typename T> T sto(string s) {
	SS A(s);
	T t;
	A >> t;
	return t;
}
template<typename T> vector<T> s2v(string s) {
	SS A(s);
	vector<T> ans;
	while (A && !A.eof()) {
		T t;
		A >> t;
		ans.pb(t);
	}
	return ans;
}

// end of pre-inserted code

int a[512][512];
void init(int i0, int j0, int k, lint &sumx, lint &sumy) {
	int mul, delta;
	if (k % 2) {
		// odd
		mul = k / 2;
		delta = 1;
	} else {
		// even
		mul = k - 1;
		delta = 2;
	}
	int muly = mul;
	sumx = sumy = 0;
	FOR(i, i0, i0 + k) {
		int mulx = mul;
		FOR(j, j0, j0 + k) {
			sumx += mulx * a[i][j];
			sumy += muly * a[i][j];
			mulx -= delta;
		}
		muly -= delta;
	}
	sumx -= mul * a[i0][j0];
	sumx -= mul * a[i0 + k - 1][j0];
	sumx -= -mul * a[i0][j0 + k - 1];
	sumx -= -mul * a[i0 + k - 1][j0 + k - 1];

	sumy -= mul * a[i0][j0];
	sumy -= mul * a[i0][j0 + k - 1];
	sumy -= -mul * a[i0 + k - 1][j0];
	sumy -= -mul * a[i0 + k - 1][j0 + k - 1];
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	FOR(test, 1, tc+1) {
		int r, c, d;
		scanf("%d%d%d ", &r, &c, &d);
		REP(i, r) {
			REP(j, c) {
				char ch;
				scanf("%c", &ch);
				a[i][j] = ch - '0';
			}
			scanf(" ");
		}

		int ans = -1;
		FOR(k, 3, min(r, c)+1) {
			REP(i, r - k + 1) {
				REP(j, c - k + 1) {
					lint sumx, sumy;
					init(i, j, k, sumx, sumy);
					if (sumx == 0 && sumy == 0) {
						//						cerr << i << " " << j << endl;
						ans = k;
						//						goto br;
					}
				}
			}
		}

		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", test);
		} else {
			printf("Case #%d: %d\n", test, ans);
		}
	}
	return 0;
}
