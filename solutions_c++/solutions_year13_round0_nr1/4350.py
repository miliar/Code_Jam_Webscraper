#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<string>
#include<cstdio>
#include<vector>
#include<cassert>
#include<cstring>
#include<cstdlib>
#include<utility>
#include<iostream>
#include<algorithm>
#include<functional>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 15
using namespace std;
typedef long long LL;
int t;
char in[M][M];
bool wo,wx;
bool check(char x)
{
	bool flag;
	REP(i,1,4)
	{
		flag=true;
		REP(j,1,4)
			if(in[i][j]!='T' && in[i][j]!=x)
				flag=false;
		if(flag)return true;
	}

	REP(j,1,4)
	{
		flag=true;
		REP(i,1,4)
			if(in[i][j]!='T' && in[i][j]!=x)
				flag=false;
		if(flag)return true;
	}

	flag=true;
	REP(i,1,4)
		if(in[i][i]!='T' && in[i][i]!=x)
			flag=false;
	if(flag)return true;

	flag=true;
	REP(i,1,4)
		if(in[i][5-i]!='T' && in[i][5-i]!=x)
			flag=false;
	if(flag)return true;

	return false;
}
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		wo = wx = false;
		REP(i,1,4)scanf("%s",in[i]+1);

		wo = check('O');
		wx = check('X');

		printf("Case #%d: ",tt);
		if(wo)puts("O won");
		else if(wx)puts("X won");
		else
		{
			bool complete=true;
			REP(i,1,4)REP(j,1,4)
				if(in[i][j] == '.')
					complete=false;
			if(complete)puts("Draw");
			else puts("Game has not completed");
		}
	}
	return 0;
}

