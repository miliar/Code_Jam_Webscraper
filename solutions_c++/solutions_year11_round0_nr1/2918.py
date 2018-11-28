#include <cstdio>

int N, T, t, tt, m1, m2, p1, p2, p;
char C;

inline int modul(int a) { return a>0?a:-a; }
inline int poz(int a) { return a>0?a:0; }

int main()
{
 freopen("test.in","r",stdin);
 freopen("test.out","w",stdout);
 
 scanf("%d\n", &t);
 
 for (tt=1; tt<=t; ++tt)
 {
 
 scanf("%d ", &N);
 
 p1 = p2 = 1;
 m1 = m2 = T = 0;
 while (N--)
       {
        scanf("%c %d ",&C, &p);
        if (C=='O')
           {
            m2 += poz( modul(p-p1) - m1 ) + 1;
            T += poz( modul(p-p1) - m1 ) + 1;
            p1 = p;
            m1 = 0;//poz(m1-modul(p-p1));
           }
        else
            {
             m1 += poz( modul(p-p2) - m2 ) + 1;
             T += poz( modul(p-p2) - m2 ) + 1;
             p2 = p;
             m2 = 0;//poz(m2-modul(p-p2));             
            }   
        //printf("%d %d\n",m1,m2);
       }
  printf("Case #%d: %d\n",tt,T);
 }
}
