#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<stdio.h>
#define fo(i,u,d) for (long i=(u); i<=(d); ++i)
#define fod(i,u,d) for (long i=(u); i>=(d); --i)
using namespace std;

const long maxn=7001;
const long maxl=100;

char word[maxn][maxl];
char s[maxn];
long n,m,t,ans,vis[maxn];

void init()
{
	scanf("%d%d%d",&n,&m,&t);
	fo(i,1,m) scanf("%s",word[i]);
}
void solve()
{
	memset(vis,0,sizeof(vis));
	ans=0;
	for (long i=0, j=0, h=0; i<strlen(s); ++i) {
		if (s[i]=='(') ++h;
		else if (s[i]==')') --h;
		else {
		   fo(l,1,m)
			  if (vis[l]==j && word[l][j]==s[i]) vis[l]=j+1;
		}
		if (h==0) ++j;
	}
	fo(i,1,m)
		if (vis[i]==n) ++ans;
}
int main()
{
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	init();
    fo(l,1,t) {
		scanf("%s",s);
		solve();
		printf("Case #%d: %d\n",l,ans);
	}
	return 0;
}
