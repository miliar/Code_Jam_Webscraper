#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <list>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair
#define pi acos(-1.0)
#define MAXN 1010
#define inf 1000000000
#define eps 1e-5
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int main()
{
	int cs,c,a,b,i;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cs);
	for (c=1;c<=cs;c++)
	{
		scanf("%d%d",&a,&b);
		for (i=0;i<a;i++)
			if ((b&(1<<i))==0) break;
		if (i==a) printf("Case #%d: ON\n",c);
		else printf("Case #%d: OFF\n",c);
	}
	return 0;
}
