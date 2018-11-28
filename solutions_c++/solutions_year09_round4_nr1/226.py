#define _CRT_SECURE_NO_DEPRECATE
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<numeric>
#include<iostream>
#include<sstream>
#include<complex>
#include<cmath>
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

char s[DIM][DIM];
int a[DIM];

int need(char s[]) {
	int len = strlen(s);
	int ans = 0;
	REP(i, len) if(s[i] == '1') ans = max(ans, i);
	return ans;
}

int main() {
	//freopen("1.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int tc;
	scanf("%d",&tc);
	REP(ttt, tc) {		
		cerr << "test " << (ttt+1) << "..." << endl;
		
		int n;
		scanf("%d ",&n);
		REP(i, n){
			scanf("%s ", s[i]);
			a[i] = need(s[i]);
		}

		int ans = 0;
		REP(i, n) {
			int p = i;
			while(p < n && a[p] > i) ++p;
			for(int j = p; j > i; --j) {
				swap(a[j], a[j-1]);
				++ans;
			}
		}

		printf("Case #%d: %d\n",ttt+1, ans);
	}

	fclose(stdout);
	return 0;
}