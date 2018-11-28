#include<iostream>
#include<algorithm>
using namespace std;
char cc[110][10],dd[110][10],str[110],list[110];
int main()
{
     freopen("B-large.in","r",stdin);
     freopen("B-large.out","w",stdout);

     int t,c,d,n;
     int i,j,k,p;

     scanf("%d",&t);
     for(i=1;i<=t;i++)
     {
          scanf("%d",&c);
          for(j=0;j<c;j++)
          scanf("%s",cc[j]);

          scanf("%d",&d);
          for(j=0;j<d;j++)
          scanf("%s",dd[j]);

          scanf("%d",&n);
          scanf("%s",str);

          int indx=0;
          for(j=0;j<n;j++)
          {
               list[indx++]=str[j];

               if(indx>1)
               {
                    for(k=0;k<c;k++) // check combine
                    {
                         if((list[indx-1]==cc[k][0]&&list[indx-2]==cc[k][1])||(list[indx-1]==cc[k][1]&&list[indx-2]==cc[k][0]))
                         {
                              indx--;
                              list[indx-1]=cc[k][2];
                              break;
                              }
                         }

                    for(k=0;k<d;k++) // check oppose
                    {
                         for(p=0;p<indx-1;p++)
                         {
                              if((list[indx-1]==dd[k][0]&&list[p]==dd[k][1])||(list[indx-1]==dd[k][1]&&list[p]==dd[k][0]))
                              {
                                   indx=0;
                                   break;
                                   }
                              }
                         }
                    }
               }

          printf("Case #%d: [",i);
          for(j=0;j<indx;j++)
          {
               printf("%c",list[j]);
               if(j<indx-1)
               printf(", ");
               }
          printf("]\n");
          }
     return 0;
     }
