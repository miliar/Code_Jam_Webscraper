// compiled by MSVS 2005 Team Suite in Release mode
// runned on Asus EEE PC 700
#define _CRT_SECURE_NO_DEPRECATE
#include<vector>
#include<string>
//#include<set>
//#include<map>
//#include<queue>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<cmath>

using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define all(X) (X).begin(),(X).end()
#define FOR(I,S,N) for(int I=(S);I<(N);++I)
#define REP(I,N) FOR(I,0,N)
#define mp make_pair
#define X first
#define Y second

#define SS stringstream
template<typename T> string tos(T q,int w=0){SS A;A.flags(ios::fixed);A.precision(w);A<<q;string s;A>>s;return s;}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T > s2v(string s){SS A(s);vector<T > ans;while(A&&!A.eof()){T t;A>>t;ans.pb(t);}return ans;}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<string> VS;

#define DIM 16384
int g[DIM],u[DIM],l[DIM];
int cc;
int n,m;
char buf[128];
int a[16];
int len(int x){
	int r = 0;
	while(x>0){
		r += (x%2);
		x /= 2;
	}
	return r;
}
bool good(int x){
	while(x > 0) {
		if((x & 3) == 3) return false;
		x /= 2;
	}
	return true;
}

int up(int x){
	int ret = 0;
	REP(i,m) if(x & (1<<i)) {
		if(i<m-1) ret = ret  |(1<<(i+1));
		if(i > 0) ret = ret |  (1<<(i-1));
	}
	return ret;
}
bool was[11][1024];
int sav[11][1024];
#define INF 10000

int f(int row, int mask){
	if((mask & a[row]) != 0) return -INF;
	if(row == 0) {
		return l[mask];
	}
	if(was[row][mask]) return sav[row][mask];
	int y = u[mask];
	int ans = -INF;
	REP(i,cc){
		if((g[i] & y) == 0){
			ans = max(ans, f(row-1, g[i]) );
		}
	}
	ans += l[mask];
	was[row][mask] = 1;
	sav[row][mask] = ans;
	return ans;
}

int main() {
	//freopen("c.txt","r",stdin);

	freopen("c-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	FOR(tn,1,tc+1) {
		scanf("%d %d ",&n,&m);
		//a.clear();
		REP(i,n) {
			scanf("%s ",buf);
			int t = 0; 
			REP(j,m) t = 2*t + (buf[j] == 'x'); 
			a[i] = t;
		}
		cc = 0;
		REP(i,1<<m) if(good(i)){
			g[cc] = i;
			u[i] = up(i);
			l[i] = len(i);
			++cc;
		}
		memset(was,0,sizeof(was));
		int ans = 0;
		REP(i,cc){
			ans = max(ans, f(n-1, g[i]));
		}
		printf("Case #%d: %d\n",tn,ans);
		// Case #%d !!!!!!!!
	}
	fflush(stdout);
	return 0;
}