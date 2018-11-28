#include<iostream>
#include<string>
using namespace std;

const string pp = "welcome to code jam";

int vis[550][20],ht;
int f[550][20];
char s[550];
int L;

int dfs( int dep,int wh )
{
	if( wh==19 ) return 1;
	if( dep==L ) return 0;

	if( vis[dep][wh]==ht ) return f[dep][wh];

	vis[dep][wh] = ht;
	int &res = f[dep][wh];

	res = dfs(dep+1,wh);
	if( s[dep]==pp[wh] ) res+=dfs(dep+1,wh+1);
	return res;
}
int main()
{
	freopen("C0.in","r",stdin);
	freopen("C0.out","w",stdout);
	int N;
	scanf("%d\n",&N);
	for(int T=1;T<=N;T++)
	{
		gets(s);
		L = strlen(s);
		ht++;
		printf("Case #%d: %.4d\n",T,dfs(0,0));
	}
	return 0;
}
