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
typedef pair<LL, LL > PLL;

/*Main code begins now */
int testnum;
int C,D;
vector<PLL> arr;


void preprocess()
{

}

bool feasible(LL time)
{
	double t=0.5*time;
	double last=-(1e15);
	for(int i=0;i<C;i++)
	{
		LL num=arr[i].second;
		LL x=arr[i].first;
		//printf("%lld %lld\n",x,num);
		for(int j=0;j<num;j++)
		{
			if(last+D > x+t+EPS) return false;
			if(last+D < x-t-EPS)
				last=x-t;
			else
				last=last+D;
				
			//if(testnum==3 && time==189268)
			//printf("last = %.6lf time = %.6lf \n",last,t);
		}
		
			
	}
	return true;
}
				

void solve()
{
	sort(arr.begin(), arr.end());
	LL lo=0;
	LL hi=(LL)(1e14);
	
	while(hi>lo)
	{
		LL mid = lo + (hi-lo)/2;
		bool z=feasible(mid);
		if(testnum==3)
		{
			//cout<<z<<" mid = "<<mid<<" "<<C<<" "<<D<<endl;
		}
		if(z)
			hi=mid;
		else
			lo=mid+1;
	}
	printf("Case #%d: %.6lf\n",testnum,0.5*hi);
}

bool input()
{
	s(C); s(D);
	int x,y;
	arr.clear();
	for(int i=0;i<C;i++)
	{
		s(x); s(y);
		arr.pb(mp((LL)x,(LL)y));
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
