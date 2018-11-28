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
char filein[100] = "D:\\codejam\\C-large.in";
char fileout[100] = "D:\\codejam\\C-large.out"; 
void read()        {    freopen(filein,"r",stdin);    }
void write()        {    freopen(fileout,"w",stdout);    }
template<class T> inline void checkmin(T &a,T b)    {if(a < 0 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)    {if(a < b)    a = b;}

char dir[4][2] = {-1, 0, 0, 1, 1, 0, 0, -1}; //up,right,down,left
inline int maxx(int a, int b){	return a > b ? a : b; }
inline int minx(int a, int b){	return a > b ? b : a; }
inline int lowbit(int x){	return ((x)&(-x)); }
int a[10000];
int main()
{
	read();
	write();
	int t,n;
	int i, j;
	int cas = 1;
	scanf("%d", &t);
	while (t --)
	{
		scanf("%d", &n);
		int s = 0;
		int sum = 0;
		for (int i = 0; i < n; i ++)
		{
			scanf("%d", &a[i]);
			s ^= a[i];
			sum += a[i];
		}
		if(s ==0)
		{
			int m = 100000000;
			for (int i = 0; i < n ; i++)
			{
				if(m > a[i])
					m = a[i];

			}
			printf("Case #%d: %d\n", cas ++, sum - m);

		}
		else
		{
			printf("Case #%d: NO\n", cas ++);

		}
	}
	return 0;
}