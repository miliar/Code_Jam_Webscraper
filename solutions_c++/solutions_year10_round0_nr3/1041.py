#include<iostream>
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<map>
#include<vector>
using namespace std;
const int cas=10;
const int n=1000,r=100000000,m=1000000000;
int main()
{
  freopen("c2.in","w",stdout);
  printf("%d\n",cas);
  for (int i=1;i<=cas;i++)
  {
    printf("%d %d %d\n",r,m,n);
    for (int j=1;j<=n;j++)
      printf("%d ",10000000);
    printf("\n");
  }
  return 0;
}
