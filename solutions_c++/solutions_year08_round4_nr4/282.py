#include <iostream>

using namespace std;
const int MAXN=1100;

char s[MAXN];
int n, k, best, per[MAXN];
bool mark[MAXN];

void init(){
	int i;
	
	scanf("%d %s",&k, &s);
	n=strlen(s);
	for (i=n; i>=1; i--)
		s[i]=s[i-1];
}

int calc()
{
	int ans=0, i, j, last=0;
	int r[MAXN];
	for (i=1; i<=n/k; i++){
		for (j=1; j<=k; j++){
			r[(i-1)*k+j]=s[(i-1)*k+per[j]];
		}
	}
	for (j=1;j<=n;j++){
		if (r[j]!=last){
			ans++;
			last=r[j];
		}
	}
	return ans;
}

void dfs(int v){
	if (v>k){
		int t=calc();
		if ( best==-1 || t<best){
			best=t;
		}
		return;
	}
	for (int i=1;i<=k;i++)
		if (!mark[i]){
			mark[i]=true;
			per[v]=i;
			dfs(v+1);
			mark[i]=false;
		}
}

void work()
{
	best=-1;
	memset(mark,false,sizeof(mark));
	dfs(1);
	printf("%d\n",best);	
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas=0, t;
	scanf("%d",&t);
	while (t--){
		cas++;
		printf("Case #%d: ", cas);
		init();
		work();
	}
	return 0;
}
