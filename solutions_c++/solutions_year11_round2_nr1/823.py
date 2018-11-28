#pragma warning(disable: 4786)
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
char filein[310] = "D:\\codejam\\A\\A-small-attempt0.in";
char fileout[390] = "D:\\codejam\\A\\A-small-attempt0.out"; 
void read()        {    freopen(filein,"r",stdin);    }
void write()        {    freopen(fileout,"w",stdout);    }
template<class T> inline void checkmin(T &a,T b)    {if(a < 0 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)    {if(a < b)    a = b;}

char dir[4][2] = {-1, 0, 0, 1, 1, 0, 0, -1}; //up,right,down,left
inline int maxx(int a, int b){	return a > b ? a : b; }
inline int minx(int a, int b){	return a > b ? b : a; }
inline int lowbit(int x){	return ((x)&(-x)); }
char mmap[101][101];
double ans[3][101];
int main()
{
	read();
	write();
	int n, i, j;
	int t, cas = 1;
	scanf("%d", &t);
	while (t --)
	{
		scanf("%d", &n);
		for (int i = 0; i <n ; i ++)
		{
			scanf("%s", mmap[i]);
		}
		//for (int k = 0; k < 3; k ++)
		//{
		//	for (int i = 0; i < n; i ++)
		//	{

		//		for (int j = 0; j < n;j ++)
		//		{
		//			ans[k][i][j] = 0;
		//		}
		//	}
		//}
		for (int i = 0; i < n; i ++)
		{
			int s = 0;
			int total = 0;
			for (int j = 0; j < n; j ++)
			{
				if(mmap[i][j] == '1' || mmap[i][j] == '0')
					total ++;
				if(mmap[i][j] == '1')
					s ++;
			}
			ans[0][i] = (double)s/total;
			
		}
		for (int i = 0; i < n; i ++)
		{
		//	int flag = 0;

			double s;
			int t;
			s = 0;
			t = 0;
			for (int j = 0; j < n; j ++)
			{
				//for (int i = 0; i < n; i ++)
				//{
				if(mmap[j][i] != '.')
				{
					int tt, ss;
					tt = ss = 0;

					for (int k = 0; k < n; k ++)
					{
						if(k == i)
							continue;
						if(mmap[j][k] != '.')
							tt ++;
						 if(mmap[j][k] == '1')
							ss ++;
					}
					s += ((double)ss / tt);
					t ++;

				}
				

			}
			ans[1][i] = s / t;
		}

			for (int i = 0; i < n; i ++)
			{
				int t = 0;
				double s = 0;
				for (int j = 0; j < n; j ++){
					if(mmap[i][j] != '.')
					{
						t ++;
						s += ans[1][j];
					}
					
				}
				ans[2][i] = s / t;
			}
			printf("Case #%d:\n", cas ++);
			for (int i = 0; i < n; i ++)
			{
				double ss = 0.25 * ans[0][i] + 0.50 * ans[1][i] + 0.25 * ans[2][i];
				printf("%.10lf\n", ss);

			}


		
	}
	return 0;
}
/*
2
3
.10
0.1
10.
2
4
.11.
0.00
01.1
.10.
*/