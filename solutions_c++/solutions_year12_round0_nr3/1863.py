#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <utility>
#include <sstream>

#define FOR(i,a,n) for(i=(a);i<(n);++i)
#define FORIT(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define f0(a) memset(a,0,sizeof(a))
#define fx(a,x) memset(a,(x),sizeof(a))

#define _bc(i) __builtin_popcount(i)
#define all(v) v.BE,v.EN
#define sz size()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define BE begin()
#define EN end()
#define IT iterator

using namespace std;
typedef vector <int> 	VI;
typedef vector < VI > 	VVI;
typedef vector<string> 	VS;
typedef pair<int,int> 	II;
typedef vector<II > 	VII;
typedef map<int,int> 	MII;
typedef long long 	lint;

#define INF (1<<30)		//or 0x7ffffff0 for 2^31-16 = 2147483647 
#define MINF 0x80000000		//-2^31
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
template<class T> string i2s(T x) { ostringstream o; o<<x; return o.str(); }
int s2i(string x) {int r=0;istringstream sin(x);sin>>r;return r; }
template<class T>
inline void _min(T &mn, T x)
{
	if(mn > x) mn=x;
}
template<class T>
inline void _max(T &mx, T x)
{
	if(mx < x) mx=x;
}
/*******************/

#define MX 2000000
bool mark[MX+1];
void solve()
{
	int A,B,n,k,cnt=0,i,j;
	string a,b;
	
	A=SS; B=SS;
	memset(mark,false,sizeof(bool)*(B+1));
	
	for(i=A; i<B; i++){
		if(mark[i])
			continue;
		a=i2s(i);
		n=a.sz;
		map<int,int> mp;
		mp[i]=1;
		for(j=1; j<n; j++)
		{
			//b=getRot(a,n,j)
				b="";
				for(k=j; k<n; k++)
					b+=a[k];
				for(k=0; k<j; k++)
					b+=a[k];
			/**/
			int bb=0;
			for(k=0; k<n; k++)
				bb=bb*10+(b[k]-'0');
				
			if(bb>i && bb <=B){
				if(mp.count(bb)==0){
					mp[bb]=1;
					mark[bb]=true;
				}
			}
		}
		int m=mp.sz;
		cnt+=(m*(m-1))/2;
	}	
	printf("%d\n",cnt);
}

int main()
{
	int t,test;
	scanf("%d\n",&test);
	for(int t=1; t<=test; t++)
	{
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
