#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int pg, pd, ig, id, w, wins_g, wins_d, loose_d, loose_g;
long long n;

long long gcd(long long a, long long b)
{
    if(b == 0)   return a;
    return   gcd(b, a%b);
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int i=0; i<tests; i++)
	{
		scanf("%I64d", &n);
		scanf("%d %d", &pd, &pg);
		ig = 100 / gcd(pg, 100);
		id = 100 / gcd(pd, 100);
		w = ig * id / gcd(ig, id);
		wins_g = pg * w / 100;
		wins_d = pd * id / 100;
		loose_g = w - wins_g;
		loose_d = id - wins_d;
//		printf("%d %d -> %d\n", id, ig, w);
//		printf("%d, %d - %d, %d\n", wins_d, loose_d, wins_g, loose_g);

		if(pg == 100 && pd != 100)   printf("Case #%d: Broken\n", i+1);
//		else   if(pd == 100 && pg != 100)   printf("Case #%d: Broken\n", i+1);
		else   if(pg == 0 && pd != 0)   printf("Case #%d: Broken\n", i+1);
		else
		{
		    int x, y, z;
		    x = wins_g;
		    y = loose_g;
		    z = id;
		    while(x < wins_d || y < loose_d)
		    {
		        x += wins_g;
		        y += loose_g;
		        z += id;
		    }
		    if(z > n)   printf("Case #%d: Broken\n", i+1);
		    else   printf("Case #%d: Possible\n", i+1);
		}
	}

	return 0;
}
