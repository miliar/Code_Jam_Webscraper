#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <string>
#include <vector>
#define REP(i,n)	for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,s,k)	for(int i=(s),_k=(k);i<=_k;++i)
#define FORD(i,s,k)	for(int i=(s),_k=(k);i>=_k;--i)
#define FORE(it,q)	for(__typeof((q).begin())it=(q).begin();it!=(q).end();++it)
using namespace std;
const int max_S = 110, max_Q = 1010;

int main()
{
	int TT,S,Q;
	map<string,int> M;
	int d[max_Q][max_S];
	char buf[200];
	scanf("%d\n",&TT);
	FOR(cs,1,TT) {
        M.clear();
        scanf("%d\n",&S);
        REP(i,S) {
            gets(buf);
            M[string(buf)] = i;
        }
        scanf("%d\n",&Q);
        vector<int> V;
        REP(i,Q) {
            gets(buf);
            V.push_back(M[string(buf)]);
        }
        REP(i,Q+1) REP(j,S) d[i][j] = max_Q;
        REP(i,S) d[0][i] = 0;
        FOR(i,1,Q) {
            REP(j,S) REP(k,S) {
                if(k != V[i-1]) {
                    d[i][k] <?= 1 - (j==k) + d[i-1][j];
                }
            }
        }
        int res = INT_MAX;
        REP(i,S) res <?= d[Q][i];
		printf("Case #%d: %d\n", cs, res);
	}
}
