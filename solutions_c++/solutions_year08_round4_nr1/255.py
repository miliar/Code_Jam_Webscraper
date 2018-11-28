#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <vector>
using namespace std;
typedef unsigned U;
typedef long long LL;
typedef unsigned long long UL;
typedef long double LD;
const int N = 50*1000;
const int INF = 1<<20;


int m,v;
int c[N];
int g[N];
int val[N];
int d[N][2];

void load_data()
{
	scanf("%d%d",&m,&v);
	for (int i=1; i<=((m-1)/2); i++)
		scanf("%d%d",&g[i],&c[i]);
	for (int i=1; i<=(m+1)/2; i++)
		scanf("%d",&val[i+(m-1)/2]);
}

inline int op(int a, int b, int gg)
{
	if (gg) return a&b;
	else return a|b;
}

void compute(int k)
{
	if (k>((m-1)/2))
	{
		d[k][val[k]]=0;
		d[k][1^val[k]]=INF;
		return;
	}
	d[k][0]=d[k][1]=INF;
	for (int i=0; i<2; i++)
	for (int j=0; j<2; j++)
		d[k][op(i,j,g[k])] = min(d[k][op(i,j,g[k])],d[2*k][i]+d[2*k+1][j]);
	if (c[k]==0) return;
	for (int i=0; i<2; i++)
	for (int j=0; j<2; j++)
		d[k][op(i,j,1^g[k])] = min(d[k][op(i,j,1^g[k])],1+d[2*k][i]+d[2*k+1][j]);
}

void single_case(int cas)
{
	load_data();
	for (int i=m; i>0; i--) 
	{
		compute(i);
//		printf("d[%d] = %d %d\n",i,d[i][0],d[i][1]);
	}
	printf("Case #%d: ",cas);
	if (d[1][v]==INF) printf("IMPOSSIBLE\n");
	else printf("%d\n",d[1][v]);

}


int main()
{
	int j;
	scanf("%d",&j);
	for (int i=0; i<j; i++)
		single_case(i+1);
	return 0;
}

