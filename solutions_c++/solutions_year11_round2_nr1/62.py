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
int N;
int arr[105][105];
char temp[105];

int num[105];
int den[105];
double wp[105];
double owp[105];
double oowp[105];
double rpi[105];



void preprocess()
{

}

void solve()
{
	for(int i=0;i<N;i++)
	{
		num[i]=0;
		den[i]=0;
		for(int j=0;j<N;j++)
		{
			if(arr[i][j]!=0) den[i]++;
			if(arr[i][j]==1) num[i]++;
		}
		wp[i]=(1.0*num[i])/den[i];
	}
	
	for(int i=0;i<N;i++)
	{
		double sum=0;
		for(int j=0;j<N;j++)
		{
			if(arr[i][j]==1) 	sum += (1.0*num[j])/(den[j]-1);
			if(arr[i][j]==-1)	sum += (1.0*num[j]-1)/(den[j]-1);
		}
		owp[i]=sum/den[i];
	}
	
	for(int i=0;i<N;i++)
	{
		double sum=0;
		for(int j=0;j<N;j++)
			if(arr[i][j]!=0)	sum += owp[j];
		oowp[i] = sum/den[i];
	}
	
	for(int i=0;i<N;i++)
		rpi[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
		
	printf("Case #%d:\n",testnum);
	for(int i=0;i<N;i++)
		printf("%.9lf\n",rpi[i]);
		
		
}

bool input()
{
	s(N);
	for(int i=0;i<N;i++)
	{
		scanf("%s",temp);
		for(int j=0;j<N;j++)
		{
			if(temp[j]=='1')	arr[i][j]=1;
			if(temp[j]=='0')	arr[i][j]=-1;
			if(temp[j]=='.')	arr[i][j]=0;
		}
	}
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
