#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
int gcd( int m, int n )
{
	int a=max(m,n),b=min(m,n);
	if(m==0) return n;if(n==0) return m;
	if(a%b==0) return b;
	return gcd(b,a-b*(a/b));
}
int main()
{
	int i,t,pd,pg;lint n;cin>>t;
	for(i=0;i<t;i++){
		scanf("%lld %d %d",&n,&pd,&pg);
		if((pg<1 && pd>0) || (pg>99 && pd<100)){
			printf("Case #%d: Broken\n",i+1);continue;
		}
		lint c=100/gcd(100,pd);//cout<<n<<endl;
		if(c<=n) printf("Case #%d: Possible\n",i+1);
		else printf("Case #%d: Broken\n",i+1);
	}
	return 0;
}
