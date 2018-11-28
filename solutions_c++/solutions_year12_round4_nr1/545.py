// Artur Kraska, II UWr

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <list>
#include <set>
#include <map>

#define znak(z)                     ((z) <= '9' ? (z)-'0' : (z) - 'A'+10)
#define foreach(iter, coll)         for(typeof(coll.begin()) iter = coll.begin(); iter != coll.end(); ++iter)
#define foreachr(iter, coll)        for(typeof(coll.rbegin()) iter = coll.rbegin(); iter != coll.rend(); ++iter)
#define lbound(P,R,PRED)            ({typeof(P) X=P,RRR=(R), PPP = P; while(PPP<RRR) {X = (PPP+(RRR-PPP)/2); if(PRED) RRR = X; else PPP = X+1;} PPP;})

#define M 1000000007

using namespace std;

int n, k, tab[1000007];
int wynik, koniec;

struct liana
{
    int d;
    int l;
    int maks;
};
liana t[1000007];

bool comp(liana f, liana s)
{
    return f.d < s.d;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; test++)
	{
		scanf("%d", &n);

        for(int i=0; i<n; i++)
        {
            scanf("%d %d", &t[i].d, &t[i].l);
            t[i].maks = 0;
        }

        scanf("%d", &t[n].d);
        t[n].l = M;
        t[0].maks = t[0].d;
        t[n].maks = 0;

        sort(t, t+n, comp);

        for(int i=0; i<n; i++)
        {
            t[i].maks = min(t[i].maks, t[i].l);
            for(int j=i+1; j<=n; j++)
            {
                if((t[i].maks >= t[j].d - t[i].d)) // && (t[j].l >= t[j].d - t[i].d))
                {
                    t[j].maks = max(t[j].maks, t[j].d - t[i].d);
//                    printf("maks w %d z %d to %d\n", j, i, t[j].maks);
                }
            }
        }

		printf("Case #%d: %s\n", test, t[n].maks > 0 ? "YES" : "NO");
	}


	return 0;
}
