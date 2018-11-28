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
  int g,i,j,k,l,m,n,r,s,t,a[2000],mx,sum;

    freopen("C-large.in","r",stdin);
   freopen("C.txt","w",stdout);
  cin >> t;
  for(g=1;g<=t;g++)
  {
      mx = 9999999;
      cin >> n;
      m = s = sum = 0;
      for(i=1;i<=n;i++)
      {
        cin >> a[i];
        m ^= a[i];
        if(a[i] < mx)mx = a[i];
      }


      if(m == 0)
      {
          for(i=1;i<=n;i++)
          {
              if(mx == a[i] && s == 0)
              {
                  s = 1;
                  continue;
              }
              sum += a[i];
          }
          cout <<"Case #"<<g<<": "<<sum<<endl;
      }
      else
      {
          cout <<"Case #"<<g<<": "<<"NO"<<endl;
      }
  }
  return 0;
}
