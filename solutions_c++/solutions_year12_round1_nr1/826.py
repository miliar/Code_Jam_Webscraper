#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
  int i1,n1;
  cin >> n1;

  int i,j,k,l,m,n;

  for (i1=1;i1<=n1;++i1)
  {
    int a,b;
    cin >> a >> b;
    
    double prob = 0.0;

    vector<double> p(b);

    for (i=0;i<a;++i)
    {
      cin >> p[i];
      prob += log(p[i]);
    };

    double cost = exp(prob)*(b-a+1)+(1-exp(prob))*(b-a+1+b+1);

    for (i=1;i<a;++i)
    {
      k = a-i;
      double prob2 = prob-log(p[k]);
      double cost2 = exp(prob2)*(i+b-(a-i)+1)+(1-exp(prob2))*(i+b-(a-i)+1+b+1);

      if (cost2<cost)
        cost = cost2;
    };
    
    double cost2 = 1+b+1;
    if (cost2<cost)
      cost = cost2;

    printf("Case #%d: %.6f\n", i1, cost);
  };

};

