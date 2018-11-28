#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int price[105][105];
int map[105][105];
int k, n;
int match[105];
int pit[105];
int dfs(int p)
{
	if (match[p]) 
		return 0;
	match[p] = 1;
	for (int i = 0; i < n; i++)if (map[p][i] && (pit[i] == -1 || dfs(pit[i])))
	{
		pit[i] = p;
		return 1;
	}
	return 0;
}
/*
#include<stdio.h>
#include<string.h>
int n, m;
int s[105][105];
int p[105][105];
int flag[105];
int ans = 105;
void dfs(int t,int l, int d)
{
	if(d>=ans)return;
	if(l==n){
		ans = d;
		return;
	}
	for(int j = 0; j < n; j++){
		if(flag[j]==0){
			flag[j]=1;
			dfs(j,l+1,d+1);
			flag[j]=0;
		}
	}
	for(int k = 0; k < n; k++)
	{
		if(flag[k]==0 && p[t][k] )
		{
			flag[k]=1;
			dfs(k,l+1,d);
			flag[k]=0;
		}
	}
}

void solve()
{
	memset(p,0,sizeof(p));
	for(int i=0;i<n;i++)
	{
		for(int j=i+1;j<n;j++){
			int flag1 = 0;
			int flag2 = 0;
			for(int k = 0; k < m; k++){
				if(p[i][k]>p[j][k])flag1=1;
				if(p[i][k]<p[j][k])flag2=1;
				if(p[i][k] == p[j][k]){
					flag1=1;
					flag2=1;
				}
			}
			if(flag1 && flag2)continue;
			else if(flag1)p[i][j]=1;
			else if(flag2)p[j][i]=1;
		}
	}
	memset(flag,0,sizeof(flag));
	for(int i = 0;i < n; i++){
		flag[i]=1;
		dfs(i,1,1);
		flag[i]=0;
	}
	printf("%d\n",ans);
}
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A1.out","w",stdout);
	int tcase;
	scanf("%d",&tcase);
	for(int i =1; i <= tcase; i++){
		scanf("%d%d",&n,&m);
		for(int j = 0; j < n; j++){
			for(int k = 0; k < m;k++){
				scanf("%d", &s[j][k]);
			}
		}
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
*/
int maxmatch()
{
	int ans = 0;
	memset(pit, -1, sizeof(pit));
	for (int i = 0; i < n; i++)
	{
		memset(match, 0, sizeof(match));
		if (dfs(i))ans++;
	}
	return ans;
}
int main()
{
	int tcase;
	freopen("C-large.in", "r", stdin);
	freopen("C1.out", "w", stdout);
	scanf("%d", &tcase);
	for(int t = 1; t <= tcase; t++)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < k; j++)
				scanf("%d", &price[i][j]);
		memset(map,0,sizeof(map));
		for (int i = 0; i < n; i++)
		{
			for (int l = i + 1; l < n; l++)
			{
				int flag=1;
				for ( int j = 0; j < k; j++){
					if((price[i][j] > price[l][j]) != (price[i][0] > price[l][0])
						     || price[i][j] == price[l][j])
					{
							flag = 0;
							break;
					}
				}			
				if (flag)
				{ 
					if (price[i][0] > price[l][0])map[l][i] = 1;
					else map[i][l] = 1;
				}
			}
		}
		int ans = n-maxmatch();
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
