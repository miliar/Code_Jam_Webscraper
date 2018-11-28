#include <cstdio>
#include <algorithm>
using namespace std;

#define Cmax 1000001

int T, t, C, D, i;
int P[Cmax], V[Cmax], ind[Cmax];
double st[Cmax], dr[Cmax];

int cmp(const int &a, const int &b)
{
 return P[a] < P[b];
}

double max(double a, double b) { return a>b?a:b; }
double min(double a, double b) { return a<b?a:b; }
double modul(double a) { return a>0?a:-a; }

int check(double nr)
{
 double l, r, L1, L2;
 //stanga
 r = -10000000000000000000.0;
 for (i=0; i<C; ++i)
     {
      l = max(P[ind[i]] - nr, r + D);      
      r = l + (V[ind[i]]-1) * D;
      st[i] = r;
      if ( modul(l - P[ind[i]]) > nr || modul(r - P[ind[i]]) > nr) break;
     }
 L1 = i;
 if (L1 == C) return 1;
 //dreapta
 l = 10000000000000000000.0;
 for (i=C-1; i>=0; --i)
     {
      r = min(P[ind[i]] + nr, l - D);
      l = r - (V[ind[i]]-1) * D;
      dr[i] = l;
      if ( modul(l - P[ind[i]]) > nr || modul(r - P[ind[i]]) > nr) break;
     }
 L2 = i;
 if (L2<0) return 1;
 /*
 printf("%.2lf\n", nr);
 for (i=0; i<=L1; ++i)
     printf("%.2lf ", st[i]);
 printf("\n");
 for (i=L2; i<C; ++i)
     printf("%.2lf ", dr[i]);
 printf("\n\n");
 */
 //cauta
 for (i=L2; i<L1; ++i)
     if (st[i] + D <= dr[i+1]) return 1;
 return 0;
}

void cauta()
{
 double p = 10000000.0;
// double p = 10;
 double nr = 0, aux;
 
 while (p > 0.00000001)
       {
        aux = nr + p;
        if (!check(aux)) nr += p;
        p /= 2;
       }
 printf("Case #%d: %.6lf\n", t, nr);
}

int main()
{
 freopen("b.in","r",stdin);
 freopen("b.out","w",stdout);
 
 scanf("%d", &T);
 for (t=1; t<=T; ++t)
     {
      scanf("%d %d", &C, &D);
      for (i=0; i<C; ++i)
          {
           scanf("%d %d", &P[i], &V[i]);
           ind[i] = i;
          }
      
      sort(ind, ind+C, cmp);
      
      cauta();
      
     }
 
 return 0;
}
