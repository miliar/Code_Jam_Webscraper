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
#define EPS 0.00000000001
#define LLD long long int
using namespace std;


int main()
{
	int Z;
	scanf("%d",&Z);
	FOR(h,1,Z+1)
	{
		LLD l,p,c;
		scanf("%lld%lld%lld",&l,&p,&c);
		LLD dif= (log((double)p)/log((double)c))-(log((double)l)/log((double)c));
		if(p>l*(LLD)pow((double)c,(double)dif))dif++;
		LLD w=(LLD)ceil(log((double)dif)/log(2.0));
		printf("Case #%d: %lld\n",h,w);
	}
	return 0;
}