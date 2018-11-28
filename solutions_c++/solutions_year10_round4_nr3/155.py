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


#define DIM 110

char a[DIM][DIM], b[DIM][DIM];

bool empty() {
	REP(i, DIM) REP(j, DIM) if(a[i][j]) return false;
	return true;
}
int main() {
	//freopen("3.txt", "r", stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);


	int tc;
	scanf("%d", &tc);
	FOR(tt, 1, tc+1) {
		int n;
		scanf("%d", &n);
		memset(a, 0, sizeof(a));

		REP(i, n) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			--x1;
			--y1;
			FOR(j, x1, x2) {
				FOR(k, y1, y2) {
					a[k+1][j+1] = 1;
				}
			}
		}
		

		int ans = 0;

		while(!empty()) {
			memset(b, 0, sizeof(b));
			FOR(i, 1, DIM) {
				FOR(j, 1, DIM) {
					if(a[i][j]) {
						b[i][j] = a[i-1][j] || a[i][j-1];
					}
					else {
						b[i][j] = a[i-1][j] && a[i][j-1];
					}
				}
			}
			memcpy(a, b, sizeof(a));
			++ans;
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}