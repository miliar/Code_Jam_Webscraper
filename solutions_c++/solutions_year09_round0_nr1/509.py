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

char word[6000][20], tmp[100100];
int q1[6000],nq1, q2[6000],nq2, cc[256], L, D, N;

int main() {
	scanf("%d%d%d", &L, &D, &N);
	for(int i=0; i<D; ++i)
		scanf("%s", word[i]);
		
	for(int t=0; t<N; ++t) {
		scanf("%s", tmp);
		//cout << tmp << endl;
		nq1 = D;
		for(int i=0; i<D; ++i)
			q1[i] = i;

		int ind = 0;
		for(int i=0; i<L; ++i) {
			if( tmp[ind]==0 ) cerr << "invalid ind index" << endl;
			memset(cc,0,sizeof(cc));
			
			if( tmp[ind]=='(' ) {
				while( tmp[++ind]!=')' ) {
					if( tmp[ind]==0 ) cerr << "invalid ind index" << endl;
					cc[tmp[ind]] = 1;
				}
				if( tmp[ind]!=')' ) cerr << "no close brack" << endl;
			} else
				cc[tmp[ind]] = 1;
			ind++;
		
			nq2 = 0;
			for(int j=0; j<nq1; ++j)
				if( cc[word[q1[j]][i]] )
					q2[nq2++] = q1[j];
			
			nq1 = nq2;
			memcpy(q1, q2, sizeof(q1));
		}
		printf("Case #%d: %d\n", t+1, nq2);
	}
	return 0;
}
