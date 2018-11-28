# include <stdio.h>
# include <stdlib.h>
# include <sstream>
# include <iostream>
# include <string>
# include <string.h>
# include <math.h>
# include <algorithm>


using namespace std;

int main()
{
   int i,j,k,l,m,n,r,s,d,t,rd,val[200],ov,bv;
   char a[200],b[200],o[200];
   r = 0;

   freopen("A-large.in","r",stdin);
   freopen("A.txt","w",stdout);

   cin >> n;
   while(n--)
   {
       cin >> k;
       for(i=1;i<=k;i++)
       cin >> a[i] >> val[i];

       ov = bv = 1;
       t = 0;

       for(i=1;i<=k;i++)
       {
          if(a[i] == 'O')
          {
              d = abs(val[i] - ov);
              ++d;
              ov = val[i];
              t += d;

              for(j=i+1;j<=k;j++)
              if(a[j] == 'B')
              {
                  if(val[j] > bv)
                  {
                      bv += d;
                      if(bv > val[j])bv = val[j];
                  }
                  else if(val[j] < bv)
                  {
                      bv -= d;
                      if(bv < val[j])bv = val[j];
                  }
                  break;
              }

          }
          else if(a[i] == 'B')
          {
              d = abs(val[i]-bv);
              ++d;
              bv = val[i];
              t += d;

              for(j=i+1;j<=k;j++)
              if(a[j] == 'O')
              {
                  if(val[j] > ov)
                  {
                      ov += d;
                      if(ov > val[j])ov = val[j];
                  }
                  else if(val[j] < ov)
                  {
                      ov -= d;
                      if(ov < val[j])ov = val[j];
                  }
                  break;
              }
          }
       }

       cout <<"Case #"<<++r<<": "<<t<<endl;
   }
   return 0;
}
