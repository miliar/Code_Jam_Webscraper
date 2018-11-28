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

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;cin>>t;FR(cas,t)
	{
		int n,x,i,min,sum; sum=0;
		int m[2000];
		printf("Case #%d: ",cas+1);
		cin>>n;
		cin>>m[0];
		min=m[0]; x=m[0];
		for (i=1;i<n;i++)
		{
			cin>>m[i];
			x=x^m[i];
		}
		for(i=0;i<n;i++)
		{
			sum=sum+m[i];
			if (min>m[i])
				min=m[i];
		}
		if (x==0)
			printf("%d",sum-min);
		else printf("NO");
		cout<<endl;
	}
}