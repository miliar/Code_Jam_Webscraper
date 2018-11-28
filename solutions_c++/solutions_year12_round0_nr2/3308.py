#include <iostream>
#include <cstdio>
 
using namespace std;
 
int main()
{
    long int t,n,s,max,temp,count,j,i;
    scanf("%ld\n",&t);
    for(j=1;j<=t;j++)
    {
           
           scanf("%ld%ld%ld",&n,&s,&max);
           count=0;
           for(i=1;i<=n;i++)
           {
                     scanf("%ld",&temp);
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
                                         
           printf("Case #%ld: %ld\n",j,count);
           }
     return 0;
     
}  