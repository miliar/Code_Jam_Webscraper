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

int d[11][20] = {
{0},
{0},
{0},
{2, 11, 12, 22},
{0},
{4, 31, 20, 23, 33},
{32, 21, 5, 41, 25, 45, 105, 42}, 
{2, 4, 22, 11, 34, 13, 23, 16, 52, 41, 63, 44}, 
{4, 20, 5, 31, 12, 32, 15, 24, 64},
{55, 58, 108, 72, 45, 75, 82},
{4, 16, 37, 58, 89, 145, 42, 20}
};
int len[11] = {0, 0, 0, 4, 0, 5, 8, 12, 9, 7, 8};
LL btodec(LL n, int b)
{
	LL ret = 0;
	int i, j, k;
	LL tp = 1;
	LL x = n;
	while(x)
	{
		LL t = x % 10;
		ret += t * tp;
		tp *= b;
		x /= 10;
	}
	return ret;
}
LL dectob(LL n, int b)
{
	vector<int> v;
	int i, j, k;
	LL x = n;
	while(x)
	{
		v.PB(x%b);
		x /= b;
	}
	LL ret = 0;
	for(i = SZ(v)-1; i>=0; i--)
	{
		ret *= 10;
		ret += v[i];
	}
	return ret;
}
LL sqofdig(LL n)
{
	LL ret = 0;
	int i, j, k;
	LL x = n;
	while(x)
	{
		LL t = x % 10;
		ret += t*t;
		x /= 10;
	}
	return ret;
}
int vis[11][1010];
char s[1010];
int bases[22];
int cnt;
int solve()
{
	int i, j, k;
	for(i = 2; i <= 111100; i++)
	{
		int tp = i;
		
		for(k = 0; k < cnt; k++)
		{
			j = bases[k];
			if(j == 2 || j == 4)
				continue;
			LL t = dectob(tp, j);
			LL x = t;
			int flag = 0;
			while(x != 1)
			{
				assert(x > 1);
				LL y = sqofdig(x);
				x = dectob(y, j);
				if(x <= 1000 && vis[j][x] == 1)
				{
					flag = 1;
					break;
				}
			}
			if(flag)
				break;
				
		}
		if(k == cnt)
			return i;
	}
	return -1;
}
			
			
int main()
{
	CLR(vis);
	int i, j, k;
	for(i = 3; i <= 10; i++)
	{
		for(j = 0; j < len[i]; j++)
		{
			vis[i][d[i][j]] = 1;
		}
	}
	int tes;
	scanf("%d", &tes);
	getchar();
	for(int t = 1; t <= tes; t++)
	{
		CLR(bases);
		cnt = 0;
		gets(s);
		string tp(s);
		istringstream in(tp);
		while(!in.eof())
		{
			in >> i;
			bases[cnt++] = i;
		}
		LL ans = solve();
		assert(ans > 1);
		printf("Case #%d: %lld\n", t, ans);
	}
	return 0;
}


