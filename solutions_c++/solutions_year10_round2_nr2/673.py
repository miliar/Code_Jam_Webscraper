#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstring>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORD(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define PB push_back
#define F first
#define S second
#define MP make_pair
#define LLD long long int 
#define PII pair<LLD,LLD> 
using namespace std;
PII chick[1000001];

int main()
{
	int Z;
	scanf("%d",&Z);
	FOR(h,1,Z+1)
	{
		LLD n,k,b,t;
		scanf("%lld%lld%lld%lld",&n,&k,&b,&t);
		LLD temp;
		FOR(i,0,n){scanf("%lld",&temp);chick[i].F=temp;}
		FOR(i,0,n){scanf("%lld",&temp);chick[i].S=temp;}
		LLD chicks=0;
		temp=0;
		LLD wy=0;
		FORD(u,n-1,0)
		{
			if(chicks>=k)break;
			if((b-chick[u].F)<=(t*chick[u].S)){chicks++;wy+=temp;}
			else temp++;
		}
		printf("Case #%d: ",h);
		chicks==k?printf("%lld\n",wy):printf("IMPOSSIBLE\n");
	}
	return 0;
}
