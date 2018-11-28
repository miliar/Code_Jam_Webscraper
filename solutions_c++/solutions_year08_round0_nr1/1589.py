#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) FOR(i,0,(n)-1)
#define FS(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) ((int)(a).size())
#define MK make_pair
#define FI first
#define SE second
typedef long long ll;
typedef long double ldouble;
int N, S, Q, dp[1005][105], nast[105], nr[1005], mini[1005];
string nazwy[105], zapy[1005];
char wej[105];
void lecim(int nur) {
	scanf("%d\n",&S);
	for(int i = 0; i < S; ++i) {
		fgets(wej, sizeof(wej), stdin);
		wej[strlen(wej)-1] = 0;
		nazwy[i] = wej;
//		cout << i << ": " << nazwy[i] << "\n";
	}
	scanf("%d\n",&Q);
	for(int i = 0; i < Q; ++i) {
		fgets(wej, sizeof(wej), stdin);
		wej[strlen(wej)-1] = 0;
		zapy[i] = wej;
//		cout << i << ": " << zapy[i] << "\n";
		for(int j = 0; j < S; ++j) if(nazwy[j] == zapy[i]) {
			nr[i] = j;
			break;
		}
	}
	if(Q == 0) {
		printf("Case #%d: %d\n", nur, 0);
		return ;
	}
	for(int i = 0; i < S; ++i) {
		if(nr[Q - 1] == i) {
			dp[Q - 1][i] = 10000;
			nast[i] = Q - 1;
		} else {
			dp[Q - 1][i] = 0;
			nast[i] = Q;
		}
		mini[Q - 1] = 0;
	}
	for(int i = Q - 2; i >= 0; --i) {
		mini[i] = 10000;
		for(int j = 0; j < S; ++j) {
			if(j == nr[i]) {
				dp[i][j] = 10000;
				nast[j] = i;
			} else {
				if(nast[j] == Q) dp[i][j] = 0;
				else dp[i][j] = mini[nast[j]] + 1;
			}
			mini[i] = min(mini[i], dp[i][j]);
		}
	}
	printf("Case #%d: %d\n", nur, mini[0]);
}
int main() {
	scanf("%d",&N);
	for(int ti = 0; ti < N; ++ti) lecim(ti + 1);
	return 0;
}
