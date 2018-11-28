#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;
const double pi=3.1415926535897932384626433832795;
const double eps=1e-8;

#define pb push_back
#define mp make_pair
#define sz size()
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))
#define HAS(x,k) ((x).find(k)!=(x).end())
#define sqr(a) ((a)*(a))
//#pragma comment(linker,"/STACK:200000000")

#define PREV(x) ((x)&((x)-1))
#define NEXT(x) (((x)<<1) - PREV(x))

char ch[1<<20];
string gs(){ scanf("%s",ch); return string(ch); }
string gl(){ gets(ch); return string(ch); }

int N;
int M[1<<16];
int A[1<<16];
int H[1<<16];
int MN[1<<16];

LL dp[1<<12][12];
LL rec(int v, int used)
{
	if (v>=1<<N) return 0;
	LL r=dp[v][used];
	if (r!=-1) return r;
	r=1LL<<60;
	
	int mn=MN[v]-used;
	if (mn==0) 
		r=rec(v*2+1,used)+rec(v*2,used)+H[v];
	else
	{
		LL v1=rec(v*2+1,used+1)+rec(v*2,used+1);
		LL v2=rec(v*2+1,used)+rec(v*2,used)+H[v];
		r=MIN(v1,v2);
	}
	return r;
}



int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int tc=0; int t; scanf("%d",&t);
	while(t--)
	{
		++tc;
		scanf("%d",&N);
		FOR(i,0,1<<N)
			scanf("%d",M+i);
		int last=1<<N;
		FOR(i,0,N)
		{
			RFOR(k,1<<(N-1-i),0)
				scanf("%d",H-k+last-1);
			last/=2;
		}
		FOR(i,0,1<<N) MN[i+(1<<N)]=M[i];
		RFOR(i,1<<N,1) MN[i]=MIN(MN[i*2],MN[i*2+1]);
		CLR(dp,-1);
		
		printf("Case #%d: %lld\n",tc,rec(1,0));
	}
	
	return 0;
}
