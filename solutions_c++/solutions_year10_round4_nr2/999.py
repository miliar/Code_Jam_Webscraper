#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
#pragma comment(linker, "/STACK:16777216")
#define pb push_back
#define L(s) (int)(s).size()
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define fr(i,st,fn) for(int (i)=(st);(i)<=(fn);++(i))
#define VI vector<int>
#define inf 1000000000000LL
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define pii pair<int,int>
#define mp make_pair
#define x first
#define y second
ll c[2222][11];
int b[2222][11];
int need[2222];
int n;
map<pair<pii,int>,ll> m;
ll dfs(pair<pii,int> p)
{
	if (m.find(p)!=m.end())
		return m[p];
	if (p.x.x+2==p.x.y)
	{
		if (p.y>need[p.x.x]||p.y>need[p.x.x+1])
			return m[p]=2*inf;
		if (p.y==need[p.x.x]||p.y==need[p.x.x+1])
			return m[p]=c[0][p.x.x/2];
		return m[p]=0;
	}
	int cur=1;
	while((1<<cur)<p.x.y-p.x.x)
		++cur;
	int pos=p.x.x/(1<<cur);
	int mid=(p.x.x+p.x.y)/2;
	ll val1=dfs(mp(mp(p.x.x,mid),p.y+1))+dfs(mp(mp(mid,p.x.y),p.y+1));
	ll val2=dfs(mp(mp(p.x.x,mid),p.y))+dfs(mp(mp(mid,p.x.y),p.y))+c[cur-1][pos];
	return m[p]=min(val1,val2);

}
int main()
{
		
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ts;
	cin>>ts;
	rp(t,ts)
	{
		cerr<<t<<endl;
		ll rez=0;
		cin>>n;
		rp(i,1<<n)
			cin>>need[i];
		rp(i,n)
			rp(j,1<<(n-1-i))
			cin>>c[i][j];
		m.clear();
		cout<<"Case #"<<t+1<<": "<<dfs(mp(mp(0,1<<n),0))<<endl;
	}
}
