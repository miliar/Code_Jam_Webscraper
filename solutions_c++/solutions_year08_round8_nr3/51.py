#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <queue>
//#include <cmath>

#define mp make_pair
#define sz(v)((int)((v).size()))
#define all(v) v.begin(),v.end()
#define pb push_back

using namespace std;

typedef pair<int,int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

const int maxn=510;
const int64 mod=1000000009;

vi g[maxn];
int n;
int64 k;

bool u[maxn];

int64 A[maxn*4][maxn];

int64 go(int x,int a1,int a2)
{
	u[x]=true;
	int64 res=1;
	int ch=0;
	for(int i=0;i<sz(g[x]);i++)
		if(!u[g[x][i]])
			ch++;
	res=A[a1+a2][ch];
	for(int i=0;i<sz(g[x]);i++)
		if(!u[g[x][i]])
			res=(res*go(g[x][i],a2+ch-1,1))%mod;
	return res;
}

int main()
{
	int tc;
	cin >> tc;
	for(int ic=0;ic<tc;ic++){
		printf("Case #%d: ",ic+1);
		for(int i=0;i<maxn;i++)
		{
			g[i].clear();
		}
		cin >> n >> k;
		memset(A,0,sizeof(A));
		for(int i=0;i<=min<int>(n,k);i++)
			for(int j=0;j<=min<int>(n,k);j++)
			{
				int64 res=1;
				for(int64 t=k-i-j+1;t<=k-i;t++)
					res=(res*t)%mod;
				A[i][j]=res;
			}
		for(int i=0;i<n-1;i++)
		{
			int x,y;
			cin >> x >> y;
			x--,y--;
			g[x].pb(y);
			g[y].pb(x);
		}
		memset(u,0,sizeof(u));
		int64 res=go(0,0,0);
		cout << res << "\n";
	}
	return 0;
}
