#include<cstdio>
#include<algorithm>
const int MAXN = 100;
const bool dbg = 0;

int x[MAXN];
int v[MAXN];

void solveCase(int c){
	int n,k,b,t;
	scanf("%d%d%d%d",&n,&k,&b,&t);
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
	for(int i=0;i<n;i++)
		scanf("%d",&v[i]);
	int res = 0;
	int saved = 0;
	for(int i=n-1;i>=0 and saved < k;i--){
		if((b-x[i]) <= t*v[i]){
			saved++;
			continue;
		}else
			res += k-saved;
	}
	printf("Case #%d: ",c);
	if(saved == k)printf("%d\n",res);
	else printf("IMPOSSIBLE\n");
}

int main(){
	int cas;
	scanf("%d",&cas);
	for(int i=0;i<cas;i++)
		solveCase(i+1);
	return 0;
}
