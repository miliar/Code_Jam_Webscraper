#include <iostream>
using namespace std;
 
#define MaxN 100
#define INF 10001

int a[MaxN][MaxN];
int p[MaxN][MaxN];
int ret[MaxN][MaxN];
bool mark[MaxN][MaxN];
int t,h,w;
int ch;
int pi,pj,ph;

void Odredi( int r, int c )
{
     
     ph = INF;
     if ( r > 0 )   if ( a[r-1][c] < ph ) { pi = r-1; pj = c;   ph = a[r-1][c]; }
     if ( c > 0 )   if ( a[r][c-1] < ph ) { pi = r;   pj = c-1; ph = a[r][c-1]; }
     if ( c < w-1 ) if ( a[r][c+1] < ph ) { pi = r;   pj = c+1; ph = a[r][c+1]; }
     if ( r < h-1 ) if ( a[r+1][c] < ph ) { pi = r+1; pj = c;   ph = a[r+1][c]; }

     if ( ph == INF || ph >= a[r][c] ) p[r][c] = -1;
     else                              p[r][c] = pi*w + pj;

}

int Solve( int r, int c )
{
     
     if ( mark[r][c] ) return ret[r][c];
     mark[r][c] = true;
     
     if ( p[r][c] == -1 ) ret[r][c] = ++ch;
     else                 ret[r][c] = Solve( p[r][c]/w, p[r][c]%w );
     
     return ret[r][c];
}

int main()
{
    
    scanf("%d",&t);
    for (int k = 0; k < t; k++) {
    
        scanf("%d%d",&h,&w);
        for (int i = 0; i < h; i++)
          for (int j = 0; j < w; j++)
            scanf("%d",&a[i][j]);
            
        for (int i = 0; i < h; i++)
          for (int j = 0; j < w; j++)
            Odredi(i,j);
          
        memset(mark, 0, sizeof(mark));
        ch = 'a'-1;
        for (int i = 0; i < h; i++)
          for (int j = 0; j < w; j++) {
             if ( mark[i][j] ) continue;
             if ( p[i][j] == -1 ) ret[i][j] = ++ch;
             else                 ret[i][j] = Solve(p[i][j]/w,p[i][j]%w);
             mark[i][j] = true;
          }
        
        printf("Case #%d:\n",k+1);
        for (int i = 0; i < h; i++) {
            printf("%c",ret[i][0]);
            for (int j = 1; j < w; j++)
              printf(" %c",ret[i][j]);
            printf("\n");
        }
    
    }
    
    return 0;
    
} 
