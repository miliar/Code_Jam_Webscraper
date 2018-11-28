#define _CRT_SECURE_NO_DEPRECATE
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

#define DIM 128
int a[DIM][DIM], b[DIM][DIM], q[DIM], t[DIM];

bool dfs(int v, int n) {
	if(t[v]) return false;
	t[v] = true;
	REP(i, n) if(b[v][i]) {
		if(q[i] == -1 || dfs(q[i], n)) {
			q[i] = v;
			return true;
		}
	}
	return false;
}

int mm(int n) {
	memset(q,-1,sizeof(q));
	int ans = 0;
	REP(i,n) {
		memset(t,0,sizeof(t));
		if(dfs(i, n)) ++ans;
	}
	return ans;
}
int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int tc;
	scanf("%d",&tc);
	REP(ttt, tc) {
		int n, s;
		scanf("%d %d",&n,&s);
		memset(b,0,sizeof(b));
		REP(i, n) REP(j, s) scanf("%d",&a[i][j]);
		REP(i, n) REP(j, n) {
			bool f = true;
			REP(k, s) if(a[i][k] >= a[j][k]) {
				f = false;
				break;
			}
			if(f) b[i][j] = 1;
		}
		int ans = n - mm(n);
		printf("Case #%d: %d\n",ttt+1,ans);
	}

	fclose(stdout);
	return 0;
}