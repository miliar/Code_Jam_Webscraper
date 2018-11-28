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

int nTC,X,Y,A;

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		printf("Case #%d: ",TC);
		scanf("%d %d %d",&X,&Y,&A);
		FOR(x1,0,X) FOR(y1,0,Y){
			FOR(x2,0,X) FOR(y2,0,Y){
				if (abs(x1*y2 - y1*x2)==A){
					printf("%d %d %d %d %d %d\n",0,0,x1,y1,x2,y2);
					goto fin;
				}
			}
		}
		puts("IMPOSSIBLE");
		fin:;
	}
}
