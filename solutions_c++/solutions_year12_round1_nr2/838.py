#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
  int n1,i1;
  cin >> n1;
  int i,j,k,l,m,n;

  for (i1=1;i1<=n1;++i1)
  {
    cin >> n;
    vector<int> a(n),b(n);
    vector<bool> c(n), d(n);
    for (i=0;i<n;++i)
    {
      cin >> a[i] >> b[i];
      c[i] = true;
      d[i] = true;
    };

  
    int star = 0;
    int ans = n;
    bool impossible = false;   

    for (i=0;i<n;++i)
    {
      int best=10000000000, bestk;
      for (j=0;j<n;++j)
        if (d[j] && b[j]<best)
        {
          best = b[j];
          bestk = j;
        };

      while (star < best)
      {
        int best2=-1, choose = -1;
                
        for (j=0;j<n;++j)
        {
          
          if (c[j] && d[j] && a[j]<=star && b[j]>best2)
          {
            best2 = b[j];
            choose = j;
          };
        };
      

        if (choose == -1)
        {
          impossible = true;
          break;
        }
        else
        {
          c[choose] = false;
          star += 1;
          ans += 1;
        };
      };

      if (impossible)
        break;

      if (!c[bestk])
        star += 1;
      else
        star += 2;

      d[bestk] = false;      
    };

    if (impossible)
      printf("Case #%d: Too Bad\n", i1);
    else
      printf("Case #%d: %d\n", i1, ans);
  };


};

