#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pii pair<int,int>
#define pdd pair<double,double>
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).size())
#define C(a) memset((a),0,sizeof(a))
#define VI vector <int>
#define ll long long
int a,b,c,d,i,j,n,m,k,kolt,r;
pii mas[1001];
map<int,pair<int,ll> > bil;
ll ans;
inline pair<int,ll> perform(int tot)
{
	ll pr=0;
	bil.clear();
	bil[0]=mp(0,pr);
	rep(i,tot)
	{
		if (mas[0].x>k){ r=0; return mp(r,pr); }
		a=0;
		int sum=0;
		while (a<n && sum+mas[a].x<=k)
		{
			sum+=mas[a].x;
			++a;
		}
		pr+=sum;
		ans+=sum;
		rotate(mas,mas+a%n,mas+n);
		--r;
		if (bil.count(mas[0].y))
		{
			pair<int,ll> rr=bil[mas[0].y];
			int len=i-rr.x;
			ll cs=pr-rr.y;
			return mp(len,cs);
		}
		bil[mas[0].y]=mp(i,pr);
	}
	return mp(tot,pr);
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		scanf("%d%d%d",&r,&k,&n);
		cout<<"Case #"<<hod<<": ";
		rept(i,n)
		{
			scanf("%d",&mas[i].x);
			mas[i].y=i;
		}
		ans=0;
		pair<int,ll> rr=perform(r);
		if (!r)
		{
			cout<<ans<<endl;
			continue;
		}
		int tot=r/rr.x;
		ans+=rr.y*tot;
		r-=rr.x*tot;
		rr=perform(r);
		cout<<ans<<endl;
	}
}
