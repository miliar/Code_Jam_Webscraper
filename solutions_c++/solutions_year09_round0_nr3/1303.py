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

#define DIM 10240
int len;
char s[DIM];
char x[20] = {"welcome to code jam"};
int sav[DIM][20];

int f(int i, int j) {
	if(j == 0) return 1;
	if(i == 0) return 0;
	// i > 0, j > 0
	if(sav[i][j] != -1) return sav[i][j];
	int ans = f(i-1, j);
	if(s[i-1] == x[j-1]) ans += f(i-1, j-1);
	ans = ans % 10000;
	return sav[i][j] = ans;
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int tc;
	gets(s);
	sscanf(s,"%d",&tc);
	REP(ttt,tc) {
		gets(s);
		len = strlen(s);
		
		memset(sav,-1,sizeof(sav));
		int ans = f(len, 19);
		printf("Case #%d: %04d\n",ttt+1,ans);
	}
	fclose(stdout);
	return 0;
}