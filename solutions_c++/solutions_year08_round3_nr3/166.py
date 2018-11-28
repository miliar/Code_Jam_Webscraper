// pro1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

//#if defined (__GNUC__) && (__GNUC__ <= 2)
//#include <hash_map>
//#include <hash_set>
//#else
//#include <ext/hash_map>
//#include <ext/hash_set>
//using namespace __gnu_cxx;
//#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
const int mn=1002;
__int64 n,m,x,y,z,a[mn],b[mn];
__int64 dp[mn];
int main()
{
	//freopen("test.txt","r",stdin);
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	/*freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);*/
	int N;
	cin>>N;
	for(int cases=1;cases<=N;cases++)
	{
		cin>>n>>m>>x>>y>>z;
		REP(i,m)
			cin>>a[i];
		REP(i,n)
		{
			b[i]=a[i%m];
			a[i%m]=(x*a[i%m] +y*(i + 1))%z;
		}
		REP(i,mn)
			dp[i]=1;
		//memset(dp,1,sizeof(dp));
		//dp[0]=1;
		__int64 total=dp[0];
		for(int k=1;k<n;k++)
		{
			//int sum=0;
			for(int i=0;i<k;i++)
			{
				if(b[k]>b[i]) 
				{
					dp[k]=(dp[k]+dp[i])%1000000007;
					//if(dp[i]==0) sum+=1;
					//else sum+=dp[i];
				}
			}
			//dp[k]=sum;
			total=(total+dp[k])%1000000007;
			if(total<0)
			{
				cout<<endl;
			}
		}

		cout<<"Case #"<<cases<<": "<<total<<endl;
	}
	return 0;
}

