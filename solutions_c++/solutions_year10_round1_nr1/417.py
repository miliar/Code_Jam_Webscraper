#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#pragma warning(disable : 4996)

#define MAXN	52
int N, K;
char board[MAXN][MAXN], rboard[MAXN][MAXN];
bool bred, bblue;
int dx[4]={1,1,1,0}, dy[4]={-1,0,1,1};
void init()
{
	cin>>N>>K;
	for (int i=0;i<N;++i)
		cin>>board[i];

	bred = false;
	bblue = false;
}

void check(int row, int col)
{
	if (rboard[row][col]=='R'&&bred)
		return;
	if (rboard[row][col]=='B'&&bblue)
		return;
	if (rboard[row][col]=='.')
		return;

	int k, tmpx, tmpy;
	for (int i=0;i<4;++i)
	{
		k=1;
		tmpx=row+dx[i]; tmpy=col+dy[i];
		while(k<K&&tmpx>=0&&tmpx<N&&tmpy>=0&&tmpy<N&&rboard[tmpx][tmpy]==rboard[row][col])
		{
			tmpx+=dx[i];tmpy+=dy[i];k++;
		}
		if (k>=K)
		{
			if (rboard[row][col]=='B')
				bblue=true;
			else if (rboard[row][col]=='R')
				bred=true;
		}
	}
}
void solve()
{
	int i, j, lowr;
	for (i=0;i<N;++i) for (j=0;j<N;++j)
	{
		rboard[j][N-1-i]=board[i][j];
	}
	
	for (j=0;j<N;++j)
	{
		lowr=-1;
		for (i=N-1;i>=0;--i)
		{
			if (rboard[i][j]=='R'||rboard[i][j]=='B')
			{
				if (lowr>i)
				{
					rboard[lowr][j]=rboard[i][j];
					rboard[i][j]='.';
					lowr--;
				}
			}
			else if (rboard[i][j]=='.')
			{
				if (lowr==-1)
					lowr=i;
			}
		}
	}
	for (i=0;i<N;++i) for (j=0;j<N;++j)
	{
		check(i,j);
		if (bred && bblue)
			break;
	}
	
}

int main()
{
//	freopen("..\\A-sample.in","r",stdin);freopen("..\\A.out","w",stdout);
//	freopen("..\\A-small-attempt0.in","r",stdin);freopen("..\\A-small.out","w",stdout);
	freopen("..\\A-large.in","r",stdin);freopen("..\\A-large.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		init();
		solve();
		if (bred&&bblue)
			cout<<"Both";
		else if (bred)
			cout<<"Red";
		else if (bblue)
			cout<<"Blue";
		else
			cout<<"Neither";
		cout<<endl;
		
		fflush(stdout);
	}
	return 0;
}

