#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
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

#define N 1024
int x[N], v[N];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	FOR(tt, 1, tc+1) {
		int ans = 0, n, k, b, t;
		scanf("%d%d%d%d", &n, &k, &b, &t);
		REP(i, n) scanf("%d", &x[i]);
		REP(i, n) scanf("%d", &v[i]);
		
		int bad_at_right = 0;
		for(int i = n-1; i >= 0; --i) {
			bool ok = (b - x[i] <= lint(t) * v[i]);
			if(!ok) ++bad_at_right;
			if(k > 0 && ok) {
				ans += bad_at_right;				
				--k;
			}
			
		}
		if(k <= 0)
			printf("Case #%d: %d\n", tt, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", tt);
	}
	return 0;
}