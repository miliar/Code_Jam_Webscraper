#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=(a),_b=(b); i<=_b; i++)

#define MOD 100003
#define MAXD 1000

int memo[1000][1000];
int nCk[MAXD][MAXD];
int C, N;

int calc(int pos, int value){
	if (value==N) return 1;
	int &ret = memo[pos][value];
	if (ret!=-1) return ret; else ret = 0;
	int gap = value - pos;
	for (int i=value+gap; i<=N; i++){
		int dpos = value - pos - 1;
		int dval = i - value - 1;
		int bebas = nCk[dval][dpos];
		int t = calc(value,i);
//		printf("%d %d, i = %d, bebas = %d, t = %d, dpos = %d, dval = %d\n",
//			pos,value,i,bebas,t,dpos,dval);
		ret = (ret + (long long) bebas*t) % MOD;
	}
	return ret;
}

int main(){
	nCk[0][0] = 1;
	FOR(i,1,MAXD-1){
		nCk[i][0] = 1;
		FOR(j,1,MAXD-1) nCk[i][j] = (nCk[i-1][j-1] + nCk[i-1][j]) % MOD;
	}

//	N = 6;
//	printf("%d\n",calc(1,3));

	scanf("%d",&C);
	REP(tt,C){
		printf("Case #%d: ",tt+1);

		scanf("%d",&N);
		memset(memo,-1,sizeof(memo));

		int res = 0;
		for (int i=2; i<=N; i++){
			res = (res + calc(1,i)) % MOD;
//			printf("%d %d = %d\n",1,i,calc(1,i));
		}
		printf("%d\n",res);
		

		fprintf(stderr,"Case #%d: %d\n",tt+1,res);
	}
}
