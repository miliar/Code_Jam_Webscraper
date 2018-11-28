#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
typedef long long ll;
typedef vector<int> VI;

int i,j,m, v,v1,v2, U,N;
int s[20000],g[20000],c[20000];
int k[20000][2];

int mn(int x, int y)
{ if(x==-1) return y; if(y==-1) return x;
	return min(x,y); }

int main()
{
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	scanf("%d",&N);
	rep(U,N)
	{
		scanf("%d%d",&m,&v);
		forr(i,1,(m-1)/2) scanf("%d %d",&g[i],&c[i]);
		forr(i,(m-1)/2+1,m)
		{ scanf("%d",&s[i]); k[i][s[i]]=0; k[i][1-s[i]]=-1; }
		ford(i,(m-1)/2,1)
		{
			if(g[i]==1 || c[i])
			{
				if(k[2*i][1]==-1 || k[2*i+1][1]==-1) k[i][1]=-1;
				else k[i][1]=k[2*i][1]+k[2*i+1][1]+(1-g[i]);
				v1=mn(k[2*i][0],k[2*i][1]);
				v2=mn(k[2*i+1][0],k[2*i+1][1]);
				if(k[2*i][0]==-1 && k[2*i+1][0]==-1) k[i][0]=-1;
				else
				{ k[i][0]=-1;
					if(k[2*i][0]!=-1 && v2!=-1) k[i][0]=k[2*i][0]+v2+(1-g[i]);
					if(k[2*i+1][0]!=-1 && v1!=-1) k[i][0]=mn(k[i][0], k[2*i+1][0]+v1+(1-g[i]));
				}
			}
			else {	k[i][0]=-1; k[i][1]=-1; }
			if(g[i]==0 || c[i])
			{
				if(k[2*i][0]==-1 || k[2*i+1][0]==-1) k[i][0]=mn(k[i][0], -1);
				else k[i][0]=mn(k[i][0], k[2*i][0]+k[2*i+1][0]+g[i]);
				v1=mn(k[2*i][0],k[2*i][1]);
				v2=mn(k[2*i+1][0],k[2*i+1][1]);
				if(k[2*i][1]==-1 && k[2*i+1][1]==-1) k[i][1]=mn(k[i][1], -1);
				else
				{
					if(k[2*i][1]!=-1 && v2!=-1) k[i][1]=mn(k[i][1], k[2*i][1]+v2+g[i]);
					if(k[2*i+1][1]!=-1 && v1!=-1) k[i][1]=mn(k[i][1], k[2*i+1][1]+v1+g[i]);
				}
			}
		}
//		forr(i,1,m) printf("%d: %d %d\n",i,k[i][0],k[i][1]);
		printf("Case #%d: ",U+1);
		if(k[1][v]==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",k[1][v]);
	}
//	getchar();
	return 0;
}
