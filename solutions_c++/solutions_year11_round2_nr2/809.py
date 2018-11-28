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
char filein[310] = "D:\\codejam\\B-small-attempt2.in";
char fileout[390] = "D:\\codejam\\B-small-attempt2.out"; 
void read()        {    freopen(filein,"r",stdin);    }
void write()        {    freopen(fileout,"w",stdout);    }
template<class T> inline void checkmin(T &a,T b)    {if(a < 0 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)    {if(a < b)    a = b;}

char dir[4][2] = {-1, 0, 0, 1, 1, 0, 0, -1}; //up,right,down,left
inline int maxx(int a, int b){	return a > b ? a : b; }
inline int minx(int a, int b){	return a > b ? b : a; }
inline int lowbit(int x){	return ((x)&(-x)); }
vector<int>vec;
int d;
struct node
{
	int p, v;
}a[1000];
bool judge(double mid, int n)
{

	double cur = vec[0] - mid;
	for (int i = 1; i < vec.size(); i ++)
	{
		double tmp = 1000000000;
		if(cur <= vec[i] - mid)
		{
			if(cur + d <=vec[i] - mid)
			{
				tmp = vec[i] - mid;
			}
			else
				tmp = cur + d;
		}
		/*else if(cur <= vec[i] - d)
			tmp = cur + d;
		else if(cur >= vec[i] && cur <= vec[i] + mid - d)
		{
			tmp = cur + d;
		}*/
		else 
			tmp = cur + d;
		cur = tmp;
		if(fabs(tmp - vec[i]) <= mid)
			continue;
		else
			return false;
		cur = tmp;
	}
	return true;

}
int main()
{
	read();
	write();
	int t, cas = 1;
	int i, j;
	int  n;
	scanf("%d", &t);
	while (t --)
	{
		scanf("%d %d", &n, &d);
		vec.clear();
		for (int i = 0; i <n;  i++)
		{
			scanf("%d %d", &a[i].p, &a[i].v);
			for (int j = 0; j < a[i].v;j ++)
				vec.push_back(a[i].p);
		}
		double low = 0;
		double high = 100000000;
		int runt = 300;
		double mid;
		//judg
		while (low  <= high)
		{
			runt --;
			mid = (low + high) / 2;
			if(runt == 0)
				break;
			if(judge(mid, n) == 1)
			{
				high = mid;
			}
			else
				low = mid;
		}
		printf("Case #%d: %.10lf\n", cas ++, mid);

	}
	return 0;
}
/*
2
3 2
0 1
3 2
6 1
2 2
0 3
1 1
*/