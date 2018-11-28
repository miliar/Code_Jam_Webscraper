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
int C,D,N;
char comb[111][10];
char opp[111][10];
char str[111];
char ans[111];
int top;


void preprocess()
{

}

void solve()
{
	top=0;
	for(int i=0;i<N;i++)
	{
		char cur=str[i];
		bool done=false;
		if(top>0)
		{
			char prev=ans[top-1];
			for(int j=0;j<C;j++)
			{
				if((cur==comb[j][0] && prev==comb[j][1]) || (cur==comb[j][1] && prev==comb[j][0]) )
				{
					ans[top-1]=comb[j][2];
					done=true;
					break;
				}
			}
			if(done) continue;
		}

		for(int j=0;j<top;j++)
		{
			char prev=ans[j];
			for(int k=0;k<D;k++)
			{
				if((cur==opp[k][0] && prev==opp[k][1]) || (cur==opp[k][1] && prev==opp[k][0]) )
				{
					top=0;
					done=true;
					break;
				}			
			}
			if(done) break;
		}
		if(done) continue;
		
		ans[top++]=cur;
	}
	
	printf("Case #%d: [",testnum);
	for(int i=0;i<top;i++)
	{
		printf("%c",ans[i]);
		if(i<top-1) printf(", ");
	}
	printf("]\n");
}

bool input()
{
	s(C);
	for(int i=0;i<C;i++)
		ss(comb[i]);
	
	s(D);
	for(int i=0;i<D;i++)
		ss(opp[i]);
	
	s(N);
	ss(str);
	
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
