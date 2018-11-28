#include <cstdio>
#include <iostream>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <cctype>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define rep(i,n) for(int i=0;i<n;i++)
#define forr(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define sz(a) ((int)(a).size())
#define ALL(a) (a).begin(),(a).end()

const int maxn=105;
const int maxk=25;

int n,k,l,test;
int a[2*maxn][2*maxn];
int sc[maxn][maxk];
bool flag;
int ans;
bool used[2*maxn];

bool dfs(int ver)
{
	if(ver==2*n+1)
		return 1;
	used[ver]=1;
	forr(i,1,2*n+1)
		if(!used[i] && a[ver][i])
		{
			a[ver][i]=0;
			a[i][ver]=1;
			if(!dfs(i))
			{
				a[ver][i]=1;
				a[i][ver]=0;
			}else
				return 1;
		}
	return 0;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&test);
	forr(t,1,test)
	{
		scanf("%d%d",&n,&k);
		rep(i,n)
			rep(j,k)
				scanf("%d",&sc[i][j]);
		memset(a,0,sizeof(a));
		rep(i,n)
			forr(j,i+1,n-1)
			{
				flag=1;
				rep(l,k)
					if(sc[i][l]==sc[j][l])
					{
						flag=0;
						break;
					}
				if(flag)
					rep(l,k-1)
						if(sc[i][l]<sc[j][l] && sc[i][l+1]>sc[j][l+1] || sc[i][l]>sc[j][l] && sc[i][l+1]<sc[j][l+1])
						{
							flag=0;
							break;
						}
				if(flag)
				{
					if(sc[i][0]<sc[j][0])		
						a[i+1][n+j+1]=flag;else
						a[j+1][n+i+1]=flag;
				}
			}
		forr(i,1,n)
		{
			a[0][i]=1;
			a[n+i][2*n+1]=1;
		}
		ans=0;
		memset(used,0,sizeof(used));
		while(dfs(0)) 
		{
			ans++;
			memset(used,0,sizeof(used));
		}
		printf("Case #%d: %d\n",t,n-ans);
	}
	return 0;
}
