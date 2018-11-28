#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int s[110][12];
int n, m, ans, rx;

void input()
{
	memset(s, 0xff, sizeof(s));
	
	int i, j, a, b, c;
	
	scanf("%d%d", &n, &m);
	for(i=0; i<m; i++){
		scanf("%d", &c);
//		cnt[i]=c;
		for(j=0; j<c; j++){
			scanf("%d%d", &a, &b);
			s[i][a-1]=b;
		}
	}
}

bool check(int x)
{
	int cnt, i, j;
	bool fg;
	cnt=0;
	for(i=0; i<m; i++){
		fg=0;
		for(j=0; j<n; j++)
			if(s[i][j]>=0){
				if(s[i][j] && (x&(1<<j))) fg=1;
				else if(!s[i][j] && !(x&(1<<j))) fg=1;
			}
		if(fg) cnt++;
	}
	return cnt==m;
}

int solve()
{
	int x, tmp, i;
	
	ans=1000;
	for(x=0; x<(1<<n); x++){
		if(check(x)){
			tmp=0;
			for(i=0; i<n; i++)
				if(x&(1<<i)) tmp++;
			if(tmp<ans) ans=tmp, rx=x;
		}
	}
	
	if(ans>100) printf(" IMPOSSIBLE\n");
	else{
		for(i=0; i<n; i++)
			if(rx&(1<<i)) printf(" 1");
			else printf(" 0");
		printf("\n");
	}
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int cc, cntc;
	
	scanf("%d", &cc);
	for(cntc=1; cntc<=cc; cntc++){
		printf("Case #%d:", cntc);
		
		input();
		solve();
	}
	
	return 0;
}
