
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

const int MAXN=111;

char a[MAXN][MAXN];

double WP[MAXN];
double OWP[MAXN];
double OOWP[MAXN];
int n;


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	REP(tests,T)
	{
		scanf("%d\n",&n);
		REP(i,n)
			gets(a[i]);

		REP(i,n)
		{
			int win=0;
			int lose=0;
			REP(j,n)
			{
				if (a[i][j]=='1')
					++win;
				if (a[i][j]=='0')
					++lose;
			}

			WP[i]=1.0*win/(win+lose);
		}

		REP(i,n)
		{
			OWP[i]=0;
			int cnt=0;
			REP(j,n)
			{
				if (a[i][j]=='.')
					continue;

				int win=0;
				int lose=0;
				REP(k,n)
				{
					if (k==i)
						continue;

					if (a[j][k]=='1')
						++win;
					if (a[j][k]=='0')
						++lose;
				}

				OWP[i]+=1.0*win/(win+lose);
				++cnt;
			}
			OWP[i]/=cnt;
		}

		printf("Case #%d:\n",tests+1);
		REP(i,n)
		{
			OOWP[i]=0;
			int cnt=0;
			REP(j,n)
				if (a[i][j]!='.')
				{
					OOWP[i]+=OWP[j];
					++cnt;
				}
			OOWP[i]/=cnt;

			printf("%.10lf\n",0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}
