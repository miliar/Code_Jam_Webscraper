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

int n, k, wynik, tab[1000007], supr, p, a, b, c;

int main()
{
	scanf("%d", &n);
	for(int j=0; j<n; j++)
	{
		scanf("%d %d %d", &k, &supr, &p);
		wynik = 0;

		for(int i=0; i<k; i++)
		{
		    scanf("%d", &a);
		    b = (a+2)/3;
		    c = max(0, b-1);
//		    printf("   -> %d %d %d\n", a, b, c);
		    if(b >= p)   wynik++;
		    else
		    {
		        if(supr > 0 && a - 2*c >= p)
		        {
		            supr--;
		            wynik++;
		        }
		    }
		}

		printf("Case #%d: %d\n", j+1, wynik);
	}



	return 0;
}
