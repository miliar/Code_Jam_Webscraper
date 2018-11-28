#include"stdio.h"

int main()
{
    int test,n,surprising,c,p,total,count,k,r;
    scanf("%d",&test);
    for(c=0;c<test;c++)
    {
                       count=0;
                       scanf("%d%d%d",&n,&surprising,&p);
                       for(k=0;k<n;k++)
                       {
                                       scanf("%d",&total);
                                       r=total/3;
                                       switch(total%3)
                                       {
                                                         case 0 :
                                                              {
                                                                    if(r>=p)
                                                                    {
                                                                            count++;
                                                                    }
                                                                    else if(surprising > 0)
                                                                    {
                                                                         if(r+1>=p && r-1>=0)
                                                                         {
                                                                                   count++;
                                                                                   surprising--;
                                                                         }
                                                                    }
                                                                    break;
                                                              }
                                                         case 1 :
                                                              {
                                                                    if(r+1>=p)
                                                                    {
                                                                              count++;
                                                                    }
                                                                    break;
                                                              }
                                                         case 2 :
                                                              {
                                                                    if(r+1>=p)
                                                                    {
                                                                              count++;
                                                                    }
                                                                    else if(surprising>0)
                                                                    {
                                                                         if(r+2>=p)
                                                                         {
                                                                                   count++;
                                                                                   surprising--;
                                                                         }
                                                                    }
                                                                    break;
                                                              }
                                                         default :
                                                                 printf("error");
                                       }
                       }
                       printf("Case #%d: %d\n",c+1,count);
    }
    return 0;
}
                                                                                
                       
    
