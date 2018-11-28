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

int n,m;

bool check(int x, ii& a)
{
	if(x==0)
	{
		a.first=0;
		a.second=0;
		return true;
	}
	if(x<=n)
	{
		a.first=x;
		a.second=1;
		return true;
	}
	if(x<=m)
	{
		a.first=1;
		a.second=x;
		return true;
	}
	for(int i=1;i<=n;i++)
	{
		if(x%i==0)
		{
			int j=x/i;
			if(j>m) continue;
			a.first=i;
			a.second=j;
			return true;
		}
	}
	return false;
}

int main()
{
	int tc;
	cin >> tc;
	for(int ic=0;ic<tc;ic++)
	{
		printf("Case #%d: ",ic+1);
		int a;
		cin >> n >> m >> a;
		ii a1,a2;
		bool ok=false;
		for(int i=0;a+i<=n*m;i++)
		{
			if(!check(i,a1)) continue;
			if(!check(a+i,a2)) continue;
			ok=true;
			break;
		}
		if(!ok)
		{
			printf("IMPOSSIBLE");
		}
		else
		{
			printf("%d %d %d %d %d %d",0,0,a1.first,a2.second,a2.first,a1.second);
		}
		printf("\n");
	}
	return 0;
}
