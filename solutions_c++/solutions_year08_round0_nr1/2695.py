#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int allnum,casenum,ennum,connum,sw,cnt;
    char buffer[128];
    char en[100][128],i,j;
    char map[100];
    freopen("a.in","r",stdin);
    gets(buffer);
    allnum = atoi(buffer);
    for(casenum=1;casenum<=allnum;casenum++)
    {
           gets(buffer);
           ennum = atoi(buffer);                 
           for(i=0;i<ennum;i++)
           {
               gets(en[i]);
            }
            gets(buffer);
            connum = atoi(buffer);
            memset(map,0,100);
            sw = 0;
            cnt = 0;
            for(i=0;i<connum;i++)
            {
                gets(buffer);
                for(j=0;j<ennum;j++)
                {
                     if(strcmp(buffer,en[j]) == 0)
                         break;               
                }
                if(j<ennum)
                {
                  if(map[j] == 0)
                  {
                        cnt++;
                        if(cnt == ennum)
                        {
                          memset(map,0,100);
                          cnt=1;    
                          sw++;   
                        }       
                        map[j] = 1;        
                  }           
                           
                }                 
                                 
             }                        
                                            
                                            
            printf("Case #%d: %d\n",casenum,sw);         
        }
    
    
    
    return 0;
    }
