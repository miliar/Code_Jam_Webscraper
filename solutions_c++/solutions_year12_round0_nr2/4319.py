#include <cstdio>

using namespace std;

int main()
{
    FILE *fin, *fout; 
    fin = fopen("B-small-attempt2.in", "r");
    fout = fopen("out.txt", "w");
    
    int t, i;
    fscanf(fin, "%d", &t);
    
    int num[150];
    for(i = 1; i <= t; i++)
    {
          int n, s, p, j, total = 0;
         fscanf(fin ,"%d%d%d", &n, &s, &p);
         
         for(j = 1; j <= n; j++)
               fscanf(fin, "%d", &(num[j]));
         for(j = 1; j <= n; j++)
         {
               if(num[j] == 0)
               {
                    if(p == 0)
                         total ++;          
               }
               else if(num[j] % 3 == 0)
               {
                      if(num[j] / 3 >= p)
                                total ++;
                      else if((s > 0) && (num[j] / 3 + 1 >= p))
                      {
                           total ++;
                           s --;             
                      }          
               }else if(num[j] % 3 == 1)
               {
                     if((num[j] + 2) / 3 >= p)
                            total ++;  
                     else if((s > 0) && ((num[j] + 2) / 3 >= p))
                     {
                          total ++;
                          s --;
                     }           
               }
               else if(num[j] % 3 == 2)
               {
                    if((num[j] + 1) / 3 >= p)
                               total++;
                    else if((s > 0) && ((num[j] + 1) / 3 + 1 >= p))
                    {
                         total++;
                         s--;           
                    }     
               }   
         }
         fprintf(fout, "Case #%d: %d\n", i, total); 
    }
    fclose(fin);
    fclose(fout);
    return 0;
} 
