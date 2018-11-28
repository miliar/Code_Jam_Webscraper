#include<stdio.h>
//#include<conio.h>
int main()
{
    int s,p,n,j,count=0,k;
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {        
          scanf("%d %d %d",&n,&s,&p);
          int scores[n];
          k=s;
          //printf("\nhere%d",n);
          for(j=0;j<n;j++)
                scanf("%d",&scores[j]);
          count=0;
          for(j=0;j<n;j++)
          {
                 if(scores[j]%3!=0)
                 {
                           if((scores[j]/3)>=p||(((scores[j]/3)+1)>=p&&((scores[j]/3)+1<=scores[j])))
                                count++;
                           else if(((scores[j]/3)+2)>=p&&k>0&&((scores[j]/3)+2<=scores[j])&&scores[j]%3==2)     
                           {     
                                 count++;  k--;  
                           }
                 }                     
                 else if(scores[j]%3==0)
                 {
                      if((scores[j]/3)>=p)
                                count++;
                      else if(((scores[j]/3)+1)>=p&&k>0&&((scores[j]/3)+1<=scores[j]))     
                      {     count++;  k--;  }
                 }
          }
          printf("Case #%d: %d\n",i,count);     
         /*printf("Case #%d: %d for input %d %d %d ",i,count,n,s,p); 
          for(j=0;j<n;j++)
          {
              printf("%d ",scores[j]);                 
          } 
          printf("\n");*/
    }
    //getch();
}
