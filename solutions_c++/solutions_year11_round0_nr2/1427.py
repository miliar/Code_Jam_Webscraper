#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int c, d, n;
int a[200];
bool dd[30][30];
int cc[30][30];

char getch()
{
     char c;
     while (scanf("%c", &c), c<'A' || c>'Z');
     return c;     
}
     
void init()
{
     char c1, c2, c3, d1, d2;
     
     for (int i = 0; i < 26; ++i)
         for (int j = i; j < 26; ++j){
             cc[j][i] = cc[i][j] = -1;
             dd[j][i] = dd[i][j] = false;
         }             
             
     scanf("%d", &c);
     for (int i = 0; i < c; ++i){
         c1 = getch();
         c2 = getch();
         c3 = getch();
         cc[c1-'A'][c2-'A'] = cc[c2-'A'][c1-'A'] = c3-'A';
     }     
     scanf("%d", &d);
     for (int i = 0; i < d; ++i){
         d1 = getch();
         d2 = getch();
         dd[d1-'A'][d2-'A'] = dd[d2-'A'][d1-'A'] = true;    
     }
     scanf("%d", &n);
     for (int i = 0; i < n; ++i)
         a[i] = (int)(getch()-'A');
}
     
void work()
{
     int p;
     int st[200];
     
     p = 0;
     memset(st, 0, sizeof(st));
     for (int i = 0; i < n; ++i){
         ++p;
      //   printf("--->%d", a[i]);
         st[p] = a[i];
         if (p>1 && cc[st[p-1]][st[p]]!=-1){
            st[p-1] = cc[st[p-1]][st[p]];        
            --p;
         }
         else
         {
             int j;
             for (j = p-1; j >0; --j)
                 if (dd[st[j]][st[p]]) break;
             if (j>0){
                p = 0;        
             }
         }
      //   printf("(%d %d)\n", p, st[p]);
     }
     printf("[");
     for (int i = 1; i <= p; ++i){
         printf("%c", (char)(st[i]+'A'));
         if (i<p) printf(", ");
     } 
     printf("]\n");
}
     
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output1.txt", "w", stdout);
    int cases, t = 0;
    scanf("%d", &cases);
    while (cases--){
          ++t;      
          printf("Case #%d: ", t);
          init();
          work();
    }
    return 0;
}
