#include<stdio.h>
int main()
{
    int t,sur,min_scor,n;
 int count=1;
 scanf("%d",&t);
 while(t--)
 {
           scanf("%d%d%d",&n,&sur,&min_scor);
           int i;
           int num[300];
           for(i=0;i<n;i++)
           scanf("%d",&num[i]);
           int j;
           int tmp;
           for(i=0;i<n-1;i++)
           for(j=i+1;j<n;j++)
           if(num[i]>num[j])
           {
                        tmp=num[i];
                        num[i]=num[j];
                        num[j]=tmp;
                        }
                       
           int limit=3*min_scor;
           limit=limit-3;
           int result=0;
           for(i=0;num[i]<limit-1;i++);
           for(;num[i]<=limit;i++){
                                   if(sur>0)
                                   {
                                            sur--;
                                            if(num[i]!=0)result++;
                                            }
                                            }
                                            for(;i<n;i++)result++;
           printf("Case #%d: %d\n",count++,result);
           }
           }
    
