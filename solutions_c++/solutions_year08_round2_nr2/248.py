#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<queue>
#include<set>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define mabs(x) ( ((x)>0) ? (x) : (-(x)) )
#define SIZE 1000
#define INF 1e10
#define EPS 1e-7
#define i64 __int64

int st[SIZE+5];
int hi[SIZE+5];
char p[SIZE+5];
i64 A,B;

void init() {
	int i,j;
	for(i=2;i<=SIZE;i++) if(!p[i]) {
		for(j=i+i;j<=SIZE;j+=i) {
			p[j] = 1;
			hi[j] = i;
		}
	}
	for(j=2;j<=SIZE;j++) if(!p[j]) hi[j] = j;
}

void Union(int a,int b) {
	int i,t;
	t = st[a];
	for(i=A;i<=B;i++) if(st[i] == t) st[i] = st[b];
}

int GCD(int a,int b) {
	if(b == 0) return a;
	return GCD(b,a%b);
}

int main() {
	i64 T,P;
	int i,j,g;
	set<int>s;
	int kase=1;

	init();
	scanf("%I64d",&T);
	
	while(T--) {
		scanf(" %I64d %I64d %I64d",&A,&B,&P);
		for(i=A;i<=B;i++) st[i] = i;
		for(i=A;i<=B;i++) for(j=i+1;j<=B;j++) {
			g = GCD(i,j);
			if(hi[g] >= P) Union(i,j);
		}
		s.clear();
		for(i=A;i<=B;i++) s.insert(st[i]);
		printf("Case #%d: %d\n",kase++,(int)s.size());
	}
	return 0;
}