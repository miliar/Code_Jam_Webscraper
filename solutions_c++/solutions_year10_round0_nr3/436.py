#include<cstdio>
typedef long long LL;
const bool dbg = 0;
const int MAXN = (1<<11);
int g[MAXN];
LL inc[MAXN];
int next[MAXN];
int n,k;
int r;
LL compute(){
	for(int i=0;i<n;i++){
		inc[i] = 0;
		next[i] = i;
		for(int j=0;j<n;j++){
			if(inc[i]+g[i+j] <= k){
				inc[i] += g[i+j];
			}else{
				next[i] = (i+j)%n;
				break;
			}
		}
		if(dbg)printf("inc[%d]:%lld\n",i,inc[i]);
		if(dbg)printf("next[%d]:%lld\n",i,inc[i]);
	}
	int idx = 0;
	LL res = 0;
	for(int i=0;i<r;i++){
		res += inc[idx];
		idx = next[idx];
	}
	return res;
}
void solveCase(int c){
	scanf("%d%d%d",&r,&k,&n);
	for(int i=0;i<n;i++){
		scanf("%d",&g[i]);
		g[i+n] = g[i];
	}
	printf("Case #%d: %lld\n",c,compute());
}

int main(){
	int cas;
	scanf("%d",&cas);
	for(int i=0;i<cas;i++)
		solveCase(i+1);
	return 0;
}
