#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int T;

const char p[]="welcome to code jam";
const int plen=strlen(p);
const int MOD=10000;
int len;
char s[1000];
int dp[1000][100];

int solve(int pos,int pat)
{
		int &ret=dp[pos][pat];
		if (ret>-1) return ret;
		
		if (pat==plen)
		 return ret=1;
		if (pos==len)
		 return ret=0;
		ret=solve(pos+1,pat);
		if (s[pos]==p[pat])
		 ret+=solve(pos+1,pat+1);
		ret%=MOD;
		
		return ret;
}

int main()
{
    scanf("%d\n",&T);
    F(xx,T)
     {
			gets(s);
			len=strlen(s);
			memset(dp,-1,sizeof(dp));
			printf("Case #%d: %04d\n",xx+1,solve(0,0));
	 }
    return 0;
}
