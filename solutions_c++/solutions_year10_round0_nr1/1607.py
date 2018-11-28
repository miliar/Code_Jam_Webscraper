#include <stdio.h>
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,1,n)

#define INP_FILE "a.in"
#define OUP_FILE "a.out"
#define N 50

int n,k;
int T;

void input(){
	scanf("%d %d",&n,&k);
}

void process(){
	bool ans;
	int D[N]={0,};
	int i;
	D[1] = 1;
	FOR(i,2,n){
		D[i] = D[i-1]*2+1;
	}
	ans = ((k+1)%(D[n]+1))==0;
	printf("Case #%d: %s\n",T,(ans==true)? "ON":"OFF" );
}

int main(){
	freopen(INP_FILE,"rt",stdin);
	freopen(OUP_FILE,"wt",stdout);
	int t;
	scanf("%d",&t);
	REP(T,t){
		input();
		process();
	}
	return 0;
}