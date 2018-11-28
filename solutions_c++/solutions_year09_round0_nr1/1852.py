#include <iostream>

using namespace std;

const int MAXN = 5010*15;

int g[MAXN][26], last[MAXN], now[MAXN];
bool mark[MAXN];
int t, l, d, n;

void work()
{
     int h, w, i, j, m, k;
     char c;
     char cc[100];
     
     memset(last, 0, sizeof(last));
     memset(mark, 0, sizeof(mark));
     h = 1;
     last[1] = 1;
     mark[1] = true;
     for (i=1; i<=l; i++)
     {
         m = 0;
         scanf("%c", &c);
         if (c=='('){
             while (scanf("%c", &c), c!=')') cc[++m] = c;            
         }     
         else
         {
             m=1;
             cc[1] = c;
         }  
         w = 0;
         for (j=1; j<=h; j++)
             for (k=1; k<=m; k++)
                 if (g[last[j]][cc[k]-'a']!=0 && !mark[g[last[j]][cc[k]-'a']]){
                    w++;
                    now[w] = g[last[j]][cc[k]-'a'];
                    mark[g[last[j]][cc[k]-'a']] = true;
                 }
         h = w;
         for (j=1; j<=h; j++) last[j] = now[j];
     }
     scanf("%c", &c);          
     printf("%d\n", w);
}
     
int main()
{
    int i, j, p;
    char c;
    
    scanf("%d%d%d\n", &l, &d, &n);
    memset(g, 0, sizeof(g));
    t = 1;    
    for (i=1; i<=d; i++){
        p = 1;
        for (j=1; j<=l; j++)
        {
            scanf("%c", &c);
            if (g[p][c-'a']==0)
            {
               t++;
               g[p][c-'a'] = t;
            }                 
            p = g[p][c-'a'];
        }
        
        while (scanf("%c", &c), c!='\n');
    }               
            
    i = 0;
    while (n--){    
          i++;
          printf("Case #%d: ", i);
          work();
    } 
    
    return 0;
}
