#include<iostream>
#include<string>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<algorithm>
using namespace std;

const int maxn=10010;

int m, n, v;
int gate[maxn], ch[maxn], val[maxn];
int dp[maxn][2];

void input()
{
	int i;
	
	memset(ch, 0, sizeof(ch));
	memset(gate, 0, sizeof(gate));
	memset(val, 0, sizeof(val));
	
	scanf("%d%d", &m, &v);
	n=(m-1)/2;
	for(i=1; i<=n; i++) scanf("%d%d", &gate[i], &ch[i]);
	for(i=n+1; i<=m; i++) scanf("%d", &val[i]), gate[i]=-1;
}

void comp()
{
	int i;
	for(i=n; i>=1; i--)
		if(gate[i]==0) val[i]=(val[2*i] || val[2*i+1]);
		else val[i]=(val[2*i] && val[2*i+1]);
}

int min(int a, int b)
{
	return a<b?a:b;
}

int andgate(int k, int t)
{
	int tmp=maxn;
	
	if(t==1) tmp=min(dp[2*k][1]+dp[2*k+1][1], tmp);
	else tmp=min(min(dp[2*k][0], dp[2*k+1][0]), tmp);
	
	if(ch[k]){
		if(t==1) tmp=min(min(dp[2*k][1], dp[2*k+1][1])+1, tmp);
		else tmp=min(dp[2*k][0]+dp[2*k+1][0]+1, tmp);
	}
	
	return tmp;
}

int orgate(int k, int t)
{
	int tmp=maxn;
	if(t==1) tmp=min(min(dp[2*k][1], dp[2*k+1][1]), tmp);
	else tmp=min(dp[2*k][0]+dp[2*k+1][0], tmp);
	
	if(ch[k]){
		if(t==1) tmp=min(dp[2*k][1]+dp[2*k+1][1]+1, tmp);
		else tmp=min(min(dp[2*k][0], dp[2*k+1][0])+1, tmp);
	}
	
	return tmp;
}

void dpfun()
{
	int i;
	for(i=m; i>n; i--) dp[i][val[i]]=0, dp[i][1-val[i]]=maxn;
	for(i=n; i>0; i--){
		dp[i][val[i]]=0;
		if(gate[i]==1) dp[i][1-val[i]]=andgate(i, 1-val[i]);
		else dp[i][1-val[i]]=orgate(i, 1-val[i]);
	}
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int cc, ct, ans;
	
	scanf("%d", &cc);
	for(ct=1; ct<=cc; ct++){
		printf("Case #%d: ", ct);
		
		input();
		comp();
		dpfun();
		ans=dp[1][v];
//		cout<<endl;
//		for(int i=1; i<=m; i++) printf("%d %d %d\n", val[i], dp[i][0], dp[i][1]);
		
		if(ans>=maxn) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	
	return 0;
}
