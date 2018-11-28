#include<cstdio>

int T, R, C;

char tab[50][50];
bool possible;
int main()
{
    scanf("%d", &T);
    for(int z=0;z<T;z++)
    {
            possible=true;
            scanf("%d %d", &R, &C);
            
            for(int i=0;i<R;i++)
            {
                  scanf(" %s", tab[i]);     
            }  
            
            for(int i=0;i<R;i++)
            {
                    for(int j=0;j<C;j++)
                    {
                            if(tab[i][j]=='#')
                            {
                                   if(j+1 < C && i+1 < R)
                                   {
                                          if(tab[i+1][j]=='#' && tab[i+1][j+1]=='#' && tab[i][j+1]=='#')
                                          {
                                               tab[i][j]='/'; 
                                               tab[i][j+1]='\\';
                                               tab[i+1][j]='\\'; 
                                               tab[i+1][j+1]='/';                   
                                          } 
                                          else 
                                          {
                                          possible=false;
                                          break;   
                                          }      
                                   }
                                   else 
                                   {
                                        possible=false;
                                        break;   
                                   }                 
                            }       
                    }       
            }    
            if(possible)
            {
               printf("Case #%d:\n", z+1);
               for(int i=0;i<R;i++) printf("%s\n", tab[i]);         
            }
            else printf("Case #%d:\nImpossible\n", z+1);   
    }
}
