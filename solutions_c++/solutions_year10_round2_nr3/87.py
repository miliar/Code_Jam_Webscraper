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

#define N 512

const int BASE = 100003;

int sav[N][N];
lint C[N][N];

lint cnk(int n, int k) {
	if(n < 0 || k < 0) return 0;
	if(n == 0) return (k == 0);
	if(C[n][k] != -1) return C[n][k];
	return C[n][k] = (cnk(n-1, k-1) + cnk(n-1, k)) % BASE;
}


int f(int n, int k) {
	if(n <= 1) return 0;
	// n > 1	
	if(k == 0) return 0;
	if(k == 1) return 1;
	// k > 1
	if(sav[n][k] != -1) return sav[n][k];
	lint ret = 0;
	REP(i, k) {
		ret = (ret + f(k, i) * cnk(n-k-1, k-i-1)) % BASE;
	}
	return sav[n][k] = ret;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);

	memset(sav, -1, sizeof(sav));
	memset(C, -1, sizeof(C));

	//while(1) {
	//	int n, k;
	//	cin >> n >> k;
	//	cout << f(n, k) << endl;
	//}

	int tc;
	scanf("%d", &tc);
	FOR(tt, 1, tc+1) {
		int n;
		scanf("%d", &n);
		int ans = 0;
		REP(i, n) ans = (ans + f(n, i)) % BASE;
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}