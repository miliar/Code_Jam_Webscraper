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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define INF 1e8
#define EPS 1e-8
#define MOD 1000000007
#define SQR(a) ((a)*(a))
typedef long long  ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

#define SIZE 110
vector<PII> v;
int n,d;
bool isok(long double time)
{
	long double pos=v[0].first-time;
	FR(i,n)
	{
		FR(j,v[i].second)
		{
			if(pos<=v[i].first) pos=max(v[i].first-time,pos);
			else if(v[i].first+time<pos) return false;
			pos+=d;
		}
	}
	return true;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tt;cin>>tt;FR(cas,tt)
	{
		printf("Case #%d: ",cas+1);
		cin>>n>>d;v.clear();
		FR(i,n)
		{
			PII p;cin>>p.first>>p.second;
			v.push_back(p);
		}
		sort(ALL(v));
		bool flag=false;
		FR(i,n)
		{
			if(v[i].second!=1) flag=true;
			if(i!=0 && v[i].first-v[i].second<d) flag=true;
		}
		cout<<fixed<<setprecision(8);
		if(!flag) {cout<<0<<endl;continue;}
		long double low=0,mid;
		long double high=(1LL<<60);
		while(high-low>1e-9)
		{
			mid=(low+high)/2;
			if(isok(mid)) high=mid;
			else low=mid;
		}
		cout<<mid<<endl;
	}
}