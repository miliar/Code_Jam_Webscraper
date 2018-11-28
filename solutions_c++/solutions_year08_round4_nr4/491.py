#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for (int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for (int i=(a),_b=(b); i>=_b; i--)
#define REP(i,n) for (int i=0,_n=(n); i<_n; i++)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

int nTC,k,p[100];
char s[50100], c[50100];

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		printf("Case #%d: ",TC);
		scanf("%d %s",&k,s);
		REP(i,k) p[i] = i;
		int len = strlen(s);
		int res = len;

		do {
			REP(i,len){
				int start = (i/k)*k;
				c[i] = s[start+p[i%k]];
			}
			int grp = 0, prev=-10;
			REP(i,len){
				if (prev != c[i]) grp++;
				prev = c[i];
			}
			res <?= grp;
		} while (next_permutation(p,p+k));

		printf("%d\n",res);
	}
}
