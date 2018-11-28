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

int n, k, w, h;
int wynik;
/*
void wkladaj(int nr, int pocz, int kon, int p, int k, int ile)
{
    if(p == pocz && k == kon)
    {
        d[nr].il = ile;
        d[nr].minn = ile;
        d[nr].szer = kon - pocz;
        return ;
    }
    int s = (pocz + kon)/2;
    if(p > s)
        wkladaj(nr*2+1, s+1, kon, p, k, ile);
}
*/
struct prost
{
    int lewo;
    int prawo;
    int dol;
    int x;
    int y;
};
list <prost> stos;
prost p, p1, p2, p3;

struct osoba
{
    int nr;
    int r;
    int x;
    int y;
};
osoba tab[10007], o;


class comp
{
     public:
     bool operator ()(const osoba & f, const osoba & s)
     {
          if(f.r == s.r)   return f.nr < s.nr;
          if(f.r > s.r)   return true;
          return false;
     }
};
set <osoba, comp> S;


bool dopasuj(prost pr, osoba &oss)
{
    int r = min(pr.x == 0 ? (pr.prawo == w ? M : 2*(p.prawo - p.lewo)) : (pr.prawo == w ? 2*(p.prawo - p.lewo) : (p.prawo - p.lewo), (p.prawo - p.lewo)/2), pr.y == 0 ? M : h-pr.dol);

    osoba os;
    os.r = r;
    os.nr = -1;

    set <osoba, comp>::iterator it = S.lower_bound(os);

    if(it == S.end())
    {
        return 0;
    }

    o = *it;

    o.x = (pr.x == 0) ? pr.x : pr.x+o.r;
    o.y = (pr.y == 0) ? pr.y : pr.y+o.r;

    return 1;
}


int main()
{
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; test++)
	{
		scanf("%d %d %d", &n, &w, &h);
		stos.clear();
		S.clear();

		for(int i=0; i<n; i++)
		{
		   scanf("%d", &tab[i].r);
		   tab[i].nr = i;
		   S.insert(tab[i]);
		}

		p.lewo = 0;
		p.prawo = w;
		p.dol = 0;
		p.x = 0;
		p.y = 0;

		stos.push_back(p);

		while(!S.empty())
		{
		    p = stos.front();

		    //osoba o;
		    if(dopasuj(p, o))
		    {
//		        printf("wklada %d (%d, %d) do (%d, %d, %d) (%d, %d)\n", o.r, o.x, o.y, p.lewo, p.prawo, p.dol, p.x, p.y);
		        S.erase(o);
                stos.pop_front();

                tab[o.nr].x = o.x;
                tab[o.nr].y = o.y;

                p1 = p;
                p2 = p;

                p1.lewo = o.x + o.r;
                p1.x = p1.lewo;

                p2.prawo = p1.lewo;
                p2.dol = o.y + o.r;
                p2.y = p2.dol;

                stos.push_front(p1);
                stos.push_front(p2);
		    }
            else   stos.pop_front();
		}

		printf("Case #%d:", test);
		for(int i=0; i<n; i++)
            printf(" %d %d", tab[i].x, tab[i].y);
        printf("\n");
	}


	return 0;
}
