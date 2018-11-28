#include<stdio.h>
#include<stdlib.h>

int T, R, C, l;
char pic[55][55];

bool work(int i, int j)
{
     if(i >= R - 1 || j >= C - 1)
         return false;
         
     if(pic[i+1][j] == '#' && pic[i+1][j+1] == '#' && pic[i][j+1] == '#') {
           pic[i][j] = '/';
           pic[i+1][j+1] = '/';
           pic[i][j+1]= '\\' ;
           pic[i+1][j] =  '\\' ;
           return true;
     }
     
     return false;
         
}

void solve()
{
     scanf("%d%d", &R, &C);
     for(int i = 0; i < R; ++i) {
          scanf("%s", pic[i]);   
     }
     
     printf("Case #%d:\n", l);
     for(int i = 0; i < R; ++i) 
     for(int j = 0; j < C; ++j) {
          if(pic[i][j] == '#') {
               if(!work(i, j)) {
                     printf("Impossible\n");
                     return;       
               }
          }     
     }  

     
     for(int i =0; i < R; ++i) {
          for(int j = 0; j < C; ++j)
              printf("%c", pic[i][j]);
          printf("\n");
     }
}
     
int main()
{
     freopen("A-large.in", "r", stdin);
     freopen("A-large.out", "w", stdout);
     
     scanf("%d", &T);
     for(l = 1; l <= T; ++l) {
          solve();  
     }
             
    // system("pause");   
}

