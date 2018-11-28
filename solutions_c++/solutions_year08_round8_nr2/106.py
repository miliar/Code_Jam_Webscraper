#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#define pb push_back
#define fi first
#define se second
#define INF 1000000000
#define MOD 10007
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef pair<string,pi> pii;
int solve()
{
	int n;
	scanf("%d",&n);
	int k=1;
	map<string,int> m;
	vector<pi> v[301];
	for (int i=0; i<n; i++)
	{
		string s;
		int a,b;
		cin>>s>>a>>b;
		if (m[s]==0) m[s]=k++;
		int p=m[s];
		v[p].pb(pi(a,b));
	}
	for (int i=1; i<k; i++)
		sort(v[i].begin(),v[i].end());
	int wynik=INF;
	for (int i=1; i<k; i++)
	{
		int ma=-1;
		int a=0,b=0,c=0,g=0,w=0;
		while (g<10000)
		{
			while (a<v[i].size()&&v[i][a].fi<=g+1) ma=max(ma,v[i][a++].se);
			if (ma==g)
			{
				w=INF;
				break;
			}
			g=ma;
			w++;
		}
		wynik=min(w,wynik);
	}
	for (int i=1; i<k; i++)
		for (int j=i+1; j<k; j++)
	{
		int ma=-1;
		int a=0,b=0,c=0,g=0,w=0;
		while (g<10000)
		{
			while (a<v[i].size()&&v[i][a].fi<=g+1) ma=max(ma,v[i][a++].se);
			while (b<v[j].size()&&v[j][b].fi<=g+1) ma=max(ma,v[j][b++].se);
			if (ma==g)
			{
				w=INF;
				break;
			}
			g=ma;
			w++;
		}
		wynik=min(w,wynik);
	}
	for (int i=1; i<k; i++)
		for (int j=i+1; j<k; j++)
			for (int l=j+1; l<k; l++)
	{
		int ma=-1;
		int a=0,b=0,c=0,g=0,w=0;
		while (g<10000)
		{
			while (a<v[i].size()&&v[i][a].fi<=g+1) ma=max(ma,v[i][a++].se);
			while (b<v[j].size()&&v[j][b].fi<=g+1) ma=max(ma,v[j][b++].se);
			while (c<v[l].size()&&v[l][c].fi<=g+1) ma=max(ma,v[l][c++].se);
			if (ma==g)
			{
				w=INF;
				break;
			}
			g=ma;
			w++;
		}
		wynik=min(w,wynik);
	}
	if (wynik==INF) return -1;
	return wynik;
}

int main()
{
	int tests;
	scanf("%d",&tests);
	for (int te=1; te<=tests; te++)
	{
		int w=solve();
		if (w>=0) printf("Case #%d: %d\n",te,w);
		else printf("Case #%d: IMPOSSIBLE\n",te);
	}
}
