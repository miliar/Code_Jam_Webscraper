#include<stdio.h>
#include<string.h>
char str[100];
int f[300];
int d[51];
__int64 ans;
void solve()
{
	int l = 0;
	int base = 0;
	memset(f,-1,sizeof(f));
	memset(d,-1,sizeof(d));
	int n = strlen(str);
	f[str[0]] = 1;
	d[1] = 0;
	
	for(int i = 0; i < n; i++ ){
		if(f[str[i]] == -1){
			for(l=0;l<=50;l++)if(d[l]==-1)break;
			d[l] = 0;
			f[str[i]] = l;
		}
		if(base < f[str[i]])base = f[str[i]];
	}
	ans = 0;
	base++;
	__int64 pod[100];
	pod[n-1] = 1;
	for(int i = n-2; i >= 0; i-- ){
		pod[i] = pod[i+1] * base;
	}
	for(int i = n-1; i >= 0; i-- ){
		if(f[str[i]] != 0 )ans += pod[i]*(f[str[i]]);
	}
	printf("%I64d\n",ans);
	
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 1; i <= T; i++){
		scanf("%s",str);
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
