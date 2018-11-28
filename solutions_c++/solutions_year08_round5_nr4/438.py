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

lint h,w,y,x;
vector<pair<lint, lint> > o;

int r;
int sav[128][128];
#define BASE 10007
//lint g(int w, int h) {
//	if(w <=2 && h <=2) return 0;
//	if((w + h - 2) %3 != 0) return 0;
//	int t = 
//}
//
//lint f(int mask) {
//	lint ret = 0;
//
//}

int doit(int i,int j){
	if(i > h || j > j) return 0;
	if(i == h && j == w) return 1;
	if(sav[i][j] != -1) return sav[i][j];
	REP(k,sz(o)) if(o[k].X == j && o[k].Y == i) return 0;
	int t = doit(i+1,j+2) + doit(i+2,j+1);
	t %=BASE;
	sav[i][j] = t;
	return t;
}

int main() {
	freopen("d-small-attempt0.in","r",stdin);
	freopen("d.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	FOR(tn,1,tc+1) {
		scanf("%lld %lld %lld",&h,&w,&r);
		o.clear();
		REP(i,r){
			scanf("%lld %lld",&y, &x);
			o.pb(mp(x,y));
		}
		sort(all(o));
		lint ans = 0;
		//REP(i,(1<<r)) ans = (ans + f(i)) % BASE;
		memset(sav,-1,sizeof(sav));
		ans = doit(1, 1);
		printf("Case #%d: %lld\n",tn,ans);
		// Case #%d !!!!!!!!
	}
	fflush(stdout);
	return 0;
}