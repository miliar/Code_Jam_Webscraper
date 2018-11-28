#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;


#define MAXN 300
int a[MAXN][MAXN];
int at[MAXN][MAXN];
int isnemp()
{
	int i, j, k;
	for(i = 0; i < MAXN; i++)
	{
		for(j = 0; j < MAXN; j++)
		{
			if(a[i][j] == 1)
				return true;
		}
	}
	return false;
}
int solve()
{
	int i, j, k;
	CLR(at);
	int cnt=0;
	while(isnemp())
	{
		cnt++;
		for(i = 0; i < MAXN; i++)
		{
			for(j = 0; j < MAXN; j++)
			{
				if(a[i][j] != 1 && i-1 >=0 && j-1>=0)
				{
					if(a[i-1][j] == 1 && a[i][j-1] == 1)
						at[i][j] = 1;
				}
				else if(a[i][j] == 1)
				{
					if(i-1 >= 0 && a[i-1][j] == 1)
						at[i][j] = 1;
					else if(j-1 >= 0 && a[i][j-1] == 1)
						at[i][j] = 1;
					else
						at[i][j] = 0;
				}
			}
		}
		for(i = 0; i < MAXN; i++)
		{
			for(j = 0; j < MAXN; j++)
			{
				a[i][j] = at[i][j];
			}
		}
	}
	return cnt;
}

int main()
{
	int tes;
	cin >> tes;
	int tesnum = 0;
	while(tes--)
	{
		tesnum++;
		int i, j, k;
		CLR(a);
		int rec;
		cin >> rec;
		for(i = 0; i < rec; i++)
		{
			int x1,x2,y1,y2;
			cin>>x1>>y1>>x2>>y2;
			x1--;x2--;y1--;y2--;
			for(j = x1; j <= x2; j++)
			{
				for(k = y1; k <= y2; k++)
				{
					a[j][k] = 1;
				}
			}
		}
		int ans = solve();
		printf("Case #%d: %d\n", tesnum, ans);
	}
	return 0;
}
