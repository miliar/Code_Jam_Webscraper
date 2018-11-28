#include<cstdio>
#include<vector>
#include<list>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
using namespace std;
#define REP(i,n) for(int i=0;i<(n); ++i)
char c[101];
int d[101];
int res[101];
int main(){
	int z, n, lastO, lastB, last; scanf("%d", &z); REP(jj,z) {
		scanf("%d", &n);
		res[0] = 0;
		d[0] = 1;
		lastO = lastB = 0;
		REP(i,n)
			scanf("%s%d", c + i, d + i + 1);
		REP(i,n){
			if(c[i]=='O'){
				last = lastO;
				lastO = i + 1;
			}
			else{
				last = lastB;
				lastB = i + 1;
			}
			res[i+1] = max(res[i], res[last] + abs(d[last]-d[i+1])) + 1;
		}
		//printf("debug: "); REP(i,n+1) printf("%d ", res[i]); printf("\n");
		printf("Case #%d: %d\n", jj+1, res[n]);
	}
	return 0;
}

