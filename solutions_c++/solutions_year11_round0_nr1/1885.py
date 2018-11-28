#include<stdio.h>
#include<stdlib.h>


int T, N, l;
int bl, ol;
int bn[105], on[105];
bool col[105];
int butt[105];

void solve()
{
     for(int i = 0; i < N; ++i) {
          scanf(" %c%d", &col[i], &butt[i]);  
     } 
     
     bn[N] = on[N] =-1;
     for(int i = N-1; i >= 0; --i) {
          bn[i] = bn[i+1];
          on[i] = on[i+1];
          if(col[i] == 'B')
              bn[i] = butt[i];
          else
              on[i] = butt[i];
                
     }   
     
     bl = ol = 1;
     int t = 0;
     for(int i = 0; i < N; t++) {
          if(col[i] == 'B') {
               if(bl < butt[i]) {
                    bl++;      
               } 
               else if(bl > butt[i]) 
                    bl--;   
               else {
                    i++;
               }
               if(ol < on[i])
                    ol++;
               else if(ol > on[i])
                    ol--;               
                    
          }
          else {
               if(ol < butt[i])
                    ol++;
               else if(ol > butt[i])
                    ol--;
               else 
                    i++;
               if(bl < bn[i])
                    bl++;
               else if(bl > bn[i])
                    bl--;
          }
     }
     
     printf("Case #%d: %d\n", l, t);
}
     
int main()
{    
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
     scanf("%d", &T);
     for(l = 1; l <= T; ++l) {
          scanf("%d", &N);
         // printf(" cccc%dcccc ",N);
          solve();        
     }
     
    // system("pause");
     return 0;
}
