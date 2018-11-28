#include<stdio.h>
#include<stdlib.h>


int T, C, D, N, l;
bool opp[26][26];
char com[26][26];
char list[105];

void solve()
{
     for(int i = 0; i < 26; ++i) 
        for(int j = 0; j < 26; ++j) {
             opp[i][j] = 0;   
             com[i][j] = -1;
        }
        
     scanf("%d", &C);
     for(int i = 0; i < C; ++i) {
          char a, b, c;
          scanf(" %c%c%c",&a, &b, &c);
          com[a-'A'][b-'A'] =  com[b-'A'][a-'A'] = c;
     }
     
     scanf("%d", &D);
     for(int i= 0; i < D; ++i) {
          char a, b;
          scanf(" %c%c", &a, &b);
          opp[a-'A'][b-'A'] = opp[b-'A'][a-'A']=1;    
     }
     
     scanf("%d ", &N);
     int loc = 0;
     for(int i = 0; i < N; ++i) {
          scanf("%c", &list[loc]);
          if(loc >0) {
               int a = list[loc-1] - 'A';
               int b = list[loc]- 'A';
               if(com[a][b] != -1) {
                    list[loc-1] = com[a][b];  
                    continue;    
               }
               else {
                    int j = 0;
                    for(; j < loc; ++j) {
                         int a = list[j] - 'A';
                         int b = list[loc] - 'A';
                         if(opp[a][b] != 0) {
                              break;        
                         }
                    }
                    if(j < loc) {
                         loc = 0;
                         continue;     
                    }
               }
                            
          }  
          ++loc;
     }
     
     printf("Case #%d: [", l);
     for(int i = 0; i < loc; ++i) {
          printf("%c", list[i]);
          if(i < loc - 1) 
               printf(", "); 
     }
     printf("]\n");
}
     
int main()
{    
     freopen("B-large.in","r",stdin);
     freopen("B-large.out","w",stdout);
     scanf("%d", &T);
     for(l = 1; l <= T; ++l) {
          solve();        
     }
     
    // system("pause");
     return 0;
}
