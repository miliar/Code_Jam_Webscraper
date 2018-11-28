// joy B
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<map>
#include<string>
#include<cmath>
#include<set>
using namespace std;
typedef long long LL;
const int MAX=11000;

int N,M;
char s[MAX][20];
int val[MAX][30];
int L[MAX];

char list[110];

int ans[MAX];
bool vis[MAX];
int wry(int k)
{
	memset(vis,0,sizeof(vis));
	int res=0;
	for(int j=1;j<=N;j++)
	{
		if(L[j]!=L[k]) vis[j]=1;
	}
	for(int i=0;i<26;i++)
	{
		int x=list[i]-'a';
		bool f=0;
		for(int j=1;j<=N;j++)
		{
			if(vis[j]) continue;
			if(val[j][x]) {f=1;break;}
		}
		if(!f) continue;
		
		if(val[k][x]==0) 
		{
			res++;
		}
		for(int j=1;j<=N;j++) if(val[j][x]!=val[k][x]) vis[j]=1;
	}
	return res;
}
int gs()
{
	for(int i=1;i<=N;i++) ans[i]=wry(i);
	
	int tmp=0,id=1;
	for(int i=1;i<=N;i++)
	{
		if(tmp<ans[i]) tmp=ans[i],id=i;
	}
	printf(" %s",s[id]);
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;scanf("%d",&T);
	int CN=0;
	
	while(T--)
	{
		scanf("%d%d",&N,&M);
		for(int i=1;i<=N;i++)
		{
			scanf("%s",s[i]);
			L[i]=strlen(s[i]);
		}
		memset(val,0,sizeof(val));
		for(int i=1;i<=N;i++)
		{
			for(int j=0;j<L[i];j++)
			{
				val[i][s[i][j]-'a']+=(1<<j);
			}
		}
		
		printf("Case #%d:",++CN);
		for(int i=1;i<=M;i++) 
		{
			scanf("%s",list);
			gs();
		}
		puts("");
		
	}
	
	return 0;
}
