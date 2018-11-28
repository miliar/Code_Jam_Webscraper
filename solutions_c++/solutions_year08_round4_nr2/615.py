#include <cstdio>

int abs(int x){ if (x < 0) return -x; return x; }

int area(int x1, int y1, int x2, int y2, int x3, int y3){
    return abs(y1*(-x2+x3) + y2*(x1-x3) + y3*(x2-x1));
}

int main(){
    int tcc = 0, tc = 0;
    for(scanf("%d", &tc); tc; --tc){
         int n, m, a;
         scanf("%d %d %d", &n, &m, &a);
         
         char done = 0;
         
         for (int x3 = 1; x3 <= n && !done; x3++){
             if ( a % x3 == 0 ){
                int y2 = a / x3;
                if ( y2 <= m ){
                   done = 1;
                   printf("Case #%d: 0 0 %d %d %d %d\n", ++tcc, 0, y2, x3, 1);                   
                }
             }
         }
         
         for (int x2 = 1; x2 <= n && !done; x2++)
             for (int y2 = 0; y2 <= m && !done; y2++)
                 for (int x3 = 0; x3 <= n && !done; x3++){
                     int t = a + y2 * x3;
                     if ( t < 0 ) continue;
                     if ( t % x2 == 0 ){
                        int y3 = t / x2;
                        if ( (x2 != x3 || y2 != y3) && y3 <= m  ) {
                           done = 1;
                           printf("Case #%d: 0 0 %d %d %d %d\n", ++tcc, x2, y2, x3, y3);
                        }
                     }
                 }
         
         if ( !done )
                  printf("Case #%d: IMPOSSIBLE\n", ++tcc);
    }
    return 0;    
}
