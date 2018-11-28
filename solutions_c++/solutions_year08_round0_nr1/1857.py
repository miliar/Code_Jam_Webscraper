#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#define REP(i,n) for (int i=0;i<(n);i++) 
using namespace std;

int S, Q;
map<string, int> M;
char buf[500];
int top;
int seq[1005];
int f[1000 + 5][100 + 5];

int
main()
{
	int T;
	scanf("%d", &T);
	REP(t,T) {
		M.clear();
		printf("Case #%d: ", t + 1);
		scanf("%d", &S); fgets(buf, sizeof buf, stdin);
		REP(s,S) {
			fgets(buf, sizeof buf, stdin);
			M.insert(make_pair(buf, s));
		}
		scanf("%d", &Q); fgets(buf, sizeof buf, stdin);
		REP(q,Q) {
			fgets(buf, sizeof buf, stdin);
			seq[q] = M.find(buf)->second;
		}
		//REP(q,Q) printf("%d ", seq[q]); puts("");
		memset(f[Q], 0, sizeof f[Q]);
		for ( int q = Q - 1; q >= 0; q-- ) {
			for ( int s = 0; s < S; s++ ) {
				f[q][s] = 1 << 30;
				for ( int i = 0; i < S; i++ ) {
					if ( i != seq[q] ) {
						f[q][s] <?= (s != i) + f[q + 1][i];
					}
				}
			}
		}
		//REP(s,S) printf("%d ", f[0][s]); puts("");
		printf("%d\n", *min_element(f[0], f[0] + S));
	}
}
