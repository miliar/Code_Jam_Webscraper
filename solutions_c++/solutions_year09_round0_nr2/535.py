#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<cmath>
#include<algorithm>
#include<set>
using namespace std;

#define sz(q) ((int)(q).size())
#define _fill(mem,v) memset(mem,v,sizeof(mem))
#define FOR(i,q1,q2) for(int i=(q1); i<=(q2); ++i)
#define FORD(i,q1,q2) for(int i=(q1); i>=(q2); --i)
#define FOREACH(it,mp) for(typeof((mp).begin()) it=(mp).begin(); it!=(mp).end(); ++it)

#define isdig(c) ('0'<=(c) && (c)<='9')

#define inbit(i,n) ((n & (1<<i))>0?1:0)
#define bit(i) (1<<i)

#define mp make_pair
#define xx first
#define yy second

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int T, N, M, lv[101][101], outdir[101][101];
const int di[] = {-1, 0, 0, 1}, dj[] = {0, -1, 1, 0}, invdir[] = {3, 2, 1, 0};
char aa[101][101];

pii q[101*101];
int nq;

void bfs(int i, int j) {
	nq = 1;
	q[0] = pii(i,j);
	for(int iq=0; iq<nq; ++iq) {
		for(int k=0; k<4; ++k) {
			int ii = q[iq].xx + di[k], jj = q[iq].yy + dj[k];
			if( 0<=ii && ii<N && 0<=jj && jj<M && outdir[ii][jj]==invdir[k] && aa[ii][jj]==-1 ) {
				aa[ii][jj] = aa[i][j];
				q[nq++] = pii(ii,jj);
			}
		}
		if( outdir[q[iq].xx][q[iq].yy]!=-1 ) {
			int k = outdir[q[iq].xx][q[iq].yy];
			int ii = q[iq].xx + di[k], jj = q[iq].yy + dj[k];
			if( aa[ii][jj]==-1 ) {
				aa[ii][jj] = aa[i][j];
				q[nq++] = pii(ii,jj);
			}
		}
	}
}

int main() {
	scanf("%d", &T);
	for(int t=1; t<=T; ++t) {
		scanf("%d%d",&N,&M);
		for(int i=0; i<N; ++i)
			for(int j=0; j<M; ++j) {
				scanf("%d", &lv[i][j]);
				outdir[i][j] = -1;
				aa[i][j] = -1;
			}
		
		for(int i=0; i<N; ++i)
			for(int j=0; j<M; ++j)
				for(int k=0; k<4; ++k) {
					int ii = i+di[k], jj = j+dj[k];
					if( 0<=ii && ii<N && 0<=jj && jj<M &&
						((outdir[i][j]==-1 && lv[ii][jj] < lv[i][j]) 
							|| (outdir[i][j]!=-1 && lv[ii][jj] < lv[i+di[outdir[i][j]]][j+dj[outdir[i][j]]]) ) )
						outdir[i][j] = k;
				}

		int nl = 0;
		for(int i=0; i<N; ++i)
			for(int j=0; j<M; ++j)
				if( aa[i][j]==-1 ) {
					aa[i][j] = 'a' + (nl++);
					bfs(i,j);
				}
		
		printf("Case #%d:\n", t);
		for(int i=0; i<N; ++i)
			for(int j=0; j<M; ++j)
				printf("%c%c", aa[i][j], (j+1==M ? '\n' : ' '));
	}
	return 0;
}
