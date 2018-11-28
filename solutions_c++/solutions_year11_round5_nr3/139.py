#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define S(X) ((X)*(X))
#define ABS(X) ((X)>0?(X):(-(X)))
#define SZ(X) (int)(X.size())
typedef pair<int,int> PII;
typedef __int64 LL;

int dr[]={-1,-1,-1,0,1,1,1,0};
int dc[]={-1,0,1,1,1,0,-1,-1};
int dir_arr[4][2]=
{
	{3,7},
	{1,5},
	{0,4},
	{2,6},
};

int R,C;
char board[20][20];
int d[20][20];
int dir[20][20];

int check()
{
	int i,j,ni,nj;

	for(i=0;i<R;i++)
		for(j=0;j<C;j++)
			d[i][j]=0;

	for(i=0;i<R;i++)
		for(j=0;j<C;j++)
		{
			ni = (i + dr[dir[i][j]]+R-1)%R;
			nj = (j + dc[dir[i][j]]+C-1)%C;

			d[ni][nj]++;
			d[i][j]--;
		}

	for(i=0;i<R;i++)
		for(j=0;j<C;j++)
			if(d[i][j])
				return 0;

	return 1;
}

inline int SIGN(int mask, int t)
{
	if(mask & (1<<t)) return 1;
	return 0;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin); freopen("C-small-output0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin); freopen("C-small-output1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin); freopen("C-small-output2.out","w",stdout);
//	freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);

	int T, ks;
	int i,len,lim,cnt;
	int t;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);

		scanf("%d%d",&R,&C);
		for(i=0;i<R;i++)
			scanf("%s",board[i]);

		len = R*C;
		lim = 1<<len;

		cnt = 0;
		for(i=0;i<lim;i++)
		{
			for(t=0;t<len;t++)
			{
				if(board[t/C][t%C]=='-') dir[t/C][t%C] = dir_arr[0][SIGN(i,t)];
				if(board[t/C][t%C]=='|') dir[t/C][t%C] = dir_arr[1][SIGN(i,t)];
				if(board[t/C][t%C]=='\\') dir[t/C][t%C] = dir_arr[2][SIGN(i,t)];
				if(board[t/C][t%C]=='/') dir[t/C][t%C] = dir_arr[3][SIGN(i,t)];
			}
			if(check())
				cnt++;
		}

		printf("%d\n",cnt%1000003);

	}

	return 0;
}