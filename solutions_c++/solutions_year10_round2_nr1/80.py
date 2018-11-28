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

#define DIM (1024*100)

map<string, int> tree[DIM];
int ptr, cc;

void clr(int v) {
	while(sz(tree[v]) > 0)	tree[v].erase(tree[v].begin());
}
void init() {
	ptr = 1;
	cc = 1;
	clr(0);
}

void dfs(int v, const vector<string> &t, int i) {
	if(i == sz(t)) return;
	if(tree[v].find(t[i]) == tree[v].end()) {
		clr(ptr);
		tree[v][t[i]] = ptr++;
		++cc;
	}
	dfs(tree[v][t[i]], t, i+1);
}

void add(string s) {
	REP(i, sz(s)) if(s[i] == '/') s[i] = ' ';
	vector<string> t = s2v<string>(s);
	dfs(0, t, 0);
}

char buf[1024*1024];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	FOR(tt, 1, tc+1) {
		init();
		int n, m;
		scanf("%d %d", &n, &m);
		REP(i, n) {
			scanf(" %s", buf);
			add(buf);
		}
		int has = cc;
		REP(i, m) {
			scanf(" %s", buf);
			add(buf);
		}
		printf("Case #%d: %d\n", tt, cc - has);
	}
	return 0;
}