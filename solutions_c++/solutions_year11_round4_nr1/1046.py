
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
#include <time.h>
#include <complex>

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

const int MAXN=1111;

int from[MAXN];
int to[MAXN];
int speed[MAXN];
int n,len,S,R,t;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	REP(tests,T)
	{
		if (scanf("%d%d%d%d%d",&len,&S,&R,&t,&n)!=5)
			throw -1;

		vector<PI> all;

		REP(i,n)
		{
			scanf("%d%d%d",&from[i],&to[i],&speed[i]);
		}

		int prev=0;
		REP(i,n)
		{
			all.push_back(mp(0,from[i]-prev));
			all.push_back(mp(speed[i],to[i]-from[i]));
			prev=to[i];
		}
		all.push_back(mp(0,len-to[n-1]));

		sort(ALL(all));

		double totalRun=0;
		double res=0;
		REP(i,(int)all.size())
		{
			int curLen=all[i].second;

			int curSpeed=all[i].first;

			double addRun=min(t-totalRun,1.0*curLen/(curSpeed+R));

			res+=addRun + 1.0*(curLen - (curSpeed+R)*addRun)/(curSpeed+S);

			totalRun+=addRun;
		}

		printf("Case #%d: %.10lf\n",tests+1,res);

	}
	return 0;
}
