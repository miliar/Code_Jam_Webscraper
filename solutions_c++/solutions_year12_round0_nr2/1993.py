#include<stdio.h>
//#include<conio.h>

int main()
{
    int test_cases, n, s_trips, p;
    int i;
    int j;
    int data;
    int result;
    int p1, p2;
    freopen("G:\out.txt","w",stdout);
    freopen("G:\in.txt", "r", stdin);
    freopen("G:\error.txt", "w", stderr);
     
    scanf("%d",&test_cases);
    
    for(i=0;i<test_cases;i++)
     {
                     result =0;
                     scanf("%d%d%d",&n, &s_trips, &p );
                     
                     if((p-1)>=0)
                        p1=3*p - 2;
                     else
                       p1=3*p;
                       
                     if((p-2)>=0)  
                       p2=3*p - 4;
                      else
                       p2=p1;
                        
                     for(j=0;j<n;j++)
                     {
                        scanf("%d",&data); 
                        if(data>=p1) 
                         ++result;
                        else if(s_trips>0 && data>=p2) 
                        {
                              ++result; 
                              --s_trips;                              
                        }
                     }
                     printf("Case #%d: %d\n", i+1, result);         
                    
     }
     return 0;
} 
