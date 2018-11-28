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

#define GI(x) scanf("%d", &x)

using namespace std;
int n;
int d[51][51];
int last1[51];

int solve()
{
	int i, j, k;
	CLR(last1);
	for(i = 0; i < n; i++)
	{
		for(j = n-1; j >= 0; j--)
		{
			if(d[i][j] == 1)
			{
				last1[i] = j;
				break;
			}
		}
	}
	int ans = 0;
	for(i = 0; i < n; i++)
	{
		if(last1[i] <= i)
			continue;
		for(j = i+1; j < n; j++)
		{
			if(last1[j] <= i)
				break;
			
		}
		int x = j;
		int y = last1[j];
		for(j = x; j > i; j--)
		{
			last1[j] = last1[j-1];
			ans++;
		}
		last1[i] = y;
	}
	return ans;
}
		
int main()
{
	int tes;
	cin >> tes;
	for(int t = 1; t <= tes; t++)
	{
		int i, j, k;
		cin >> n;
		char c;
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < n; j++)
			{
				cin >> c;
				d[i][j] = c - '0';
			}
		}
		int ans = solve();
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
	
