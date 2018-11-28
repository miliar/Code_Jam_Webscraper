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

int n, k, wynik, a, b;
int tab[10], dl, w, l, l2, flaga, il;
int ile[] = {0, 0, 1, 1, 2, 1, 3}, jakie[][3] = {{}, {}, {1}, {1}, {1, 2}, {1}, {1, 2, 3}};

inline static bool sprawdz(int krok)
{
    l2 = 0;
    for(int i=0; i<dl; i++)
    {
        l2 = l2*10 + tab[(dl+krok-i)%dl];
    }
}

inline static int policz(int liczba)
{
//    printf("sprawdza %d\n", liczba);
    dl = 0, w = 0, l = liczba, il = 0;
    while(liczba > 0)
    {
        tab[dl] = liczba%10;
        dl++;
        liczba /= 10;
    }
    for(int i=0; i<dl; i++)
    {
//        printf("    przes o %d\n", jakie[dl][i]);
        sprawdz(i);
        il += (l == l2);
        w += (l < l2 && l2 <= b);
//        printf("%d %d\n", l, l2);
    }
//    printf("  wyszlo %d\n", w);
//    printf("%d daje w:%d, il:%d\n", l, w, il);
    return w/il;
}

int main()
{
	scanf("%d", &n);
	for(int j=0; j<n; j++)
	{
		scanf("%d %d", &a, &b);
		wynik = 0;
		for(int i=a; i<=b; i++)
		{
		    wynik += policz(i);
		}
		printf("Case #%d: %d\n", j+1, wynik);
	}


	return 0;
}
