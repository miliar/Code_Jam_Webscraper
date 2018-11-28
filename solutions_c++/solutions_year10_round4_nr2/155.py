#define _CRT_SECURE_NO_DEPRECATE
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<algorithm>
#include<numeric>
#include<iostream>
#include<sstream>
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
#define PRV(X) {cout<<#X<<" = {";int __prv;REP(__prv,sz(X)-1) cout<<(X)[__prv]<<",";cout<<(X).back()<<"}"<<endl;}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define SS stringstream
template<typename T> string tos(T q,int w=0){SS A;A.flags(ios::fixed);A.precision(w);A<<q;string s;A>>s;return s;}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T > s2v(string s){SS A(s);vector<T > ans;while(A&&!A.eof()){T t;A>>t;ans.pb(t);}return ans;}

// end of pre-inserted code

#define DIM 2048

int a[DIM];
int c[DIM][DIM], code[DIM][DIM];
//PII decode[DIM];
int n;

const lint INF = 1000000000;

lint sav[2*DIM][16];

lint f(int rnd, int p, int k) {
	if(rnd == -1) {
		if(a[p] >= n-k) return 0;		
		return INF;
	}
	if(sav[code[rnd][p]][k] != -1)
		return sav[code[rnd][p]][k];

	lint ret = f(rnd-1, 2*p, k) + f(rnd-1, 2*p+1, k);
	lint ret2 = f(rnd-1, 2*p, k+1) + f(rnd-1, 2*p+1, k+1) + c[rnd][p];
	return sav[code[rnd][p]][k] = min(ret, ret2);
}

int main() {
	//freopen("2.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);


	int tc;
	scanf("%d", &tc);
	FOR(tt, 1, tc+1) {
		scanf("%d", &n);
		REP(i, 1<<n) scanf("%d", &a[i]);		
		int cnt = 0;
		REP(i, n) {
			REP(j, (1<<n) / (1<<(i+1))) {
				scanf("%d", &c[i][j]);
				code[i][j] = cnt;
				//decode[cnt] = mp(i, j);
				++cnt;
			}
		}
		
		memset(sav, -1, sizeof(sav));

		lint ans = f(n-1, 0, 0);


		printf("Case #%d: %d\n", tt, (int)ans);
	}
	return 0;
}