#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

int main()
  {
  int T;

  scanf("%d ",&T);
  for(int t=0;t<T;++t)
    {
    int N;
    scanf("%d ",&N);

    vector<int> x(N),y(N),r(N);
    for(int i=0;i<N;++i)
      {
      scanf("%d %d %d ", &x[i], &y[i], &r[i]);
      }

    if (N==1)
      {
      printf("Case #%d: %lf\n",t+1,1.0*r[0]);
      continue;
      }

    if (N==2)
      {
      printf("Case #%d: %lf\n",t+1,1.0*max(r[0],r[1]));
      continue;
      }

    if (N==3)
      {
      double ret=1000000000;
      double t01= (sqrt(1.0* (x[0]-x[1])*(x[0]-x[1]) + (y[0]-y[1])*(y[0]-y[1]) ) +r[0]+r[1])*0.5;
      double t02= (sqrt(1.0* (x[0]-x[2])*(x[0]-x[2]) + (y[0]-y[2])*(y[0]-y[2]) ) +r[0]+r[2])*0.5;
      double t12= (sqrt(1.0* (x[1]-x[2])*(x[1]-x[2]) + (y[1]-y[2])*(y[1]-y[2]) ) +r[1]+r[2])*0.5;
      double ret1=std::max(t01,1.0*r[2]);
      double ret2=std::max(t02,1.0*r[1]);
      double ret3=std::max(t12,1.0*r[0]);
      printf("Case #%d: %lf\n",t+1,1.0*min(min(ret1,ret2),ret3));
      continue;
      }
    }

  return 0;
  }