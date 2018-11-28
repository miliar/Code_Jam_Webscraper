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
#define PII pair<int,int> 
using namespace std;
PII tab[1010];
int main()
{
	int Z;
	scanf("%d",&Z);
	FOR(h,1,Z+1)
	{
		int n;
		int w=0;
		scanf("%d",&n);
		FOR(i,0,n)
			scanf("%d%d",&tab[i].F,&tab[i].S);
		FOR(i,0,n)
		{
			FOR(j,0,n)
			{
				if(i==j)continue;
				if(tab[i].F>tab[j].F&&tab[i].S<tab[j].S)
					w++;
				else if(tab[i].F<tab[j].F&&tab[i].S>tab[j].S)
					w++;
			}
		}
		printf("Case #%d: %d\n",h,w/2);
	}
	return 0;
}