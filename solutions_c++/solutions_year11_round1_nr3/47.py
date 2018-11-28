#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
using namespace std; 

const int inf = 1000*1000*1000; 
#define CL(x,a) memset(x,a,sizeof(x)); 
#define ALL(v) (v).begin(),(v).end() 
#define PII pair<int,int> 
#define PDI pair<double,int> 
#define MP(a,b) make_pair(a,b) 
#define FOR(i,n) for(int i=0;i<n;i++) 
typedef long long LL; 
typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef vector< vector<PII > > vvpii; 

struct st
{
	int c,s,t;
	st()
	{
	}
	void read()
	{
		scanf("%d%d%d",&c,&s,&t);
	}
};
int dp[89][175][89];
vector<int> mask[89][175][89];
int T;
int n,m;
vector<st> card;
int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	FOR(test,T)
	{
		CL(dp,-1);
		scanf("%d",&n);
		vector<int> v;
		FOR(i,n)
			v.push_back(i);
		card.resize(n);
		FOR(i,n)
			card[i].read();
		scanf("%d",&m);
		card.resize(n+m);
		FOR(i,m)
			card[n+i].read();
		dp[0][1][n]=0; mask[0][1][n] = v;
		for (int i=0;i<85;i++)
		{
			for (int j=0;j<171;j++)
			{
				for (int k=0;k<85;k++)
				{
					if (dp[i][j][k] == -1)
						continue;
					if (j == 0)
						continue;
					vector<int> t = mask[i][j][k];
					for (int z=0;z<t.size();z++)
					{
						if (dp[i+1][min(j-1+card[t[z]].t,170)][min(n+m,k+card[t[z]].c)] < dp[i][j][k] + card[t[z]].s)
						{
							dp[i+1][min(j-1+card[t[z]].t,170)][min(n+m,k+card[t[z]].c)] = dp[i][j][k] + card[t[z]].s;
							vector<int> tt = t;
							swap(tt[z],tt.back());
							tt.pop_back();
							for (int q=0;q<card[t[z]].c && k+q < n+m;q++)
							{
								tt.push_back(k+q);
							}
							mask[i+1][min(j-1+card[t[z]].t,170)][min(n+m,k+card[t[z]].c)]=tt;
						}
					}
				}
			}
		}
		int res = 0;
		
		for (int i=0;i<85;i++)
		{
			for (int j=0;j<171;j++)
			{
				for (int k=0;k<85;k++)
				{
					res = max(res,dp[i][j][k]);
				}
			}
		}
		printf("Case #%d: %d\n",test+1,res);
	}
	return 0; 
}