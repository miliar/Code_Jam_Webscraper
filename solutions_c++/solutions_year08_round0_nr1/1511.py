#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct inf
{
        int flag;
        char name[100];
} inf;

int main()
{
    int m,n,p;
    int i,j,k;
    inf *q = NULL;
    int *r;
    int sw;
    char tmp[100];
    FILE *f,*g;
    
    f = fopen("in.txt","r");
    g = fopen("out.txt","w");
    
    fscanf(f,"%d\n",&m);    
    for(i = 0; i < m; ++i)
    {
               
                sw = 0;
                fscanf(f,"%d\n",&n);    

                q = (inf*)calloc(n,sizeof(struct inf));
                
                for(j = 0; j < n; ++j)
                {
                      char c;
                      int t = 0;
                      while (((c = fgetc(f))!= EOF)&&(c!='\n'))
                            q[j].name[t++] = c;
                      
                      q[j].name[t] = '\0';                                                 
                      
                      
                }
                fscanf(f,"%d\n",&p);
                                    
                r = (int*)calloc(p,sizeof(int));
                
                for(k = 0; k < p; ++k)
                {
                      char c;
                      int t = 0;
                      int l = 0;
                      while (((c = fgetc(f))!= EOF)&&(c!='\n'))
                            tmp[t++] = c;
                      
                      tmp[t] = '\0'; 
                        
                     for(l = 0 ; l < n;l++)
                     {
                             
                             if(!strcmp(q[l].name,tmp))
                             {
                                   r[k] = l;
                                   
                                   break;
                             }
                     }
                                          
                   
                } 
               
                sw = 0;
                 for(k = 0; k < p; ++k)
                {
                       int s = 0;
                        
                       
                        
                       for(j = 0; j < n; ++j)
                       {
                               s += q[j].flag;
                       }
                       
                       if(q[r[k]].flag == 0)
                           if(s ==n-1)
                           {
                                sw++;
                                for(j = 0; j < n; ++j)
                                {
                                      q[j].flag = 0;
                                }
                                q[r[k]].flag = 1;
                           }
                           
                       q[r[k]].flag = 1;
                       
                       
                }
            
            
            
                 free(q);
                 free(r);     
            
              fprintf(g,"Case #%d: %d\n",i+1,sw);

    }
        
    fclose(f);
    fclose(g);
    fflush(stdin);
    scanf(" ");

    return 0;
}
