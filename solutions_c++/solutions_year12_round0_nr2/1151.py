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
int a[1000];
int n,p;
int memo[200][200];
int f(int ind,int s)
{
	if(s<0) return -1000000;
	if(ind==n)
	{
		if(s==0) return 0;
		return -1000000;
	}
	int res=-1000000;
	int &ret=memo[ind][s];
	if(ret!=-1) return ret;
	FR(i,11) FOR(j,max(0,i-2),min(11,i+3)) FOR(k,max(0,i-2),min(11,i+3))
	{
		if(i+j+k!=a[ind]) continue;
		if(abs(k-j)>2) continue;
		int isnum=0;
		int ispoint=0;
		if(max(i,max(j,k))>=p) ispoint=1;
		if(abs(i-j)==2 || abs(k-j)==2 || abs(i-k)==2) isnum=1;
		res=max(res,ispoint+f(ind+1,s-isnum));
	}
	return ret=res;

}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);	
	int t;cin>>t;
	FR(cas,t)
	{
		printf("Case #%d: ",cas+1);
		cin>>n;
		int s;cin>>s>>p;
		FR(i,n) cin>>a[i];
		CLR(memo,-1);
		cout<<f(0,s)<<endl;
	}
}