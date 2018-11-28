//#pragma warning(disable: 4786)
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <strstream>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
#define MP                    make_pair
#define CCQ(que)            while(!que.empty()) que.pop();
#define CC(m,what)            memset(m,what,sizeof(m))
#define FF(i,a)                for( int i = 0 ; i < a ; i ++ )
#define FOR(i,a,b)            for( int i = a ; i < b ; i ++ )
#define LL(a)                a<<1        //LL和RR主要用于线段树
#define RR(a)                a<<1|1        //PP用于调试输出二维矩阵
#define PP(n,m,a)            puts("---");FF(i,n){FF(j,m)cout << a[i][j] << ' ';puts("");}
const double Pi = acos(-1.0);
const int INF = 2000000000;
char filein[100] = "D:\\codejam\\A-small-attempt0.in";
char fileout[100] = "D:\\codejam\\A-small-attempt0.out"; 
void read()        {    freopen(filein,"r",stdin);    }
void write()        {    freopen(fileout,"w",stdout);    }
template<class T> inline void checkmin(T &a,T b)    {if(a < 0 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)    {if(a < b)    a = b;}

char dir[4][2] = {-1, 0, 0, 1, 1, 0, 0, -1}; //up,right,down,left
inline int maxx(int a, int b){	return a > b ? a : b; }
inline int minx(int a, int b){	return a > b ? b : a; }
inline int lowbit(int x){	return ((x)&(-x)); }

/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
int dp[111][111][111];
struct node
{
	char ch[10];
	int p;
}a[1000];
const int N = 100;
int main()
{
	//read();
	//write();
	int t, n;
	int cas = 1;
	scanf("%d", &t);
	while (t --)
	{
		scanf("%d", &n);
		memset(dp, -1, sizeof(dp));
		dp[0][1][1] = 0;
		for (int i = 0; i < n ; i++)
		{
			scanf("%s %d", a[i].ch, &a[i].p);
		}
		for (int i = 0; i < n; i ++)
		{
			for (int j = 1; j <= N; j ++)
			{
				for (int k = 1; k <= N; k ++)
				{
					if(dp[i][j][k] != -1)
					{
						if(a[i].ch[0] == 'O')
						{
							int d = abs(a[i].p - j) + 1;
							int ans = dp[i][j][k] + d;
							int l = k - d >= 1 ? k - d : 1;
							int h = k + d <= N ? k + d: N;
							for (int o = l; o <= h; o ++)
							{
								checkmin(dp[i + 1][a[i].p][o], dp[i][j][k] + d);
							}
						}
						else
						{
							int d = abs(a[i].p - k) + 1;
							int ans = dp[i][j][k] + d;
							int l = j - d >= 1 ? j - d : 1;
							int h = j + d <= N ? j + d: N;
							for (int o = l; o <= h; o ++)
							{
								checkmin(dp[i + 1][o][a[i].p], dp[i][j][k] + d);
							}
						}
					}
				}
			}
		}
		/*for (int  i = 1; i <= n ; i ++)
		{
			printf("%d:#####\n", i);
			for (int j = 1; j <= 4; j ++)
			{
				for (int k = 1; k <= 4; k ++)
				{
					printf("dp[%d][%d][%d] = %d\n", i, j, k, dp[i][j][k]);
				}
			}
		}*/
		int ans = -1;
		for (int i = 1; i <= 100; i++)
		{
			for (int j = 1; j <= 100; j ++)
			{
				if(dp[n][i][j] != -1)
					checkmin(ans, dp[n][i][j]);
			}
		}
		printf("Case #%d: %d\n",cas ++ ,  ans);
			


	}
	return 0;
}