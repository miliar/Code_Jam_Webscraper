#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std; typedef unsigned long ulong; typedef long long llong;
typedef unsigned long long ullong;

int x[100],y[100],r[100];

double dist(int i,int j)
{
  double d=sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]));
  return (d+r[i]+r[j])*0.5;
}

double doit(int n)
{
  double R=100000;
  if (n==1) return r[0];
  else if (n==2) return max(r[0],r[1]);
  else
  {
    for(int i=0;i<n;i++)
    {
      int i1=(i+1)%3, i2=(i+2)%3;
      R <?= max(double(r[i]), dist(i1,i2));
    }
    return R;
  }
}

int main()
{
int cases;

cin >> cases; getchar();

for(int loop=1;loop<=cases;loop++)
{
  int n; cin >> n;

  for(int i=0;i<n;i++)
  {
    scanf("%d%d%d",&x[i],&y[i],&r[i]);
  }

  printf("Case #%d: ",loop);

  printf("%f\n", doit(n));

  fflush(stdout);
}

}
