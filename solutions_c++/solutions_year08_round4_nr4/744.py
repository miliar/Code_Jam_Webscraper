#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;


long cas,n,cas1,value,i,j,k,min_1,count1,A[1009];
char sa[1009],sp[1009];



int main()
{
////freopen("D-small-attempt0.in","r",stdin);
/////freopen("d_s.out","w",stdout);    



scanf("%ld",&cas);


for(cas1=1;cas1<=cas;cas1++)    
    {
    scanf("%ld",&value);                            
    scanf("%s",sa);                            
    
    for(i=0;i<value;i++)
    A[i]=i;
    n=strlen(sa);
    min_1=n;
    
    for(i=0;i<n;i++)
    {
    j=i/value;
    k=i%value;
    sp[i]=sa[j*value+A[k]];        
    }
    sp[n]=0;
    count1=1;
    for(i=1;i<n;i++)
    if(sp[i]!=sp[i-1])
    count1++;
    if(count1<min_1)
    min_1=count1;
    
    while( next_permutation(A,A+value) )  
    {

   for(i=0;i<n;i++)
    {
    j=i/value;
    k=i%value;
    sp[i]=sa[j*value+A[k]];        
    }
    sp[n]=0;
    count1=1;
    for(i=1;i<n;i++)
    if(sp[i]!=sp[i-1])
    count1++;
    if(count1<min_1)
    min_1=count1;
           
    }                           
                                
                                
   
   printf("Case #%ld: %ld\n",cas1,min_1);                             
                                
                                
    }
    
    
    
    
    
    
return 0;    
}
