#include<iostream>
using namespace std;
int T;
int C, D, N;
char lc[64][4], ld[64][4]; 
char S[512];

     
 char stk[512];
 int top = 0;
 void CheckC()
 {
     if(top < 2) return;
     int i, j; 
     for(i = 0; i < C; ++i)
         if(lc[i][0] == stk[top-1] && lc[i][1] == stk[top-2]
          || lc[i][1] == stk[top-1] && lc[i][0] == stk[top-2])
          {
              top -= 2;
              stk[top++] = lc[i][2];
              return;
          }
 } 
  void CheckD()
 {
     if(top < 2) return;
     int i, j; 
     for(i = 0; i < D; ++i)
         if(ld[i][0] == stk[top-1])
          {
              for(j = 0; j < top - 1; ++j)
                  if(stk[j] == ld[i][1])
                  {
                     top = 0;
                     return;
                  }

          }
          else if(ld[i][1] == stk[top-1])
          {
              for(j = 0; j < top - 1; ++j)
                  if(stk[j] == ld[i][0])
                  {
                     top = 0;
                     return;
                  }

          }
 } 
int main()
{
    int i, j;
    int cs = 0; 
    freopen("B_L.in", "r", stdin);
    freopen("B_L.out", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
              
              top = 0;
              
         scanf("%d", &C);
         
         for(i = 0; i < C; ++i)
             scanf("%s", lc[i]);
         
         scanf("%d", &D);
         
         for(i = 0; i < D; ++i)
             scanf("%s", ld[i]);
         
         scanf("%d", &N);
         scanf("%s", S);
    
         
         for(i = 0; i < N; ++i)
         {
             stk[top++] = S[i];
             
             CheckC();
             CheckD();
         }
          
          printf("Case #%d: ", ++cs);
          printf("[");
          for(i = 0; i < top; ++i)
             {
                  
                  if(i) printf(", ");
                  printf("%c", stk[i]);
              }
          printf("]\n");
    }
}
