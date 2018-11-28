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

int T, N, nn;
char str[100100], text[] = "welcome to code jam";
int aa[501][30];

int main() {
	nn = strlen(text);

	gets(str);
	sscanf(str, "%d", &T);
	for(int t=1; t<=T; ++t) {
		gets(str);
		N = strlen(str);
		memset(aa, 0, sizeof(aa));
		aa[0][0] = (str[0]=='w')?1:0;
		
		for(int i=1; i<N; ++i)
			for(int j=0; j<nn; ++j) {
				aa[i][j] = aa[i-1][j];
				if( str[i]==text[j] )
					aa[i][j] = (aa[i][j] + ((j==0) ? 1 : aa[i-1][j-1]) )%10000;
			}
		
		int ans = aa[N-1][nn-1];
		printf("Case #%d: %0.4d\n", t, ans%10000);
	}
	return 0;
}
