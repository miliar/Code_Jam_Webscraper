/*Author : Vineet Kumar */
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<stack>
#include<queue>
using namespace std;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))
#define max(a,b)	((a)>(b)?(a):(b))
#define min(a,b)	((a)<(b)?(a):(b))
#define	si(n)		scanf("%d",&n)
#define pi(n)		printf("%d ",n)
#define pil(n)		printf("%d\n",n)
#define sl(n)		scanf("%lld",&n)
#define sd(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)
#define scan(v,n)	vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define mod (int)(1e9 + 7)
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
string g[11];
int check(int i, int j)
{
	char ch = g[i][j];
	if((g[i][j-1]==ch || g[i][j-1]=='T') && (g[i][j-2]==ch || g[i][j-2]=='T') && (g[i][j-3]==ch || g[i][j-3]=='T'))
		return 1;
	if((g[i-1][j-1]==ch || g[i-1][j-1]=='T') && (g[i-2][j-2]==ch || g[i-2][j-2]=='T') && (g[i-3][j-3]==ch || g[i-3][j-3]=='T'))
		return 1;
	if((g[i-1][j]==ch || g[i-1][j]=='T') && (g[i-2][j]==ch || g[i-2][j]=='T') && (g[i-3][j]==ch || g[i-3][j]=='T'))
		return 1;
	if((g[i-1][j+1]==ch || g[i-1][j+1]=='T') && (g[i-2][j+2]==ch || g[i-2][j+2]=='T') && (g[i-3][j+3]==ch || g[i-3][j+3]=='T'))
		return 1;
	if((g[i][j+1]==ch || g[i][j+1]=='T') && (g[i][j+2]==ch || g[i][j+2]=='T') && (g[i][j+3]==ch || g[i][j+3]=='T'))
		return 1;
	if((g[i+1][j+1]==ch || g[i+1][j+1]=='T') && (g[i+2][j+2]==ch || g[i+2][j+2]=='T') && (g[i+3][j+3]==ch || g[i+3][j+3]=='T'))
		return 1;
	if((g[i+1][j]==ch || g[i+1][j]=='T') && (g[i+2][j]==ch || g[i+2][j]=='T') && (g[i+3][j]==ch || g[i+3][j]=='T'))
		return 1;
	if((g[i+1][j-1]==ch || g[i+1][j-1]=='T') && (g[i+2][j-2]==ch || g[i+2][j-2]=='T') && (g[i+3][j-3]==ch || g[i+3][j-3]=='T'))
		return 1;
	return 0;
}
int main()
{
	int i,j,n,t,test = 1;
	rep(i,10)
		g[i] = "..........";
	char q[11],w[11];
	for(si(t);t--;)
	{
		printf("Case #%d: ",test++);
		int cnt_dot = 0;
		rep(i,4)
		{
			ss(q);
			strcpy(w,"...");
			strcat(w,q);
			rep(j,strlen(q))
				if(q[j]=='.')
					cnt_dot++;
			strcat(w,"...");
			g[i+3] = w;
		}
		int flag = 0, ans, x;
		FOR(i,3,7)
		{
			FOR(j,3,7)
			{
				if(g[i][j]=='T' || g[i][j]=='.')
					continue;
				else
				{
					if(check(i,j))
					{
						if(g[i][j] == 'X')
							printf("X won\n");
						else
							printf("O won\n");
						flag = 1;
						break;
					}
				}
			}
			if(flag)
				break;
		}
		if(!flag)
		{
			if(cnt_dot == 0)
				printf("Draw\n");
			else
				printf("Game has not completed\n");
		}
	}
	return 0;
}

