#include"stdio.h"

int main()
{
    int t,n,s,i,p,all,count,k,r;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
                       count=0;
                       scanf("%d%d%d",&n,&s,&p);
                       for(k=0;k<n;k++)
                       {
                                       scanf("%d",&all);
                                       r=all/3;
                                       if((all%3)==0)
                                       {
                                                       if(r>=p)
                                                               count++;
                                                       else if(s > 0)
                                                       {
                                                                         if(r+1>=p && r-1>=0)
                                                                         {
                                                                                   count++;
                                                                                   s--;
                                                                         }
                                                       }
                                       }
                                       else if(((all%3)==1)&&(r+1>=p))
                                                count++;
                                       else if((all%3)==2)
                                                            if(r+1>=p)
                                                            {
                                                                      count++;
                                                            }
                                                            else if(s>0)
                                                            {
                                                                 if(r+2>=p)
                                                                 {
                                                                           count++;
                                                                           s--;
                                                                 }
                                                            }
                                       }
                                       printf("Case #%d: %d\n",i+1,count);
    }
    return 0;
}
                        
                                                                    
