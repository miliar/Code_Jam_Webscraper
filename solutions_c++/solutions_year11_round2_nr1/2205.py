# include <stdio.h>
# include <sstream>
# include <iostream>
# include <string.h>
# include <vector>
# include <string>
# include <algorithm>
# include <map>
# include <math.h>
# include <stdlib.h>

using namespace std;

int main()
{
   int i,j,k,l,m,n,t,a[200],at[200],o,b[200],ba[200],bat[200],ow[200];
   double ca[200],cat[200],opw,op[200],oop[200];
   char ab[200][200];
   double r,s,p,w,oow,tp,tr,tot;
  freopen("A-large.in","r",stdin);
  freopen("a-out.txt","w",stdout);
  cin >> t;

  for(k=1;k<=t;k++)
  {
       cin >> n;

       for(i=1;i<=n;i++)
       {
           for(j=1;j<=n;j++)
           {
               cin >> ab[i][j];
           }
       }

       //win
       for(i=1;i<=n;i++)
       {
           at[i] = a[i] =  0;
           for(j=1;j<=n;j++)
           {
               if(ab[i][j] == '1'){++a[i];++at[i];}
               else if(ab[i][j] == '0')
               ++at[i];
           }
       }

       //ow

       for(i=1;i<=n;i++)
       {
           bat[i] = at[i];
           ba[i] = a[i];

       }



       for(i=1;i<=n;i++)
       {
         opw=0.0;
         for(j=1;j<=n;j++)
         {
             if(i == j)continue;
             if(ab[j][i] == '1')
             {
                 tr = bat[j]-1;
                 tp = ba[j]-1;
                 opw += (tp/tr);
             }
             else if(ab[j][i] == '0')
             {
                tr = bat[j]-1;
                tp = ba[j];
                opw += (tp/tr);
             }

         }

         op[i] = (double)(opw/bat[i]);

       }

      cout << "Case #"<<k<<":"<<endl;
       for(i=1;i<=n;i++)
       {
           opw = 0.0;
           for(j=1;j<=n;j++)
           {
              if(i==j)continue;
              if(ab[i][j] == '0'||ab[i][j] == '1')
              {
                  opw += op[j];
              }

           }
           oop[i] = (double)(opw/bat[i]);

       }

       tot = 0.0;
       for(i=1;i<=n;i++)
       {
           tot = (double)(a[i]*1.0/at[i]);
           tot *= 0.25;
           tot += (0.5*op[i]);
           tot += (0.25*oop[i]);
           cout << tot<<endl;
           tot =0.0;
       }



  }
  return 0;
}


/*
3
4
.11.
0.00
01.1
.10.

*/
