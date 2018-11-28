#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define REP(i,n) FOR(i,0,n)
#define UN(a) sort(all(a)),(a).erase(unique(all(a)), (a).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

#define K 110
#define inf 100000

int a[K][K];

int main()
{
	int left[K],right[K];
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int test;
	scanf("%d",&test);
	int k,ans;
	bool flag;
	REP(t,test)
	{
		memset(a,0,sizeof(a));
		scanf("%d",&k);
		REP(i,k)
		{
			REP(j,i+1)
				scanf("%d",&a[i][k-1-i+2*j]);
			left[i]=k-1-i;
			right[i]=k-1+i;
		}
		FOR(i,k,2*k-1)
		{
			REP(j,2*k-i-1)
				scanf("%d",&a[i][i-k+1+2*j]);
			left[i]=i-k+1;
			right[i]=3*k-i-3;
		}
		ans=inf;
		REP(i,2*k-1)
			REP(j,2*k-1)
				if(k+abs(k-1-i)+abs(k-1-j)<ans)
				{
					flag=1;
					REP(x,2*k-1)
					{
					 	FOR(y,left[x],right[x]+1)
					 		if(2*i-x>=0 && 2*i-x<2*k-1 && y>=left[2*i-x] && y<=right[2*i-x] && a[2*i-x][y]!=a[x][y] ||
		            		   2*j-y>=left[x] && 2*j-y<=right[x] && a[x][2*j-y]!=a[x][y])
							{
								flag=0;
								break;
							}
					}
					if(flag)
					{
						ans=k+abs(k-1-i)+abs(k-1-j);//max(k+abs(k-1-i),k+abs(k-1-j));
						if(ans==4)
						{
							int s=0;
						}
					}
				}
		printf("Case #%d: %d\n",t+1,ans*ans-k*k);
	}
	return 0;
}
