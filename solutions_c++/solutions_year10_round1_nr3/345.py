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

template<class T> inline T gcd(T a,T b)//NOTES:gcd(
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}

#define MAXN	1000001
#define MAXA	1000
int win[MAXA][MAXA];

int A1, A2, B1, B2;

void init()
{
	memset(win,255,sizeof(win));
	int i, j, tmp, t;
	for (i=0;i<MAXA;++i) 
		win[0][i]=win[i][0]=1;
	for (i=1;i<MAXA;++i) for (j=1;j<=i;++j)
	{
		if(j==i)
		{
			win[i][j]=0;
			continue;
		}
		tmp=(i%j);
		t=i/j;
		if (tmp==0)
			win[i][j]=win[j][i]=1;
		else
		{
			if (t==1)
			{
				if (win[j][tmp]!=-1)
					win[i][j]=win[j][i]=1-win[j][tmp];
				else
					win[i][j]=win[j][i]=win[j][tmp];
			}
			else if (win[j][tmp]!=-1)
				win[i][j]=win[j][i]=1;
		}
	}
}

int check(int large, int small)
{
	if (large==small)
		return 0;
	int tmp, tmpr;
	if (large<small)
	{
		tmp=small;
		small=large;
		large=tmp;
	}
	if (large<MAXA)
		return win[large][small];
	else
	{
		tmp=large/small;
		tmpr=large%small;
		if (tmpr==0)
			return 1;
		int g = check(small,tmpr);
		if (tmp==1)
		{
			if (g!=-1)
				return 1-g;
			else
				return g;
		}
		else
		{
			if (g!=-1)
				return 1;
			else
				return g;
		}
	}
}

int solve()
{
	cin>>A1>>A2>>B1>>B2;
	int i, j, count(0);
	for (i=A1;i<=A2;++i) for(j=B1;j<=B2;++j)
	{
		if (check(i,j)==1)
			count++;
	}

	return count;
}

int main()
{
//	freopen("..\\C-sample.in","r",stdin);freopen("..\\C.out","w",stdout);
	freopen("..\\C-small-attempt1.in","r",stdin);freopen("..\\C-small.out","w",stdout);
//	freopen("..\\C-large.in","r",stdin);freopen("..\\C-large.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		init();
		int ret = solve();
		printf("%d\n", ret);
		
		fflush(stdout);
	}
	return 0;
}

