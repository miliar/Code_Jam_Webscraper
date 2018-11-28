#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>

using namespace std;
typedef long long ll;

const double PI=acos(-1.0);
const double eps=1e-11;

#define dump(x) cerr<<#x<<" = "<<(x)<<endl;
#define foreach(c,itr) for (__typeof( (c).begin() ) itr=(c).begin();itr!=(c).end() ;itr++ )


int countbit(int n) {return (n==0)?0:1+countbit(n&(n-1));}
int lowbit(int n) {return n&(n^(n-1));}
string toString(ll v) { ostringstream sout;sout<<v;return sout.str();}
string toString(int v) { ostringstream sout;sout<<v;return sout.str();}
int Rand16(){return rand();}
int Rand32(){return rand()*rand();}
double DRand(){return (double)rand()/RAND_MAX;}
int RandRange(int f,int r){return f+(int)(DRand()*(r-f)+0.5);}


const int MAX = 100+5;

int bo[2][MAX][MAX];

bool isOK(int a[MAX][MAX])
{
	int i,j;
	for (i=0;i<MAX;i++)
		for (j=0;j<MAX;j++)
			if (a[i][j])
				return true;
	return false;
}

int main()
{
	int t,cas;
	int i,j,k;
	int x1,y1,x2,y2;
	int R;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	scanf("%d",&t);
	cas=0;
	while (t--)
	{
		cas++;
		memset(bo,0,sizeof(bo));
		scanf("%d",&R);
		for (i=0;i<R;i++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);			
				for (j=x1;j<=x2;j++)
					for (k=y1;k<=y2;k++)
						bo[0][j][k]=1;
		}

		int ans=0;
		int now,pre;
		now=0;

		while (isOK(bo[now]))
		{
			/*
			printf("ans=%d\n",ans);
			for (i=1;i<=5;i++,putchar('\n'))
				for (j=1;j<=5;j++)
					printf("%d",bo[now][i][j]);
					*/
			ans++;
			pre=now;
			now=1-now;
			memset(bo[now],0,sizeof(bo[now]));

			for (i=1;i<MAX-1;i++)
				for (j=1;j<MAX-1;j++)
				{
						if (bo[pre][i-1][j] && bo[pre][i][j-1])
							bo[now][i][j]=1;
						else
						{
							if (!bo[pre][i-1][j] && !bo[pre][i][j-1])
								bo[now][i][j]=0;
							else
								bo[now][i][j]=bo[pre][i][j];
						}
				}
		}

		printf("Case #%d: ",cas);
		printf("%d\n",ans);
	}
	return 0;
}
