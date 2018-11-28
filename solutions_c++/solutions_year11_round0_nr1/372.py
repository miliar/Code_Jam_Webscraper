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
bool O[111];
int button[111];



void preprocess()
{

}

void solve()
{
	int Opos,Otime,Bpos,Btime,total;
	total=0;
	Opos=1; Otime=0;
	Bpos=1; Btime=0;
	
	for(int i=0;i<N;i++)
	{
		if(O[i])
		{
			int d=abs(button[i]-Opos);
			Otime+=d;
			Opos=button[i];
			if(Otime<total) Otime=total;
			Otime++;
		}
		else
		{
			int d=abs(button[i]-Bpos);
			Btime+=d;
			Bpos=button[i];
			if(Btime<total) Btime=total;
			Btime++;
		}
		
		total=max(Btime,Otime);
	}
	
	printf("Case #%d: %d\n",testnum,total);

}

bool input()
{
	s(N);
	char temp[111];
	for(int i=0;i<N;i++)
	{
		scanf("%s",temp);
		O[i]=(temp[0]=='O');
		s(button[i]);
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
