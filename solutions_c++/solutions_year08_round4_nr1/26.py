#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <cctype>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long int64;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

const int maxn=100000;
const int inf=100000000;

int n;

int type[maxn];
int ch[maxn];

int solve(int t,int x,int y,int v)
{
	if(v==0)
	{
		if(t==0)
			return x+y;
		else
			return min(x,y);
	}
	else
	{
		if(t==0)
			return min(x,y);
		else
			return x+y;
	}
}

int get(int x,int y)
{
	if(type[x]<2) return type[x]==y ? 0:inf;
	int a,b;
	a=get(2*x,y);
	b=get(2*x+1,y);
	int res=solve(type[x]-2,a,b,y);
	if(ch[x])
		res=min(res,solve(3-type[x],a,b,y)+1);
	return res;
}

int main()
{
	int tc;
	cin >> tc;
	for(int ic=0;ic<tc;ic++)
	{
		printf("Case #%d: ",ic+1);
		int v;
		cin >> n >> v;
		for(int i=0;i<(n-1)/2;i++)
		{
			int x,y;
			cin >> x >> y;
			type[1+i]=2+x;
			ch[1+i]=y;
		}
		for(int i=0;i<(n+1)/2;i++)
		{
			int x;
			cin >> x;
			type[1+i+(n-1)/2]=x;
		}
		int res=get(1,v);
		if(res>=inf/2) res=-1;
		if(res==-1)
			cout << "IMPOSSIBLE";
		else
			cout << res;
		printf("\n");
	}
	return 0;
}
