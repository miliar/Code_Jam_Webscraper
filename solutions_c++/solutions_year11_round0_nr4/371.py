//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

#define FOR(i,a,b)					for(int i=a;i<b;i++)
#define REP(i,n)					FOR(i,0,n)
#define pb						 	push_back
#define mp						 	make_pair
#define s(n)						scanf("%d",&n)
#define sl(n) 						scanf("%lld",&n)
#define sf(n) 						scanf("%lf",&n)
#define ss(n) 						scanf("%s",n)
#define fill(a,v) 					memset(a, v, sizeof a)
#define sz							size()
#define INF							(int)1e9
#define EPS							1e-9
#define bitcount					__builtin_popcount
#define all(x)						x.begin(), x.end()
#define gcd							__gcd
#define maX(a,b)					(a>b?a:b)
#define miN(a,b)					(a<b?a:b)

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long LL;
typedef pair<int, int > PII;

/*Main code begins now */
int testnum;
double fact[105];
double invfact[1005];
double drng[1005];
double ans[1005];

int N;
int arr[1005];

void preprocess()
{
	fact[0]=1;
	for(int i=1;i<=100;i++)
		fact[i]=fact[i-1]*i;
	
	drng[0]=1;
	for(int i=1;i<=100;i++)
		if(i%2)	drng[i]=drng[i-1]-1/fact[i];
		else	drng[i]=drng[i-1]+1/fact[i];
	
	for(int i=101;i<=1000;i++)
		drng[i]=drng[i-1];
		
	invfact[0]=1;
	for(int i=1;i<=1000;i++)
		invfact[i]=invfact[i-1]/i;
		
	ans[0]=0;
	ans[1]=0;
	for(int i=2;i<=1000;i++)
	{
		double temp=0;
		for(int j=0;j<i;j++)
			temp+=(drng[j]*invfact[i-j])*ans[j];
		temp++;
		ans[i]=temp/(1-drng[i]);
	}
}

void solve()
{
	int cnt=0;
	for(int i=1;i<=N;i++)
		if(arr[i]!=i) cnt++;
	printf("Case #%d: %.9lf\n",testnum,(double)cnt);
}

bool input()
{
	s(N);
	for(int i=1;i<=N;i++)
		s(arr[i]);
	return true;
}


int main()
{
	preprocess();
	int T; s(T);
	for(testnum=1;testnum<=T;testnum++)
	{
		if(!input()) break;
		solve();
	}
}
