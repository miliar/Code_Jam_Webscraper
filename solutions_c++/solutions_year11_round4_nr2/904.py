
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
#include <bitset>

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

const int MAXN=555;
const int dx[]={0,0,1,1};
const int dy[]={0,1,0,1};

char buf[MAXN];
Long a[MAXN][MAXN];
int n,m,D;
Long sumR[MAXN][MAXN];
Long sumC[MAXN][MAXN];
bool canX[MAXN][MAXN];

bool checkX(Long sumX,int i,int j,int K)
{
	REP(k,4)
	{
		int cx=i+dx[k]*(K-1);
		int cy=j+dy[k]*(K-1);

		sumX-=a[cx][cy] * (2*i + K - 1 - cx*2);
	}

	return sumX==0;
}

bool checkY(Long sumY,int i,int j,int K)
{
	REP(k,4)
	{
		int cx=i+dx[k]*(K-1);
		int cy=j+dy[k]*(K-1);

		sumY-=a[cx][cy] * (2*j + K - 1 - cy*2);
	}

	return sumY==0;
}

bool solve(int K)
{
	memset(canX,0,sizeof(canX));
	REP(X,n-K+1)
	{
		Long sumX=0;
		Long total=0;

		REP(i,K)
		{
			Long addX=sumC[X+K-1][i] - ((X==0)?0:sumC[X-1][i]);
			total+=addX;
			sumX+=addX*(K - 2*i - 1);
		}

		if (checkX(sumX,X,0,K))
			canX[X][0]=true;

		FOR(j,1,m-K+1)
		{
			sumX+=total*2;

			Long subX=sumC[X+K-1][j-1] - ((X==0)?0:sumC[X-1][j-1]);

			total-=subX;
			sumX-=subX*(K+1);

			Long addX=sumC[X+K-1][j+K-1] - ((X==0)?0:sumC[X-1][j+K-1]);

			total+=addX;
			sumX-=addX*(K-1);

			if (checkX(sumX,X,j,K))
				canX[X][j]=true;
		}
	}

	REP(Y,m-K+1)
	{
		Long sumY=0;
		Long total=0;

		REP(j,K)
		{
			Long addY=sumR[j][Y+K-1] - ((Y==0)?0:sumR[j][Y-1]);
			total+=addY;
			sumY+=addY*(K - 2*j - 1);
		}

		if (checkY(sumY,0,Y,K))
		{
			if (canX[0][Y])
				return true;
		}

		FOR(i,1,n-K+1)
		{
			sumY+=total*2;

			Long subY=sumR[i-1][Y+K-1] - ((Y==0)?0:sumR[i-1][Y-1]);

			total-=subY;
			sumY-=subY*(K+1);

			Long addY=sumR[i+K-1][Y+K-1] - ((Y==0)?0:sumR[i+K-1][Y-1]);

			total+=addY;
			sumY-=addY*(K-1);

			if (checkY(sumY,i,Y,K))
			{
				if (canX[i][Y])
					return true;
			}
		}
	}

	return false;
}

bool solve2(int K)
{
	REP(i,n-K+1)
	{
		REP(j,m-K+1)
		{
			Long sumX=0;
			Long sumY=0;
			REP(X,K)
			{
				REP(Y,K)
				{
					sumX+=a[X+i][Y+j]*(K-1-2*X);
					sumY+=a[X+i][Y+j]*(K-1-2*Y);
				}
			}

			if (checkX(sumX,i,j,K) && checkY(sumY,i,j,K))
				return true;
		}
	}
	return false;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	REP(tests,T)
	{
		if (scanf("%d%d%d\n",&n,&m,&D)!=3)
			throw -1;
		REP(i,n)
		{
			gets(buf);
			REP(j,m)
				a[i][j]=D+(buf[j]-'0');
		}

		REP(i,n)
		{
			REP(j,m)
			{
				if (j==0)
					sumR[i][j]=a[i][j]; else
					sumR[i][j]=sumR[i][j-1]+a[i][j];
				if (i==0)
					sumC[i][j]=a[i][j]; else
					sumC[i][j]=sumC[i-1][j]+a[i][j];
			}
		}

		int found=-1;
		for (int K=min(n,m)+1;K>=3;--K)
		{
			if (solve2(K))
			{
				found=K;
				break;
			}
		}

		printf("Case #%d: ",tests+1);
		if (found==-1)
		{
			puts("IMPOSSIBLE");
		} else
			printf("%d\n",found);
	}

	return 0;
}
