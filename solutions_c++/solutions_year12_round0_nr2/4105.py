#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int t,n,s,max,temp,count,j,i;
    scanf("%d\n",&t);
    for(j=1;j<=t;j++)
    {
           
           scanf("%d%d%d",&n,&s,&max);
           count=0;
           for(i=1;i<=n;i++)
           {
                     scanf("%d",&temp);
                     if(temp==0)
                        {        if(max==0)
                                         {  count++;
                                           continue;}
                                 else
                                           continue;
                                           }                        
                     if(temp>=3*max-2)
                                   count++;
                     else
                     {
                         if(temp>=3*max-4 && s!=0)
                                      {    count++;
                                          s--;
                                          }
                                          }
                                         
                                         }                   
                                         
           printf("Case #%d: %d\n",j,count);
           }
     return 0;
     
}             
