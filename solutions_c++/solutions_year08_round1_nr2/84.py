#include <stdio.h>
#include <string.h>

int Z[100],O[100];
int N,M;

int bitcount(int x){
	if (x==-1) return 100;
	int res=0;
	while (x){
		if (x&1) res++;
		x>>=1;
	}
	return res;
}

void solve(int cas){
	int i,j,p,s,t,res;
	scanf("%d%d",&N,&M);
	for (i=0;i<M;i++){
		Z[i]=O[i]=0;
		scanf("%d",&t);
		while (t--){
			scanf("%d%d",&p,&s); p--;
			if (s==1) O[i]|=(1<<p);
			else Z[i]|=(1<<p);
		}
//		printf("...........%d..%d %d\n",i,O[i],Z[i]);
	}
	res=-1;
	for (i=(1<<N)-1;i>=0;i--){
		for (j=0;j<M;j++)
			if ((i&O[j])||((~i)&Z[j])) continue;
			else break;
		if (j==M){
			if(bitcount(res)>bitcount(i)) res=i;
//			printf("i=%d\n",i);
		}
	}
	printf("Case #%d:",cas);
	if (res==-1) printf(" IMPOSSIBLE\n");
	else{
		for (i=0;i<N;i++) printf(" %d",(res>>i)&1);
		printf("\n");
	}
}

int main(){
	int t,cas;
	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}

