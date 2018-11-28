#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define FOR(i,n) for( i = 0 ; i<(n) ; i++)
#define ROF(i,n) for( i = (n-1) ; i>=0 ; i--)
#define RFOR(i,a,b)  for( i = (a) ; i<(b) ; i++)
#define RROF(i,a,b)  for( i = (a-1) ; i>=(b) ; i--)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
#define eps (1e-11)
#define inf (1<<29)
#define pb push_back 
#define ALL(a) a.begin(),a.end()
#define sz size()
int max(int a,int b)
{
	if(a>b) return a;
	else return b;
}
int min(int a,int b)
{
	if(a<b) return a;
	else return b;
}
vector<int> aa[17];
int grid[17][17];
int n,k;
bool cross(int a,int b)
{
	if(aa[a][0] == aa[b][0])
		return true;
	int i,p = aa[a][0]>aa[b][0] ?1 :0;
	for(i = 1;i<k;i++)
	{
		if(aa[a][i] == aa[b][i])
			return true;
		int k = aa[a][i]>aa[b][i] ?1 :0;
		if(k!=p)
			return true;
	}
	return false;
}
int count(int a)
{
	int ret = 0;
	for(;a;a=a>>1)
		ret+=(a&1);
	return ret;

}
int main()
{
	
//	freopen("C.in","r",stdin);
	//freopen("c.txt","w",stdout);
	int tc,fg = 1,p,j;
	cin>>tc;
	while(tc--)
	{
		CLR(grid);
		cin>>n>>k;
		int i;
		for(i = 0;i<17;i++)	aa[i].clear();

		FOR(i,n)
		{
			FOR(j,k)
			{
				scanf("%d",&p);
				aa[i].pb(p);
			}
		}
		FOR(i,n-1)
		{
			for(j = i+1;j<n;j++)
			{
				if(cross(i,j))
					grid[i][j] = grid[j][i] = 1;
			}
		}
		bool fl[17];
		CLR(fl);
		for(i = 1;i<(1<<n);i++)
		{
			int k = count(i);
			int re = 0,q;
			for(p = 0;p<n;p++)
			{
				for(q = p+1;q<n;q++)
				{
					if(((1<<p)&i) && ((1<<q)&i))
					{
						re+=grid[p][q];
					}
				}
			}
			int tar = k*(k-1)/2;
			if(tar == re)
				fl[k] = true;
		}
		for(i = 1;i<=n;i++)
		{
			if(!fl[i])
				break;
		}
		printf("Case #%d: %d\n",fg++,i-1); 
	}
	
	return 0;
}