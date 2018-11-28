#define _CRT_SECURE_NO_DEPRECATE 

#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 

using namespace std; 

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

struct Query
{
	int x;
	int who;
} q[1000];

const int MAXN=111;

int res[MAXN][MAXN][MAXN];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	REP(tests,T)
	{
		int n;
		scanf("%d",&n);
		REP(i,n)
		{
			char c;
			scanf(" %c %d ",&c,&q[i].x);
			q[i].who=c=='O'?0:1;
			--q[i].x;
		}

		memset(res,-1,sizeof(res));
		res[0][0][0]=0;

		REP(i,n)
		{
			bool updated=true;
			while (updated)
			{
				updated=false;
			REP(x1,100)
			{
				REP(x2,100)
				{
					if (res[i][x1][x2]==-1)
						continue;

					for (int k1=-1;k1<=1;k1++)
					{
						int nx1=x1+k1;
						if (nx1<0 || nx1>=100)
							continue;

						for (int k2=-1;k2<=1;k2++)
						{
							int nx2=x2+k2;
							if (nx2<0 || nx2>=100)
								continue;

							if (res[i][nx1][nx2]==-1 || res[i][nx1][nx2]>res[i][x1][x2]+1)
							{
								res[i][nx1][nx2]=res[i][x1][x2]+1;
								updated=true;
							}

							if (q[i].who==0 && q[i].x==x1)
							{
								if (res[i+1][x1][nx2]==-1 || res[i+1][x1][nx2]>res[i][x1][x2]+1)
								{
									res[i+1][x1][nx2]=res[i][x1][x2]+1;
									updated=true;
								}
							}
						}

						if (q[i].who==1 && q[i].x==x2)
						{
							if (res[i+1][nx1][x2]==-1 || res[i+1][nx1][x2]>res[i][x1][x2]+1)
							{
								res[i+1][nx1][x2]=res[i][x1][x2]+1;
								updated=true;
							}
						}
					}
				}
			}
			}
		}

		int r=-1;
		REP(x1,100)
		{
			REP(x2,100)
			{
				if (res[n][x1][x2]==-1)
					continue;
				if (r==-1 || r>res[n][x1][x2])
					r=res[n][x1][x2];
			}
		}

		printf("Case #%d: %d\n",tests+1,r);
	}
	return 0;
}
