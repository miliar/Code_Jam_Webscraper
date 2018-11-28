/*
** In the name of God **
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iterator>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define EPS 1e-8
#define MOD 1000000007
#define INF 100000000
#define SQR(a) ((a)*(a))
#define e(a,b) (fabs(a-b)<EPS)
#define pb push_back
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

bool isValid(int x,int num)
{
	num-=x;
	for(int low=max(0,x-1); low <= min(x+1,10) ; low++)
		for(int high=max(0,x-1); high <= min(x+1,10) ; high++)
			if(abs(high-low)==2) continue;
			else if(low+high==num) return true;

	return false;
}

vector<int> b[31];

bool surp(int j,int k,int l)
{
	return((abs(j-k)==2 || abs (j-l)==2 || abs(k-l)==2)&& (abs(j-k)<=2 && abs (j-l)<=2 && abs(k-l)<=2));
		
}

void pre()
{
	FOR(i,2,31)
	{
		FR(j,min(i+1,11))FOR(k,j,min(i+1,11))FOR(l,k,min(i+1,11))
			if(j+k+l==i && surp(j,k,l))
			{
				VI t;t.pb(j);t.pb(k);t.pb(l);
				b[i]=t;
			}
	}
}

int main()
{
	pre();
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;scanf("%d",&t);
	int n,s,p;
	FOR(q,1,t+1)
	{
		scanf("%d%d%d",&n,&s,&p);
		VI a(n);
		vector<bool> vis(n);
		FR(i,n) scanf("%d",&a[i]);
		sort(ALL(a));
		if(s>0)FR(i,n)FOR(j,p,11)FR(k,b[a[i]].size())if(b[a[i]][k]==j)
		{
			s--;
			vis[i]=true;
			if(s==0) goto next;
		}
		/*if(s>0)
		{
			FR(i,n) if(!vis[i]) if(a[i]>=2 && a[i]<=28) s--;
		}*/
next:;
		FR(i,n) if(!vis[i]) FOR(j,p,11) 
			if(isValid(j,a[i]))
			{
				vis[i]=true;
			}

		int cnt=0;
		FR(i,n) cnt += vis[i];
		printf("Case #%d: %d\n",q,cnt);
	}
}