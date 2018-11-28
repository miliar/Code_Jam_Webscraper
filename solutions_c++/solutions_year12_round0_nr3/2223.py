#include"stdio.h"

int main()
{
    int testcase,a,b,c,k;
    int n,x,r,narray[10],tarray[10],test,m,count;
    
    scanf("%d",&testcase);
    
    for(c=0;c<testcase;c++)
    {
                           count=0;
                           scanf("%d%d",&a,&b);
                           for(n=a;n<b;n++)
                           {
                                           //printf("%d - count b4 %d\n",n,count);
                                
                                for(r=1,x=0;;r=r*10,x++)
                                {
                                                        if(n%r==n)
                                                                  break;
                                } 
                                
                                for(k=0,r=1;k<x;k++,r=r*10)
                                {
                                                           narray[x-k-1]=((int)n/r)%10;
                                }
                                
                                for(k=1;k<x,test!=n;k++)
                                {
                                                test=0;
                                                  for(m=0;m<x;m++)
                                                  {
                                                                  
                                                                  if(m>=x-k)
                                                                  {
                                                                            tarray[m-x+k]=narray[m];
                                                                  }
                                                                  else
                                                                  {
                                                                      tarray[m+k]=narray[m];
                                                                  }
                                                  }
                                                  
                                                  for(m=0,r=1;m<x;m++,r=r*10)
                                                  {
                                                                             test=test+tarray[x-m-1]*r;
                                                  }
                                                  
                                                  if(tarray[0]!=0 && test>n && test<=b && test>a)
                                                  {
                                                                  //printf("%d - %d\n",k,test);
                                                                  count++;
                                                  }
                                }
                           }
                           printf("Case #%d: %d\n",c+1,count);
    }
    return 0;
}
                                                                            
                                                            
                                                
                                
                                           
