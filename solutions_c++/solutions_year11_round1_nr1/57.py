// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;
int main()
{
	int t,cas=0;
	LL n,pd,pg,qd,qg;
	scanf("%d",&t);
	while ( t-- ) {
		scanf("%I64d%I64d%I64d",&n,&pd,&pg);
		if ( pd>0 && pg==0 ) { printf("Case #%d: Broken\n",++cas); continue; }
		if ( pd<100 && pg==100 ) { printf("Case #%d: Broken\n",++cas); continue; }
		qd=100/__gcd(100LL,pd);
		//qg=100/__gcd(100,pg);
		printf("Case #%d: %s\n",++cas,qd<=n?"Possible":"Broken");
	}
	return 0;
}
