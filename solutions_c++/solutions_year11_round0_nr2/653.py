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
char filein[100] = "D:\\codejam\\B-small-attempt3.in";
char fileout[100] = "D:\\codejam\\B-small-attempt3.out"; 
void read()        {    freopen(filein,"r",stdin);    }
void write()        {    freopen(fileout,"w",stdout);    }
template<class T> inline void checkmin(T &a,T b)    {if(a < 0 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)    {if(a < b)    a = b;}

char dir[4][2] = {-1, 0, 0, 1, 1, 0, 0, -1}; //up,right,down,left
inline int maxx(int a, int b){	return a > b ? a : b; }
inline int minx(int a, int b){	return a > b ? b : a; }
inline int lowbit(int x){	return ((x)&(-x)); }
char ch1[100][3];
char ch2[100][3];
int t, n, m;
char ddd;
int findd(string s, char a, char b)
{
	int ans = 0;
	for (int i = 0; i < n;  i++)
	{
		if(ch1[i][0] == a && ch1[i][1] == b)
		{
			ans = 1;
			ddd = ch1[i][2];
			break;
		}
		if(ch1[i][0] == b && ch1[i][1] == a)
		{
			ans = 1;
			ddd = ch1[i][2];
			break;
		}
	}

	if(ans)
		return ans;
	for (int i = 0; i < s.size(); i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			if(s[i] == ch2[j][0] && b == ch2[j][1])
				return 2;
			else if(s[i] == ch2[j][1] && b == ch2[j][0])
				return 2;
		}
	}
	return ans;
}
int main()
{
	read();
	write();
	int i, j;
	string ans;
	char ch[1000];
	scanf("%d", &t);
	int cas = 1;
	while (t --)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i  ++)
		
		{
			scanf("%s", ch1[i]);
		}
		scanf("%d", &m);
		for (int i = 0; i < m; i ++)
		{
			scanf("%s", ch2[i]);
		}
		int tt;
		scanf("%d", &tt);
		scanf("%s", ch);
		int len = strlen(ch);
		ans.clear();

		for (int i = 0; i < len; i ++)
		{
			if (ans.size() < 1)
			{
				//int now = ans.size() - 1;
				ans += ch[i];
			}
			else
			{
				int now = ans.size() - 1;
				int c = findd(ans, ans[now], ch[i]);
				if(c == 1)
				{
					ans.resize(ans.size() - 1);
					int flag = -1;
					while (ans.size() >= 1)
					{

						int now = ans.size() - 1;
						int c = findd(ans, ans[now], ddd);
						if(c == 2)
						{
							flag = 0;
							ans.clear();
							break;
						}
						else if(c == 0)
						{
							flag = 0;
							ans += ddd;
							break;
						}
						else
						{
							flag = 1;
							ans.resize(ans.size() - 1);

						}
					}
					if(flag == 1 || flag == -1)
						ans += ddd;
				}
				else if(c == 2)
				{
					ans.clear();
				}
				else
				{
					ans += ch[i];
				}
			}
		}
		printf("Case #%d: [", cas++);

		for (int i = 0; i < ans.size(); i ++)
		{
			if(i == ans.size() - 1)
				printf("%c", ans[i]);
			else
				printf("%c, ", ans[i]);
		}
		printf("]\n");
		
	}
	return 0;
}