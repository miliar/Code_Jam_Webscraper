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
#define SQR(a) ((a)*(a))
typedef long long  ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<ll,ll> PII;
typedef pair<double,double> PDD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define EPS 1e-8
const ll INF=1LL<<55;
#define MOD 1000000007
#define SIZE 100010

vector<pair<char,int> > v;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;cin>>t;FR(cas,t)
	{
		printf("Case #%d: ",cas+1);
		int n;cin>>n;
		v.clear();
		FR(i,n)
		{
			pair<char,int> p;
			cin>>p.first>>p.second;
			v.push_back(p);
		}
		int time=0;
		int ind=0;
		int posO,posB;posO=posB=1;
		while(ind!=v.size())
		{
			time++;
			int nextO,nextB;nextO=nextB=0;
			FOR(i,ind,v.size())
			{
				if(v[i].first=='O' && nextO==0) nextO=v[i].second;
				if(v[i].first=='B' && nextB==0) nextB=v[i].second;
			}
			if(v[ind].first=='O' && posO==v[ind].second)
			{
				int temp=abs(nextB-posB);
				if(temp>abs(nextB-posB-1)) posB++;
				else if(temp>abs(nextB-posB+1)) posB--;
				ind++;
				continue;
			}
			if(v[ind].first=='B' && posB==v[ind].second)
			{
				int temp=abs(nextO-posO);
				if(temp>abs(nextO-posO-1)) posO++;
				else if(temp>abs(nextO-posO+1)) posO--;
				ind++;
				continue;
			}
			int temp=abs(nextB-posB);
			if(temp>abs(nextB-posB-1)) posB++;
			else if(temp>abs(nextB-posB+1)) posB--;
			temp=abs(nextO-posO);
			if(temp>abs(nextO-posO-1)) posO++;
			else if(temp>abs(nextO-posO+1)) posO--;
		}
		cout<<time<<endl;
	}
}