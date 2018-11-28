#include<stdio.h>
 
int main(void)
{ 
    int t, n, s, count, p, a[101], t1=1, i; 
    scanf("%d\n", &t); 
    while(t--) 
    {           
              count=0;           
              scanf("%d %d %d", &n, &s, &p);           
              for(i=0;i<n;i++)                           
                              scanf("%d", &a[i]);           
              for(i=0;i<n;i++)           
              {                           
                             if(a[i]%3==0)                           
                             {                                        
                                         if((a[i]/3)>=p)                                        
                                                        count++;                                        
                                         else if(s>0&&((a[i]/3)+1)>=p&&a[i])                                        
                                         {                                         
                                               count++;                                         
                                               s--;                                        
                                         }                                        
                             }                           
                             else                            
                             {                            
                                 if((a[i]/3)+1>=p&&a[i])                            
                                 count++;                           
                                 else if(s!=0&&(a[i]/3)+2>=p&&a[i]%3==2)                            
                                 {                                 
                                                                   count++;                                 
                                                                   s--;                             
                                 }                           
                             }                           
              }           
              printf("Case #%d: %d\n", t1++, count);           
    } 
    return 0;
}
