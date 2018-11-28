#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <string>

using namespace std;

int main()
{
  int n1,i1;
  cin >> n1;
  for (i1=1;i1<=n1;++i1)
  {
    int i,j,k,l,m,n;
    cin >> n;
    vector<double> s(n), y(n);
    
    double x = 0;

    for (i=0;i<n;++i)
    {
      cin >> s[i];
      x += s[i];
    };

    for (i=0;i<n;++i)
    {
      double low=0, high=1;
      while (high-low>=0.00000001)
      {
        double mid=(low+high)/2;
        
        double bound = s[i]+mid*x;
        double remain = 1-mid;
        for (j=0;j<n;++j)
          if (i!=j && s[j]<bound)
            remain -= (bound-s[j])/x;

        if (remain<0)
          high = mid;
        else
          low = mid;
      };
      y[i]=low;
    };



    printf("Case #%d:", i1);
    for (i=0;i<n;++i)
      printf(" %.6f", y[i]*100);
    printf("\n");
  };

};
