#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
using namespace std;


int main()
{
    int cas;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &cas);
    int T=0;
    while(cas--)
    {
       int n;
       scanf("%d", &n);
       T++;
       int res = 0, maxx=(1<<30), dd=0;
       for(int i=0; i<n; ++i)
       {
          int tmp;
          scanf("%d", &tmp);
          dd^=tmp;
          res += tmp;
          maxx = min(maxx, tmp);
       }
       res -= maxx;
       if(dd==0)
          printf("Case #%d: %d\n",T, res);
       else
          printf("Case #%d: NO\n",T);
    }
    //system("pause");
    return 0;
} 

