#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<cstring>

// Felix J's AI v1.0
#define FOR(i,a,b) for(int i=(a),_n=(b); i<=_n; i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n; i--)
#define FILL(i,v) memset((i),(v),sizeof((i)))
#define DEBUG(x) cout << "  >> " << #x << " => " << x <<endl

using namespace std;
typedef long long LL;

inline void OFILE(string f) {
	string in = f + ".in";
	freopen( in.c_str(), "r", stdin);
	string out = f + ".out.txt";
	freopen( out.c_str(), "w", stdout);
}
bool pris[10003];
int arr[105], dig[10];;
int calc(int N, int prev, int maxN) {

}

int main() {
	OFILE("Csmall1");
	int ntc;
	scanf("%d", &ntc);
	FOR(TC, 1, ntc) {
		memset(pris, 0, sizeof(pris));
		int P,Q;
		scanf("%d %d", &P, &Q);
		FOR(i,1,P) pris[i] = 1;
		REP(i,Q) {
			dig[i] = i;
			scanf("%d", &arr[i]);
		}
		int ans = ( 1<<29 );
		do {
			int curans = 0;
			FOR(i,1,P) pris[i] = 1;
			REP(i,Q) {
				int now = arr[dig[i]], count = 0;
				pris[now] = 0;
				for(int k=now-1; k>0 && pris[k]; k--, count++);
				for(int k=now+1; k<=P && pris[k]; k++, count++);
				curans += count;
			}
			ans <?= curans;
		} while( next_permutation(dig,dig+Q) );
		printf("Case #%d: %d\n",TC, ans);
	}
	// system("pause");
	return 0;
}
