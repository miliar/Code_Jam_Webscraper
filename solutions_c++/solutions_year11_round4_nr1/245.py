/*
 * a.cpp
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
typedef pair<int,int> PII;

#define SS stringstream
template<typename T> string tos(T q,int w=0){SS
A;A.flags(ios::fixed);A.precision(w);A<<q;string s;A>>s;return s;}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T > s2v(string s){SS A(s);vector<T > ans;while(A&&!A.eof()){T t;A>>t;ans.pb(t);}return ans;}

// end of pre-inserted code

int main() {
	freopen("A-large.in","r", stdin);
	freopen("A-large.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	FOR(test, 1, tc+1) {
		int x, s, r, t, n;
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		VI a;
		REP(i, n) {
			int b, e, w;
			scanf("%d%d%d",&b,&e,&w);
			FOR(j, b, e) {
				a.pb(w);
			}
		}
		while(sz(a) < x) {
			a.pb(0);
		}
		sort(all(a));
		double ans = 0;
		double tt = t;
		REP(i, sz(a)) {
			if(tt > 1e-9) {
				double dd = 1.0 / (r + a[i]);
				if(dd <= tt) {
					ans += dd;
					tt -= dd;
				}
				else {
					double x = (r + a[i]) * tt;
					ans += tt;
					ans += (1 - x) / (s + a[i]);
					tt = 0;
				}
			}
			else {
				ans += 1.0 / (s + a[i]);
			}
		}
		printf("Case #%d: %.9lf\n", test, ans);
	}
	return 0;
}
