/* Asyamov Igor
e-mail: igor9669@gmail.com*/

#include <iostream>
#include <deque>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <map>
#include <fstream>
#include <cstdlib>
#include <queue>
#include <bitset>
#include <set>
#include <stack>
#include <utility>
#include<cassert>
using namespace std;
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define PB push_back
#define A first
#define B second
#define Len(a) (int)a.length()
#define Sz(a) (int)a.size()
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI > VVI;
#define MAXN 250
const double Eps=1e-9;
const double Pi=2*acos(0.0);
const int inf=1000*1000*1000;

int a[MAXN][MAXN];

void Do()
{
	int b[MAXN][MAXN];

	FOR(i,MAXN)
	{
		FOR(j,MAXN)
		{
			b[i][j]=a[i][j];
			if(a[i][j]==0)
			{
				if(a[i][j-1]==1 && a[i-1][j]==1)b[i][j]=1;
			}
			else
			{
				if(a[i][j-1]==0 && a[i-1][j]==0)b[i][j]=0;
			}
		}
	}
	FOR(i,MAXN)FOR(j,MAXN)a[i][j]=b[i][j];
}


bool Check()
{
	FOR(i,MAXN)
	{
		FOR(j,MAXN)
		{
			if(a[i][j]==1)return false;
		}
	}
	return true;
}

int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(cur,t)
	{
		int n;
		scanf("%d",&n);
		FOR(i,MAXN)CLR(a[i],0);
		FOR(i,n)
		{
			int x1,x2,y1,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			FR(j,x1,x2+1)
			{
				FR(k,y1,y2+1)
				{
					a[j][k]=1;
				}
			}
		}
		int cnt=0;
		while(1)
		{
			if(Check())break;
			cnt++;
			Do();
		}
		printf("Case #%d: %d\n",cur+1,cnt);
	}
	return 0;
}

