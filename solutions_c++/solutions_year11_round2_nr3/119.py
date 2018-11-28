#include<stdio.h>
#include<vector>
using namespace std;
int N,M;
vector<int> E[1000];
int Ed[1000][2];
int C[1000];
int usd[1000];

void findP(int a,int b) {
	int i,j,x=a,m=0;
	usd[ C[a] ] = 1;
	usd[ C[b] ] = 1;
	for(i=0;i<E[b].size();i++) {
		for(j=0;j<N;j++) {
			if((b+j)%N == E[b][i]) break;
			if((b+j)%N == a) break;
		}
		if((b+j)%N == a) continue;
		if(j > m) {
			m = j;
			x = E[b][i];
		}
	}
	if(m>0) findP(a,x);
}

int check(int c) {
	int i,j;
	for(i=0;i<M;i++) {
		for(j=0;j<c;j++) usd[j] = 0;
		findP(Ed[i][0], Ed[i][1]);
		for(j=0;j<c;j++) if(!usd[j]) return 0;
		for(j=0;j<c;j++) usd[j] = 0;
		findP(Ed[i][1], Ed[i][0]);
		for(j=0;j<c;j++) if(!usd[j]) return 0;
	}
	return 1;
}

int f(int x, int c) {
	int i;
	if(x==N) return check(c);
	for(int i=0;i<c;i++) {
		C[x] = i;
		if( f(x+1,c) ) return 1;
	}
	return 0;
}

int main() {
	int t,T,i,j;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d %d",&N,&M);
		for(i=0;i<M;i++) scanf("%d",&Ed[i][0]);
		for(i=0;i<M;i++) scanf("%d",&Ed[i][1]);
		for(i=0;i<N;i++) E[i].clear();
		for(i=0;i<N;i++) E[i].push_back((i+1)%N);
		for(i=0;i<M;i++) E[ --Ed[i][0] ].push_back( --Ed[i][1] );
		for(i=0;i<M;i++) E[ Ed[i][1] ].push_back( Ed[i][0] );
		for(i=2;f(0,i);i++);
		f(0,i-1);
		printf("Case #%d: %d\n",t,i-1);
		for(i=0;i<N;i++) {
			if(i>0) printf(" ");
			printf("%d",C[i]+1);
		}
		printf("\n");
	}
	return 0;
}

