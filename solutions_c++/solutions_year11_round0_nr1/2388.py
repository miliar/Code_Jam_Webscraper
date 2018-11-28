#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
int num[1000];
char color[1000];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int last_orange,last_black,total,total_orange,total_black;
    int n,m,i,l,k;
    char ch;
    scanf("%d",&n);
    for(l=0;l<n;l++)
     {
      last_orange=last_black=1;
      total=total_orange=total_black=0;
      scanf("%d",&m);

      for(k=0;k<m;k++)
       scanf(" %c %d",&color[k],&num[k]);

       color[m]=0;

      for(i=0;i<m;i++)
      {
          if(color[i]=='O')
          {
              total_orange+=fabs(num[i]-last_orange)+1;
              last_orange=num[i];
              if(total_orange<=total_black)
               total_orange=total_black+1;
              total=total_orange;
              }
          else if(color[i]='B')
          {
              total_black+=fabs(num[i]-last_black)+1;
              last_black=num[i];
              if(total_black<=total_orange)
               total_black=total_orange+1;
              total=total_black;

              }

          }

          printf("Case #%d: %d\n",l+1,total);

     }


    return 0;
    }
